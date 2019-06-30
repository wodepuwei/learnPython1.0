#!/usr/bin/python 
#__*__coding:utf8__*__

import os 

print "Process(%s) is starting..." % os.getpid()
pid = os.fork() 
if pid == 0 :
	print 'I was a child process(%s) of process(%s)' % (os.getpid(),os.getppid())
else: 
	print 'I am creating a new thread(%s)' % os.getpid()
