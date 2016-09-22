#include "ckyfd.h"
   
#include <errno.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdarg.h>

#define m_error(format, ...)  fprintf(stderr, "[%s:%s:%d] [error] " format "\n", __FILE__, __FUNCTION__, __LINE__, ##__VA_ARGS__)
#define m_info(format, ...)   fprintf(stderr, "[%s:%s:%d] [info] "  format "\n", __FILE__, __FUNCTION__, __LINE__, ##__VA_ARGS__)
#define m_debug(format, ...)  fprintf(stderr, "[%s:%s:%d] [debug] " format "\n", __FILE__, __FUNCTION__, __LINE__, ##__VA_ARGS__)

