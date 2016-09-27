#!/bin/bash

set -o nounset
set -o errexit

VERBOSE_MODE=0

function error_handler()
{
  local STATUS=${1:-1}
  [ ${VERBOSE_MODE} == 0 ] && exit ${STATUS}
  echo "Exits abnormally at line "`caller 0`
  exit ${STATUS}
}
trap "error_handler" ERR

PROGNAME=`basename ${BASH_SOURCE}`
DRY_RUN_MODE=0

function print_usage_and_exit()
{
  set +x
  local STATUS=$1
  echo "Usage: ${PROGNAME} [-v] [-v] [--dry-run] [-h] [--help] <train>"
  echo ""
  echo "<train>              train file"
  echo " Options -"
  echo "  -v                 enables verbose mode 1"
  echo "  -v -v              enables verbose mode 2"
  echo "      --dry-run      show what would have been dumped"
  echo "  -h, --help         shows this help message"
  exit ${STATUS:-0}
}

function debug()
{
  if [ "$VERBOSE_MODE" != 0 ]; then
    echo $@
  fi
}

GETOPT=`getopt -o vh --long dry-run,help -n "${PROGNAME}" -- "$@"`
if [ $? != 0 ] ; then print_usage_and_exit 1; fi

eval set -- "${GETOPT}"

while true
do case "$1" in
     -v)            let VERBOSE_MODE+=1; shift;;
     --dry-run)     DRY_RUN_MODE=1; shift;;
     -h|--help)     print_usage_and_exit 0;;
     --)            shift; break;;
     *) echo "Internal error!"; exit 1;;
   esac
done

if (( VERBOSE_MODE > 1 )); then
  set -x
fi


# template area is ended.
# -----------------------------------------------------------------------------
if [ ${#} != 1 ]; then print_usage_and_exit 1; fi

# current dir of this script
CDIR=$(readlink -f $(dirname $(readlink -f ${BASH_SOURCE[0]})))
PDIR=$(readlink -f $(dirname $(readlink -f ${BASH_SOURCE[0]}))/..)

# -----------------------------------------------------------------------------
# functions

function make_calmness()
{
	exec 3>&2 # save 2 to 3
	exec 2> /dev/null
}

function revert_calmness()
{
	exec 2>&3 # restore 2 from previous saved 3(originally 2)
}

function close_fd()
{
	exec 3>&-
}

function jumpto
{
	label=$1
	cmd=$(sed -n "/$label:/{:a;n;p;ba};" $0 | grep -v ':$')
	eval "$cmd"
	exit
}

# end functions
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# main 

make_calmness
if (( VERBOSE_MODE > 1 )); then
	revert_calmness
fi

python='/usr/bin/python2.7'

mkdir -p ${CDIR}/wdir
WDIR=${CDIR}/wdir
train=$1

# make lexicon
${python} ${CDIR}/makelexicon.py < ${train} > ${WDIR}/lexicon.txt

# make input symbol
${python} ${CDIR}/makesymbol.py --input < ${WDIR}/lexicon.txt > ${WDIR}/char.sym

# make output symbol
${python} ${CDIR}/makesymbol.py --output < ${WDIR}/lexicon.txt > ${WDIR}/word.sym

# compile and optimize fst
fstcompile --isymbols=${WDIR}/char.sym --osymbols=${WDIR}/word.sym ${WDIR}/lexicon.txt ${WDIR}/lexicon.cmp
fstdeterminize ${WDIR}/lexicon.cmp ${WDIR}/lexicon.det
fstminimize    ${WDIR}/lexicon.det ${WDIR}/lexicon.min
fstarcsort     ${WDIR}/lexicon.min ${WDIR}/lexicon.srt

# print out fst
fstprint --isymbols=${WDIR}/char.sym --osymbols=${WDIR}/word.sym ${WDIR}/lexicon.srt > ${WDIR}/lexicon.srt.txt

# relabel <w> to <eps>
# <eps> 0
# <w> 3
echo "3 0" > ${WDIR}/map.txt
fstrelabel --relabel_ipairs=${WDIR}/map.txt ${WDIR}/lexicon.srt ${WDIR}/lexicon.fst
fstprint --isymbols=${WDIR}/char.sym --osymbols=${WDIR}/word.sym ${WDIR}/lexicon.fst > ${WDIR}/lexicon.fst.txt

# prepare config xml file
cp -rf ${CDIR}/config.xml ${WDIR}

# prepare input data for decoding
${python} ${CDIR}/separatechars.py < ${train} > ${WDIR}/input.txt

# decoding
cd ${WDIR}
${PDIR}/src/test_ckyfd config.xml < input.txt > output.txt

close_fd

# end main
# -----------------------------------------------------------------------------
