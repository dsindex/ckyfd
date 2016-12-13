# Autoconf configuration for ckyfd
#

AC_INIT([ckyfd],[0.0.1],[hazzling@gmail.com],[ckyfd])
PACKAGE=ckyfd

AC_PREREQ(2.50)

AC_CONFIG_AUX_DIR([build])

AC_CANONICAL_TARGET

AM_INIT_AUTOMAKE([foreign])
AC_CONFIG_HEADERS([include/auto_config.h])

AC_PREFIX_DEFAULT(`pwd`/install)
AC_MSG_RESULT("prefix is $prefix.")

AC_ARG_ENABLE(debug,
   [  --enable-debug=val remove optimization option gcc, val=yes or no],
   [case "${enableval}" in
      yes) debug=true CFLAGS="-g";;
      no)  debug=false CFLAGS="-g -O2" ;;
      *) AC_MSG_ERROR(bad value ${enableval} for --enable-debug) ;;
    esac],[debug=false])
AM_CONDITIONAL(DEBUG,test x"$debug" = xtrue)

AC_ARG_ENABLE(gprof,
   [  --enable-gprof=val using gnu profiler, val=yes or no, use exclusively with --enable-pprof],
   [case "${enableval}" in
      yes) gprof=true CFLAGS="-g -pg";;
      no)  gprof=false CFLAGS="-g -O2" ;;
      *) AC_MSG_ERROR(bad value ${enableval} for --enable-gprof) ;;
    esac],[gprof=false])
AM_CONDITIONAL(GPROF,test x"$gprof" = xtrue)

AC_ARG_WITH(kyfd,
	AC_HELP_STRING(
		[--with-kyfd=DIRECTORY],
		[set kyfd directory path]),
	[kyfd="$withval"],
	[path=/home/kyfd/install
     if test -f ${path}/include/decoder.h ; then
        kyfd_path=${path}
     else
	    AC_MSG_ERROR(Cannot locate kyfd include header. You should either use --with-kyfd option or install kyfd in ${path})
     fi
     kyfd=${kyfd_path}
	]
)
AC_MSG_RESULT(found kyfd in $kyfd.);
AC_SUBST(kyfd)

AC_ARG_ENABLE(python,
   [  --enable-python=val make python wrapper library, val=yes or no],
   [case "${enableval}" in
      yes) python=true ;;
      no)  python=false ;;
      *) AC_MSG_ERROR(bad value ${enableval} for --enable-python) ;;
    esac],[python=false])
AM_CONDITIONAL(PYTHON_USE,test x"$python" = xtrue)

AM_COND_IF( [PYTHON_USE],[ 
AC_ARG_WITH(pythoninc,
    AC_HELP_STRING(
        [--with-pythoninc=DIRECTORY],
        [set python include directory path]),
    [pythoninc="$withval"],
    [path=/usr/include/python2.7
     if test -f ${path}/Python.h ; then
        python_header=${path}
     else
        AC_MSG_ERROR(Cannot locate python include header. You should either use --with-pythoninc option or place python header in ${path})
     fi
     pythoninc=${python_header}
    ]
)
AC_MSG_RESULT(found python header in $pythoninc.);
AC_SUBST(pythoninc) ] )

dnl ---------------------------------------------------------------------------
AH_TOP([#ifndef AUTO_CONFIG_H
#define AUTO_CONFIG_H 1
])

AH_BOTTOM([
#endif /* AUTO_CONFIG_H */
])

AH_VERBATIM([1_NEAR_TOP__],[
/* example */
#undef CKYFD_HOME
])

AC_DEFINE(CKYFD_HOME,`pwd`)

dnl ---------------------------------------------------------------------------
dnl Checks for programs
AC_PROG_CXX
AC_PROG_CC
AC_PROG_INSTALL
AC_PROG_LIBTOOL


dnl should fail configure when followings headers does not exist.
AC_CHECK_HEADERS( \
	string.h stdlib.h stdio.h sys/types.h sys/stat.h fcntl.h \
    getopt.h \
)

AC_CHECK_FUNCS( \
	getopt \
	getopt_long \
)
CKYFD_RELEASE_DATE=`LANG=C date "+%a %b %d %T %Z %Y"`

AC_SUBST(PACKAGE)
AC_SUBST(CKYFD_RELEASE_DATE)

AC_SUBST(LIBTOOL)

AC_SUBST(AM_CFLAGS)
AC_SUBST(AM_CPPFLAGS)
AC_SUBST(AM_LDFLAGS)
AC_SUBST(AM_LIBTOOLFLAGS)

AC_CONFIG_FILES([
	Makefile
	src/Makefile
	include/Makefile
]) 

AM_COND_IF( [PYTHON_USE], [
AC_CONFIG_FILES([
	wrapper/python/Makefile
	wrapper/python/test.py
	wrapper/python/test_rouzeta.py
])] ) 

AC_OUTPUT


