#!/usr/bin/env python
#-*- coding: utf8 -*-

import os
import sys
import re

WORD_BW = '<space>'

SP = re.compile('''[\s]+''')

def norm(s) :
	return SP.sub(' ', s).strip()

def encode(string) :
	'''
	string : 나는 학교에서 공부합니다.
	return : 나 는 <space> 학 교 에 서 <space> 공 부 합 니 다 .
	'''
	if not string : return None
	try : string_u = string.decode('utf-8')
	except Exception, e :
		sys.stderr.write(str(e) + '\n')
		return None
	encoded = ' '.join([WORD_BW if e == ' ' else e for e in string_u])
	return encoded.encode('utf-8')

def to_mlist(encoded, decoded) :
	'''
    encoded : 나 는 <space> 학 교 에 서 <space> 공 부 합 니 다 .
	decoded : 나 /np 는 /pt <space> 학 교 /nc 에 서 /pa <space> 공 부 /na 하 /xv _ㅂ 니 다 /ef . /sf
	'''
	eoj_list = encoded.replace(WORD_BW, '\t').split('\t')
	eoj_list = [eoj.replace(' ','') for eoj in eoj_list]
	mseq_list = decoded.replace(WORD_BW, '\t').split('\t')
	for mseq in mseq_list : # '나 /np 는 /pt'
		mseq = mseq.strip()

	
def tagging(kyfd, string) :
	'''
	string  : 나는 학교에서 공부합니다.
	'''
	outs = []
	if not kyfd or not string : return outs

	# replace multiple space to single space
	string = norm(string)

	encoded = encode(string)
	if not encoded : return outs

	# analyzed : 0 ||| 나 /np 는 /pt <space> 학 교 /nc 에 서 /pa <space> 공 부 /na 하 /xv _ㅂ 니 다 /ef . /sf ||| 47.8457 \t ...
	analyzed = kyfd.decode(encoded)

	results = analyzed.strip().split('\t')
	nbest = len(results)
	for result in results :
		result = result.strip().replace('|||','\t')
		tokens = [token.strip() for token in result.split('\t')]
		size = len(tokens)
		decoded = None
		score = 0
		if size == 1 : # decoded output only
			decoded = tokens[0]
		if size == 2 : # seq, decoded output | decoded output, score
			if tokens[0].isdigit() :
				decoded = tokens[1]
			else :
			 	decoded = tokens[0]
			 	score = tokens[1]
		if size == 3 : # seq, decoded output, score
			decoded = tokens[1]
			score = tokens[2]
		mlist = to_mlist(encoded, decoded)
		outs.append([mlist, score])

	return outs
