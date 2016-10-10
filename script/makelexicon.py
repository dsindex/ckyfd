#!/usr/bin/env python
#-*- coding: utf8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from optparse import OptionParser
import math

# global variable
VERBOSE = 0
EPS = '<eps>'  # epsilon
WB  = '<w>'    # word boundary

if __name__ == '__main__':

	parser = OptionParser()
	parser.add_option("--verbose", action="store_const", const=1, dest="verbose", help="verbose mode")
	(options, args) = parser.parse_args()

	# build word vocab
	word_vocab = {}
	freq_sum = 0
	while 1:
		try:
			line = sys.stdin.readline()
		except KeyboardInterrupt:
			break
		if not line:
			break
		line = line.strip()
		for word in line.split() :
			# make lower
			key = word.lower()
			if key in word_vocab :
				word_vocab[key] += 1
			else :
				word_vocab[key] = 1
			freq_sum += 1

	# build lexicon
	'''
	0 1696954 s swords 1
	1696954 1696955 w <eps>
	1696955 1696956 o <eps>
	1696956 1696957 r <eps>
	1696957 1696958 d <eps>
	1696958 1696959 s <eps>
	1696959 0 <w> <eps>
	'''
	start_state = 0
	state = 1
	for key, freq in word_vocab.iteritems() :
		try : key_u = key.decode('utf-8')
		except : continue
		size = len(key_u)
		idx = 0
		while idx < size :
			ch_u = key_u[idx]
			ch = ch_u.encode('utf-8')
			if idx == 0 :
				# compute minus log probability
				prob = 0
				if freq_sum != 0 : prob = freq / float(freq_sum)
				logprob = -math.log(prob)
				tp = [start_state, state, ch, key, logprob]
				print ' '.join([str(e) for e in tp])
			else :
				tp = [state, state+1, ch, EPS]
				print ' '.join([str(e) for e in tp])
				state += 1
			idx += 1
		tp = [state, start_state, WB, EPS]
		print ' '.join([str(e) for e in tp])
		state += 1

	print '0 0 <s> <s>'
	print '0'

	
