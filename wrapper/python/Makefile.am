
kyfd_home  = ${kyfd}
kyfd_inc   = ${kyfd_home}/include
kyfd_lib   = ${kyfd_home}/lib

ckyfd_home  = ${top_builddir}
ckyfd_inc   = ${ckyfd_home}/include
ckyfd_lib   = ${ckyfd_home}/src

python_inc = ${pythoninc}

AM_CPPFLAGS  = -I${kyfd_inc} -I${ckyfd_inc} -I${python_inc}

lib_LTLIBRARIES = libpkyfd.la

include_HEADERS = pkyfd.h

libpkyfd_la_SOURCES = pkyfd.cc
libpkyfd_la_LDFLAGS = -avoid-version -fPIC -undefined dynamic_lookup
libpkyfd_la_LIBADD  = -lckyfd -lkyfd -L${kyfd_lib} -L${ckyfd_lib}
libpkyfd_la_CFLAGS  = -g -Wall -fno-strict-aliasing

dist_bin_SCRIPTS = test.py test_rouzeta.py rouzeta.py


