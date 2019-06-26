# --*-- coding:utf-8 --*--

import math
import functools

def dd(x):
	flag = True
	n = math.sqrt(x)
	n = int(n)
	for i in range(2,n+1):
		if x % i == 0:
			flag = False 
	return flag

def compare(x,y):
	x = x.upper()
	y = y.upper() 

	if x < y :
		return 1 
	elif x == y:
		return 0
	else: 
		return -1 

def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print '%s %s:' % (text,func.__name__)
            return func(*args,**kw)
     	return wrapper     
	return decorator

def log(text,func):
	def wrapper(*args,**kw):
		print '%s %s:' % (text,func.__name)
		return func(*args,**kw)
	return wrapper 


import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


#filter函数的比较
#ll=filter(dd,range(1,101))
#print ll

#忽略大小写，倒叙排序
ll = sorted(['Abc','bcd','cdg'],compare)
print ll