
ckyfd_home  = ${top_builddir}
ckyfd_inc   = ${ckyfd_home}/include
ckyfd_lib   = ${ckyfd_home}/src

python_inc = ${pythoninc}

AM_CFLAGS  = -I${ckyfd_inc} -I${python_inc}

lib_LTLIBRARIES = libpckyfd.la

include_HEADERS = pckyfd.h

libpckyfd_la_SOURCES = pckyfd.c
libpckyfd_la_LDFLAGS = -avoid-version -fPIC -undefined dynamic_lookup
libpckyfd_la_LIBADD  = -lckyfd_static -L${ckyfd_lib}
libpckyfd_la_CFLAGS  = -g -Wall -fno-strict-aliasing

dist_bin_SCRIPTS = test.py


