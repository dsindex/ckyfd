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
BS  = u'<b>'   # begin sentence
EPS = u'<eps>' # epsilon
WB  = u'<w>'   # word boundary

if __name__ == '__main__':

	parser = OptionParser()
	parser.add_option("--verbose", action="store_const", const=1, dest="verbose", help="verbose mode")
	(options, args) = parser.parse_args()

	# build word vocab
	word_vocab = {}
	while 1:
		try:
			line = sys.stdin.readline()
		except KeyboardInterrupt:
			break
		if not line:
			break
		line = line.strip()
		for word in line.split() :
			# make lower, decode to unicode
			try : key = word.lower().decode('utf-8')
			except : continue
			if key in word_vocab :
				word_vocab[key] += 1
			else :
				word_vocab[key] = 1

	# compute pair, symbol count
	'''
	예) <b> 다 음 검 색 <w>
	[(<b>, 다), (다, 음), (음, 검), (검, 색), (색, <w>)]
	[<b>, 다, 음, 검, 색]
	'''
	symbols = {}
	total_symbol_count = 0
	pairs = {}
	total_pair_count = 0
	for key, freq in word_vocab.iteritems() :
		key_list = [BS] + list(key) + [WB]
		size = len(key_list)
		idx = 0
		while idx < size :
			ch = key_list[idx]
			if idx + 1 < size :
				nch = key_list[idx+1]
				pair = ch + u'-' + nch
				if pair in pairs :
					pairs[pair] += freq
				else :
					pairs[pair] = freq
				total_pair_count += freq
				if ch in symbols :
					symbols[ch] += freq
				else :
					symbols[ch] = freq
				total_symbol_count += freq
			idx += 1
		
	# build autospacer
	'''
	for every word in word_vocab, 
	  예) <b> 다 음 검 색 <w>
	  0 1 다 다       p(<b>, 다) / p(<b>)
	  1 2 음 음       p(다, 음)  / p(다)
	  2 3 검 검       p(음, 검)  / p(음)
	  3 4 색 색       p(검, 색)  / p(검)
	  4 5 <eps> <w>   p(색, <w>) / p(색)
	  5 0 <eps> <eps>
	'''
	start_state = 0
	state = 1
	for key, freq in word_vocab.iteritems() :
		key_list = [BS] + list(key) + [WB]
		size = len(key_list)
		idx = 0
		while idx < size :
			if idx == size - 1 : # last WB
				break
			ch = key_list[idx]
			if idx + 1 < size :
				nch = key_list[idx+1]
				pair = ch + u'-' + nch
				# compute minus log probability
				prob = 0
				pair_count = 0
				symbol_count = 0
				if pair in pairs : pair_count = pairs[pair]
				if ch in symbols : symbol_count = symbols[ch]
				if symbol_count != 0 : prob = pair_count / float(symbol_count)
				logprob = -math.log(prob)
			if idx == 0 :
				from_ch = nch
				to_ch = nch
				tp = [start_state, state, from_ch, to_ch, logprob]
				print ' '.join([str(e).encode('utf-8') for e in tp])
			else :
				from_ch = nch
				to_ch = nch
				if nch == WB : from_ch = EPS
				tp = [state, state+1, from_ch, to_ch, logprob]
				print ' '.join([str(e).encode('utf-8') for e in tp])
				state += 1
			idx += 1
		tp = [state, start_state, EPS, EPS]
		print ' '.join([str(e).encode('utf-8') for e in tp])
		state += 1

	print '0 0 <s> <s>'
	print '0'

	
