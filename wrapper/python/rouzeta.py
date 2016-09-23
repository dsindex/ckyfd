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
	return :
	  elist : ['나는','학교에서','공부합니다.']
	  mlist : [{'morph':'나는','tag':'/np','ltag':None, 'eidx':0, 'midx':0}, { .. }, ...]
	'''
	elist = encoded.replace(WORD_BW, '\t').split('\t')
	elist = [eoj.replace(' ','') for eoj in elist]

	mlist = []
	mseq_list = decoded.replace(WORD_BW, '\t').split('\t')
	eidx = 0
	midx = 0
	for mseq in mseq_list : # '공 부 /na 하 /xv _ㅂ 니 다 /ef . /sf'
		mseq = mseq.strip().split()
		mseq_size = len(mseq)
		bucket = []
		idx = 0
		while idx < mseq_size :
			m = mseq[idx]
			msize = len(m)
			if msize >= 2 and m[0] == '/' : # tag
				mtype = 'tag'
			else :                          # syll
				mtype = 'syll'
			if mtype == 'tag' :
				morph = ''.join(bucket)
				# --------------------------------------------------
				# check if next is also tag type, ex) '/irrs /vb'
				t_range = 0
				nidx = idx+1
				while nidx < mseq_size :
					n = mseq[nidx]
					nsize = len(n)
					if nsize >= 2 and n[0] == '/' : t_range += 1
					else : break
					nidx += 1
				# --------------------------------------------------
				if t_range >= 1 :
					tag = mseq[idx + t_range]             # last tag
					ltag = ''.join(mseq[idx:idx+t_range]) # additional tag
				else :
					tag = m
					ltag = None
				mlist.append({'morph':morph, 'tag':tag, 'ltag':ltag, 'eidx':eidx, 'midx':midx})
				midx += 1

				bucket = []
				idx += t_range
			else : # syll
				bucket.append(m)
			idx += 1	
		eidx += 1

	return mlist, elist
	
def tagging(kyfd, string, verbose=False) :
	'''
	string  : 나는 학교에서 공부합니다.
	'''
	outs = []
	if not kyfd or not string : return outs

	# replace multiple space to single space
	string = norm(string)

	encoded = encode(string)
	if not encoded : return outs

	analyzed = kyfd.decode(encoded)

	if verbose :
		print encoded
		print analyzed

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
		mlist, elist = to_mlist(encoded, decoded)
		outs.append([mlist, elist, score])

	return outs

