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
		# remove space, make lower
		try : line_u = line.replace(' ', '').lower().decode('utf-8')
		except : continue
		print ' '.join([ch_u.encode('utf-8') for ch_u in line_u])
