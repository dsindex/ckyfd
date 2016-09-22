# Makefile.am for top_builddir

if PYTHON_USE
SUBDIRS = include src wrapper/python
DIST_SUBDIRS = include src etc wrapper/python
else
SUBDIRS = include src
DIST_SUBDIRS = include src
endif

TARBALL_TARGET=./${PACKAGE}-${VERSION}-bin/

dist-bin :
	make DESTDIR=${HOME}/temp/${PACKAGE} install
	rm -rf ${TARBALL_TARGET}  && mkdir ${TARBALL_TARGET}
	cp -rf ${HOME}/temp/${PACKAGE}/${prefix}/* ${TARBALL_TARGET}
	tar -zcvf ./${PACKAGE}-${VERSION}-${build}.tar.gz ${TARBALL_TARGET}
	rm -rf ${TARBALL_TARGET}

PACKAGE_FULL_NAME="${PACKAGE}-${VERSION}-${host}"

dist-bin-path :
	rm -rf ${PACKAGE_FULL_NAME}
	make DESTDIR=`pwd`/${PACKAGE_FULL_NAME} install
	cd ${PACKAGE_FULL_NAME} && find . -type f -print > ../files.lst
	tar -C ${PACKAGE_FULL_NAME} -zcvf ${PACKAGE_FULL_NAME}.tar.gz `cat files.lst`
	rm -rf ${PACKAGE_FULL_NAME}
