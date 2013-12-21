#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#lol bootstrap, © koo5



import importlib
import pyke
from pyke import knowledge_engine
e = knowledge_engine.engine(__file__)



def ass(verb, *args):
	e.assert_('lemon', verb, args)

class Node(object):
	def view(self):
		query(
	def as(self, verb, arg):
	
NodeView(Node):
	def __init__(self, type, view):
		self.type = type
		self.view = view
	def ass(self):
		sa('is_view_of_node', self.type)
class String():
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
		print self.to_text()
	
	def to_text(self):
		r=""
		for i in self.items:
			r+=i.to_text() + "\n"
		return r


class Codes(List):
	def __init__(self, items):
		self.items = items
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

class Section(Node):

	def __init__(self, name, codes):
		self.name = name
		self.codes = codes
		
	def to_text(self):
		return "section "+self.name+":\n" + self.codes.to_text()

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



class PythonCall(Node):
	def __init__(self, module, name, arguments):
	    self.module = module
	    self.name = name
	    self.arguments = arguments


class PythonTuple(Node):
    def __init__(self, items):
        self.items = items

class Rule(Node):
	def __init__(self, time, action, codes):
		self.time = time
		self.action = action

class ActionParameter(Node):
	def __init__(self, name, type):
		self.name = name
		self.type = type

class ActionSignature(Node):
	def __init__(self, items):
		self.items = items

class ActionDefinition(Node):
	def __init__(self, signature):
		self.signature = signature

class ItemResolver(Node):
	def __init__(self, clues):
		self.clues = clues

	def resolve(self):
		print "resolving", self.clues
		items = program.codes.items
		print items
		if self.clues.has_key("type"):
			print "by type", self.clues['type']
			items = filter(lambda i: isinstance(i, self.clues['type']), items)
		
		print "resolved to", items
		if len(items) == 1:
			return items
		else:
			raise "resolution failed"


program = Program(
	name = "x", codes = 
Codes(
[
		Section("builtin", codes = Codes(
		[
			ActionDefinition(ActionSignature(["importing", ActionParameter(name = 'module', type = String)]))
			
			
		])),
		ClassDefinition('pygame window', Object),
		ObjectDeclaration('window', 'pygame window'),
		Import('os'),
		Rule('before', 
			ItemResolver({'list':ItemResolver({'type':Section, 'name':'builtin'}), 'index':0, 'type':ActionDefinition, 'key':"signature"}), Codes([])),
#		PythonCall(module = 'os', name = 'putenv', arguments = PythonTuple(["SDL_VIDEO_ALLOW_SCREENSAVER","1"])),
		Import('pygame')
]))



#program.ass()


print ItemResolver({'type':Section, 'name':'builtin'}).resolve()


e.get_kb('a').dump_universal_facts()
e.get_kb('a').dump_specific_facts()






print program.to_text()



a view of node can be verbose

dump(program):=
	has_attribute %V, verbose 
	is_view_of_node %V, program 

++++++++++++++++++++++








