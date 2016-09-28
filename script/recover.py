#!/usr/bin/env python
#-*- coding: utf8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from optparse import OptionParser

# global variable
VERBOSE = 0

if __name__ == '__main__':

	parser = OptionParser()
	parser.add_option("--verbose", action="store_const", const=1, dest="verbose", help="verbose mode")
	(options, args) = parser.parse_args()

	while 1:
		try:
			line = sys.stdin.readline()
		except KeyboardInterrupt:
			break
		if not line:
			break
		line = line.strip()
		if not line : continue
		line = line.replace(' ','').replace('<w>',' ')
		print line
