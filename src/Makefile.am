
INCLUDES  = 

OPTS = #-DDEBUG

lib_LTLIBRARIES = libckyfd.la libckyfd_static.la

libckyfd_la_SOURCES = ckyfd.c 
libckyfd_la_LDFLAGS = -avoid-version -no-undefined
libckyfd_la_CFLAGS = -g -Wall -fPIC ${OPTS}

libckyfd_static_la_SOURCES = ckyfd.c 
libckyfd_static_la_LDFLAGS = -static -avoid-version -no-undefined
libckyfd_static_la_CFLAGS = -g -Wall -fPIC ${OPTS}

bin_PROGRAMS = test_ckyfd

test_ckyfd_SOURCES    = test_ckyfd.c
test_ckyfd_LDFLAGS    = -static -avoid-version -no-undefined
test_ckyfd_LDADD      = -lckyfd -lkyfd -lpthread -ldl
test_ckyfd_CFLAGS     = -g -Wall ${OPTS}
