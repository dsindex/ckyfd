#include <kyfd/decoder.h>
#include <kyfd/decoder-config.h>
#include <istream>
#include <ostream>
#include <streambuf>
#include <string>
#include "ckyfd.h"

using namespace kyfd;

struct membuf : std::streambuf
{
	membuf(char* begin, char* end) {
		this->setg(begin, begin, end);
	}
};

void* create_decoder(int argc, char** argv, void** config)
{
    DecoderConfig* conf = new DecoderConfig;
	conf->parseCommandLine(argc, argv);
    Decoder* decoder = new Decoder(*conf);
	*config = conf;
	return decoder;
}

void destroy_decoder(void* decoder, void* config)
{
	if( decoder ) delete decoder;
	if( config )  delete config;
}

static char *strlcat(char *dst, const char *src, int *limit)
{
	char    *p;

	if(!src)    return dst;
	if(!dst)    return NULL;

	p = dst;
	while(*p++);
	p--;

	while(*src != '\0' && *limit > 0) {
		*p++ = *src++;
		(*limit)--;
	}
	*p = '\0';
	return p;
}

int run_decoder(void* decoder, char* in, char* out, int out_size)
{
	// char* -> istream
	membuf sbuf(in, in + strlen(in));
	std::istream input(&sbuf);

	std::string line;
	while (std::getline(input, line)) {
		std::cout << "line: " << line << "\n";
	}

	/*
	std::ostream output;
	int ret = (Decoder*)decoder->decode(input, output);

	// ostream -> char*
	std::string str =  output.str();
	const char* chr = str.c_str();
	int limit = out_size;
	strlcat(out, chr, &limit);

	return ret;
	*/
	return 1;
}

