#!/usr/bin/env python
#-*- coding: utf8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from optparse import OptionParser

# global variable
VERBOSE = 0
EPS = '<eps>'
SP  = '<s>'
UNK = '<unk>'
WB  = '<w>'

if __name__ == '__main__':

	parser = OptionParser()
	parser.add_option("--verbose", action="store_const", const=1, dest="verbose", help="verbose mode")
	parser.add_option("--input", action="store_const", const=1, dest="input", help="input")
	parser.add_option("--output", action="store_const", const=1, dest="output", help="input")
	(options, args) = parser.parse_args()

	symbols = {}
	symbols[EPS] = 0
	symbols[SP] = 1
	symbols[UNK] = 2
	symbols[WB] = 3
	idx = 4
	while 1:
		try:
			line = sys.stdin.readline()
		except KeyboardInterrupt:
			break
		if not line:
			break
		line = line.strip()
		if not line : continue
		tokens = line.split()
		size = len(tokens)
		if size < 4 : continue
		isymbol = tokens[2]
		osymbol = tokens[3]
		symbol = isymbol
		if options.input :
			symbol = isymbol
		if options.output :
			symbol = osymbol
		if symbol not in symbols :
			symbols[symbol] = idx
			idx += 1

	symbols = sorted(symbols.iteritems(), key=lambda x : x[1])
	for symbol, idx in symbols :
		print symbol + ' ' + str(idx)
