#include <istream>
#include <ostream>
#include <streambuf>
#include <string>
#include "decoder.h"
#include "decoder-config.h"
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
	Decoder* dec = static_cast<Decoder*>(decoder);
	DecoderConfig* conf = static_cast<DecoderConfig*>(config);

	if( dec ) delete dec;
	if( conf )  delete conf;
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
	Decoder* dec = static_cast<Decoder*>(decoder);

	// char* -> istream
	membuf sbuf(in, in + strlen(in));
	std::istream input(&sbuf);

	/*
	std::string line;
	while (std::getline(input, line)) {
		std::cout << "line: " << line << "\n";
	}
	*/

	std::ostringstream output;
	int ret = dec->decode(input, output);
	if( !ret ) return _CKYFD_FAILURE;

	// ostringstream to char*
	std::string str =  output.str();
	const char* chr = str.c_str();
	int limit = out_size;
	*out = '\0';
	strlcat(out, chr, &limit);
	if( limit == 0 ) return _CKYFD_BUFOVER;

	return _CKYFD_SUCCESS;
}

