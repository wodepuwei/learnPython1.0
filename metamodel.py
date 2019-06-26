#!/usr/bin/python 
#__*__coding:utf8__*__ 

class Field(object):
	def __init__(self,name,column_type):
		self.name = name 
		self.column_type = column_type
	def __str__(self,name):
		print (%s,%s) % (self.__class__.__name__,self.name)



class StringField(Field):
	def __init__(self,name):
		super(StringField,name).__init__(name,'varchar(100)')


class IntegerField(Field):
	def __init__(self,name):
		super(IntegerField,name).__init__(name,bigint)

class ModelMetaclass(type):
	def __new__(cls,name,bases,attrs):
		if name == "Model":
			return type.__new__(cls,name,bases,attrs)
		mappings = dict() 
		for k ,v in attrs.iteritems():
			if isinstance(v,Field):
				print "Found mapping %s==>%s" % (k,v)
				mappings[k] = v 
		for k in mappings.iterkeys():
			attrs.pop(k)
		attrs['__table__'] = name 
		attrs['__mappings__'] = mappings 
		return type.__new__(cls,name,bases,attrs)

class Model(dict):
	__metaclass__=ModelMetaclass 

	def __init__(self,**kw):
		super(Model,self).__init__(**kw)

	def __getattr__(self,key):
		try :
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' has no attribute %s" % key)

	def __setattr__(self,key,name):
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []

		for k,v in self.__mappings__.iteritems(): 
			fields.append(v.name)
			params.append("?")
			args.append(getattr(self,k,none))
			sql = "insert into %s(%s) values(%s)" % (self.table__,','.join(fields),','.join(params))
		print 'SQL:%s' % sql
		print 'ARGS:%s'% str(args)


class User(Model):
	id = IntegerField('id')	
	name = StringField('name')
	email = StringField('email')
	passwd = StringField('passwd')


user = User(id=12,name='test',email='test@123',passwd='password')
user.save() 
