#ifndef CKYFD_H__
#define CKYFD_H__

#ifdef __cplusplus
extern "C" {
#endif

void* create_decoder(char* config_file, void** config, char* nbest, char* oformat);

void  destroy_decoder(void* decoder, void* config);

int   run_decoder(void* decoder, char* in, char* out, int out_size);

typedef enum {
	_CKYFD_FAILURE = 0,
	_CKYFD_SUCCESS = 1,
	_CKYFD_BUFOVER = -1,
} ckyfd_ret_t;

#ifdef __cplusplus
}
#endif

#endif
