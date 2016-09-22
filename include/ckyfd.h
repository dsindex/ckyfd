#ifndef CKYFD_H__
#define CKYFD_H__

#ifdef __cplusplus
extern "C" {
#endif

void* create_decoder(int argc, char** argv, void** config);

void  destroy_decoder(void* decoder, void* config);

int   run_decoder(void* decoder, char* in, char* out, int out_size);

#ifdef __cplusplus
}
#endif

#endif
