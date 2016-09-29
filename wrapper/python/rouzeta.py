#!/usr/bin/env python
#-*- coding: utf8 -*-

import os
import sys
import re

WORD_BW = '<space>'
SP = re.compile('''[\s]+''')
ROUZETA_SEJONG_TAG_MAP = {
	'ac':'MAJ', # 접속부사	ac	conjunctive adverb	또는, 그러나, ...
	'ad':'MAG', # 부사	ad	adverb	매우, 과연, ...
	'ai':'MAG', # 의문부사	ai	interrogative adverb	어디, 언제, ...
	'am':'MAG', # 지시부사	am	demonstrative adverb	여기, 저기, ...
	'di':'MM',  # 의문관형사	di	interrogative adnoun	어느, 몇, ...
	'dm':'MM',  # 지시관형사	dm	demonstrative adnoun	이, 그, 저, ...
	'dn':'MM',  # 관형사	dn	adnoun	새, 헌, ...
	'du':'MM',  # 수관형사	du	numeral adnoun	한, 두, ...
	'ec':'EC',  # 연결어미	ec	conjunctive ending	~며, ~고, ...
	'ed':'ETM', # 관형사형전성어미	ed	adnominal ending	~는, ~ㄹ, ...
	'ef':'EF',  # 어말어미	ef	final ending	~다, ~는다, ...
	'en':'ETN', # 명사형전성어미	en	nominal ending	~ㅁ, ~기 (두 개뿐)
	'ep':'EP',  # 선어말어미	ep	prefinal ending	~았, ~겠, ...
	'ex':'EC',  # 보조적연결어미	ex	auxiliary ending	~아, ~고, ...
	'it':'IC',  # 감탄사	it	interjection	앗, 거참, ...
	'na':'NNG', # 동작성보통명사	na	active common noun	가맹, 가공, ...
	'nc':'NNG', # 보통명사	nc	common noun	가관, 가극, ...
	'nd':'NNB', # 의존명사	nd	dependent noun	겨를, 곳, ...
	'ni':'NP',  # 의문대명사	ni	interrogative pronoun	누구, 무엇, ...
	'nm':'NP',  # 지시대명사	nm	demonstrative pronoun	이, 이것, ...
	'nn':'NR',  # 수사	nn	numeral	공, 다섯, ...
	'np':'NP',  # 인칭대명사	np	personal pronoun	나, 너, ...
	'nr':'NNP', # 고유명사	nr	proper noun	YWCA, 홍길동, ...
	'ns':'NNG', # 상태성보통명사	ns	stative common noun	간결, 간절, ...
	'nu':'NNB', # 단위성의존명사	nu	unit dependent noun	그루, 군데, ...
	'nb':'SN',  # 숫자	nb	number	1, 2, ...
	'pa':'JKB', # 부사격조사	pa	number	~에, ~에서, ...
	'pc':'JC',  # 접속조사	pc	conjunctive particle	~나, ~와, ...
	'pd':'JKG', # 관형격조사	pd	adnominal particle	~의 (한 개)
	'po':'JKO', # 목적격조사	po	adnominal particle	~을, ~를, ~ㄹ
	'pp':'VCP', # 서술격조사	pp	predicative particle	~이~ (한 개) !! '사람이다'
	'ps':'JKS', # 주격조사	ps	subjective particle	~이, ~가, ...
	'pt':'JX',  # 주제격조사	pt	thematic particle	~은, ~는, (두 개)
	'pv':'JKV', # 호격조사	pv	vocative particle	~야, ~여, ~아, ...
	'px':'JX',  # 보조사	px	auxiliary particle	~ㄴ, ~만, ~치고, ...
	'pq':'JKQ', # 인용격조사	pq	quotative particle	~고, ~라고, ~라, ...
	'pm':'JKC', # 보격조사	pm	complementary particle	~이, ~가 (두 개)
	'vb':'VV',  # 동사	vb	verb	감추~, 같~, ...
	'vi':'VA',  # 의문형용사	vi	interrogative adjective	어떠하~, 어떻~, ...
	'vj':'VA',  # 형용사	vj	adjective	가깝~, 괜찮~, ...
	'vx':'VX',  # 보조용언	vx	auxiliary verb	나~, 두~, ...
	'vn':'VCN', # 부정지정사	vn	auxiliary verb	아니~ (하나)
	'xa':'EC',  # 부사파생접미사	xa	adverb derivational suffix	~게, ~이, ... !! '없이,없게'
	'xj':'XSA', # 형용사파생접미사	xj	adjective derivational suffix	같~, 높~, 답~, ...
	'xv':'XSV', # 동사파생접미사	xv	verb derivational suffix	~하, ~시키, ...
	'xn':'XSN', # 명사접미사	xn	noun suffix	~군, ~꾼, ...
	'sc':'SP',  # 쉼표	sc	comma	:, ,, ...
	'se':'SP',  # 줄임표	se	ellipsis	…
	'sf':'SF',  # 마침표	sf	sentence period	!, ., ?
	'sl':'SP',  # 여는따옴표	sl	left parenthesis	(, <, [, ...
	'sr':'SP',  # 닫는따옴표	sr	right parenthesis	), >, ], ...
	'sd':'SP',  # 이음표	sd	dash	-, ...
	'su':'SL',  # 단위	su	unit	Kg, Km, bps, ...
	'sy':'SW',  # 화폐단위	sy	currency	$, ￦, ...
	'so':'SP',  # 기타기호	so	other symbols	α, φ, ...
	'nh':'SH',  # 한자	nh	chinese characters	丁, 七, 万, ...
	'ne':'SL',  # 영어	ne	english words	computer, ...
}

def norm(s) :
	return SP.sub(' ', s).strip()

def encode(string) :
	'''
	string : '나는 학교에서 공부합니다.'
	return : '나 는 <space> 학 교 에 서 <space> 공 부 합 니 다 .'
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
    encoded : '나 는 <space> 학 교 에 서 <space> 공 부 합 니 다 .'
	decoded : '나 /np 는 /pt <space> 학 교 /nc 에 서 /pa <space> 공 부 /na 하 /xv _ㅂ 니 다 /ef . /sf'
	return  :
	  - elist : ['나는','학교에서','공부합니다.']
	  - mlist : [{'morph':'나','tag':'np','ltag':None, 'stag':'NP', 'eidx':0, 'midx':0, ...}, { .. }, ...]
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
				tag = tag[1:]
				if ltag : ltag = ltag[1:]
				stag = tag
				if tag in ROUZETA_SEJONG_TAG_MAP : stag = ROUZETA_SEJONG_TAG_MAP[tag]
				mlist.append({'morph':morph, 'tag':tag, 'ltag':ltag, 'stag':stag, 'eidx':eidx, 'midx':midx})
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
	string  : '나는 학교에서 공부합니다.'
	return  : list of [mlist, elist, score] 
	  - elist : ['나는','학교에서','공부합니다.']
	  - mlist : [{'morph':'나','tag':'np','ltag':None, 'stag':'NP', 'eidx':0, 'midx':0, ...}, { .. }, ...]
	  - score : sum of weights through FST path, -1 if undefined
	'''
	outs = []
	if not kyfd or not string : return outs

	# replace multiple space to single space
	string = norm(string)

	encoded = encode(string)
	if not encoded : return outs

	# ex) seq ||| decoded output ||| score
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
		score = -1
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

