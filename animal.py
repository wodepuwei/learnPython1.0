#!/usr/bin/python 
#__coding:utf-8__ 

class Animal(object):
	def run(self):
		print "Animal is running"

class Dog(Animal):
	def run(self):
		print "Dog is running"

class Cat(Animal):
	def run(self):
		print "Cat is running"

def run_twice(animal):
	animal.run() 
	animal.run()		


if __name__ == '__main__':
	a = Animal()
	d = Dog()
	c = Cat() 
	a.run()
	d.run()
	c.run()

	run_twice(Cat())
	run_twice(Animal())
