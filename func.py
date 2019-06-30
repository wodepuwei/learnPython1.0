#!/usr/bin/python 
#__*__coding:utf8__*__

"__todo__"=="search1函数的完善"

import os
def search(s):
	for f in os.listdir('./'):
		if os.path.isfile(f):
			fpath = os.path.join(os.path.abspath('.'),f)
			#if s in os.path.splitext(fpath)[0]:
			if s in os.path.split(fpath)[1]:
				print fpath
def search1(s,dirpath='./'):
	if not os.path.isdir(dirpath):
		raise dirError
	
	for f in os.listdir(dirpath):
		if os.path.isfile(f):
			fpath = os.path.join(os.path.abspath('.'),f)
			if s in os.path.splitext(fpath)[0]:
				print fpath


if __name__=="__main__":
	search('hell')
	print "======================="
	search('animal')
