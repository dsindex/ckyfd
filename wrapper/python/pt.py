#!/usr/bin/env python
#-*- coding: utf8 -*-

import os
import sys

def post_tagging(string, analyzed) :
	'''
	ex) 0 ||| 나 /np 는 /pt <space> 학 교 /nc 에 서 /pa <space> 공 부 /na 하 /xv _ㅂ 니 다 /ef . /sf ||| 47.8457 \t ...
	'''
	outs = []
	if not analyzed : return outs
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
		outs.append([decoded, score])

	return outs

