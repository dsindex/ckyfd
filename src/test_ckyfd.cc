#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include "ckyfd.h"

#define LINE_SIZE	10240

int main(int argc, char** argv)
{
	int  size;
	char string[LINE_SIZE+1];
	int  buf_size = LINE_SIZE*10;
	char buf[buf_size+1];
	int  cnt_line;

	void* config;
	void* decoder;
	struct timeval t1,t2;
	int ret;
	char* nbest = "1";
	char* oformat = "text"; // text | score | component

	if(argc == 1) {
		fprintf(stderr, "Usage : %s config.xml\n", argv[0]);
		return 1;
	}

	fprintf(stderr, "--------------------------\n");
	fprintf(stderr, "-- Started Kyfd Decoder --\n");
	fprintf(stderr, "--------------------------\n");


	gettimeofday(&t1, NULL);

	// load the configuration and initialize the decoder
	decoder = create_decoder(argv[1], &config);
    
	fprintf(stderr, "Loaded configuration, initializing decoder...\n");

	gettimeofday(&t2, NULL);
	fprintf(stderr,"elapsed time = %lf sec\n",((t2.tv_sec - t1.tv_sec)*1000000 + t2.tv_usec - t1.tv_usec)/(double)1000000);

	cnt_line = 0;
	while(fgets(string, LINE_SIZE, stdin) != NULL) {
		size = strlen(string);
		if(string[size-1] == '\n'){
			string[size-1] = '\0';
			--size;
		}
		if(size > 1 && string[size-1] == '\r'){
			string[size-1] = '\0';
			--size;
		}
		if(string[0] == '\0')
			continue;

		ret = run_decoder(decoder, string, buf, buf_size, config, nbest, oformat);
		switch( ret ) {
			case _CKYFD_SUCCESS :
				fprintf(stdout, "%s\n", buf);
				break;
			case _CKYFD_FAILURE :
				break;
			case _CKYFD_BUFOVER :
				break;
			default :
				break;
		}
		
		cnt_line++;
		if( cnt_line % 1000 == 0 ) {
			fprintf(stderr,"cnt_line = %d\n", cnt_line);
		}
	}

	gettimeofday(&t2, NULL);
	fprintf(stderr,"elapsed time = %lf sec\n",((t2.tv_sec - t1.tv_sec)*1000000 + t2.tv_usec - t1.tv_usec)/(double)1000000);

	destroy_decoder(decoder, config);
   
	return 0;
}
