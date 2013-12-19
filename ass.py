#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#lol bootstrap, © koo5

import importlib

import pyke
from pyke import knowledge_engine
e = knowledge_engine.engine(__file__)
#e.activate('a')


"""
knowledge base
top down:
	goal: the gui
	editor window is a kind of pygame window
	pygame window is a kind of thing..
"""

def ass(verb, *args):
	e.assert_('a', verb, args)

class Node(object):
	pass

class Object(object):
	@classmethod
	def to_text(cls):
		return "Object"

class Assertion(Node):
	def ass(self):
		if self.object != None:
			ass(self.verb, self.subject, self.object)
		else:
			e.assert_('a', self.verb, (self.subject, ))

#Assertion(verb = 

class List(Node):
	def __init__(self, items):
		self.items = items
		for i in self.items:
			i.parent = self
	
	def to_text(self):
		r=""
		for i in self.items:
			r+=i.to_text() + "\n"
		return r


class Codes(List):
	def ass(self):
		for i in self.items:
			i.ass()


class ClassDefinition(Node):
	def __init__(self, name, superclass):
		self.name = name
		self.superclass = superclass
	def ass(self):
		e.assert_('a', 'is class', (self.name, self.superclass))
	def to_text(self):
		return self.name + " is a subclass of " + self.superclass.to_text()
	

class ObjectDeclaration(Node):
	def __init__(self, name, type):
		self.name = name
		self.type = type
	def ass(self):
		e.assert_('a', 'is an object of type', (self, self.type))
	def to_text(self):
		return self.name + " is an object of type " + self.type


class Import(Node):
	def __init__(self, name):
		self.name = name
		self.loaded = None
	
	def to_text(self):
		return "import the python module "+self.name +(str(self.loaded) if self.loaded else "")
		
	def run(self):
		self.loaded = importlib.import_module(self.name)
	
	def ass(self):
		ass('is a python module import', self)

class Program(Node):

	def __init__(self, name, codes):
		self.name = name
		self.codes = codes
		self.memory = dict()

	def to_text(self):
		return self.name+"\n"+self.codes.to_text()

	def run(self):
		self.ass()
		e.activate('a')

	def ass(self):
		ass('is a kind of', self, Node)
		self.codes.ass()


program = Program(
	"x", Codes(
	[
		ClassDefinition('pygame window', Object),
		ObjectDeclaration('window', 'pygame window'),
		Import('pygame')
	]
	))


program.ass()

e.get_kb('a').dump_universal_facts()
e.get_kb('a').dump_specific_facts()

print program.to_text()

