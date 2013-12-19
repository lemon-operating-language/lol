#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#lol bootstrap, © koo5

"""
current attack plan:
 create the ast nodes and an interpreter in python
 codify syntax and write an ide in lemon
"""



class Node(object):
	pass

class Rule(Node):
	def __init__(self, codes, time, name):
		self.codes = codes
		self.time = time
		self.name = name
	def run(self):
		self.codes.run()

class Import(Node):
	"an import of a python module"
	def __init__(self, name):
		self.name = name
	def run(self):
		self.module = __import__(self.name)

class Program(Node):
	"""the root of what the interpreter interprets"""

	def __init__(self, imports, codes):
		imps = ['__builtin__'] + imports
		self.imports = [Import(i) for i in imps]
		
	def get_rules(self):
		result = {'before':{}, 'after':{}, 'instead of':{}}
		for i in self.codes.items:
			if isinstance(i, Rule):
				result[i.time][i.name] = i
		return result

	def call_rule(self, time, name):
		if self.get_rules()[time].has_key(name):
			self.get_rules()[time][name].run()

	def run(self):
		"do eeet"
		self.call_rule(['before']['doing imports'])
		for i in self.imports.items:
			self.statements.run()

	

Rule("doing imports")



  
class Codes(List):


	def top_level_objects(self):
		"return objects defined in the first level only"
		"items of type Object in self.items"
		"Objects in self.items"
		for i in self.items:
			if isinstance(i, Object):
				yield i


	def run(self):
		for i in self.items:
			i.run()



class Import(Node):
	def __init__(self, name):
		self.name = name

	def run(self):
		self.loaded = __import__(name)

class Imports(Node):
	def __init__(self, items):
		self.items = items

	def run(self):
		


class PythonCall(Node):
	def __init__(self, module, name, arguments):
	    self.module = module
	    self.name = name
	    self.arguments = arguments


class PythonTuple(Node):
    def __init__(self, items):
        self.items = items


#Rule("importing X")


class Namespace(List):
	pass


syntax = {'program': {'codes':Codes, 'name':Text

program = Program(
	imports = List((List(items=['os', 'pygame']))
	codes = Codes(
		items = 
		[
			Namespace(items = List(
			[
				
		
		
			Import(
		
PythonCall(module = 'os', name = 'putenv', arguments = PythonTuple(["SDL_VIDEO_ALLOW_SCREENSAVER","1"]))


			Function(
				names = ["regenerate LICENSE file"],
				codes = Codes([
					Print(Text("boo!"))
				]
			)

done = False





contact = "irc: sirdancealot @ freenode"





def shit(gone_wrong):
	print(gone_wrong)
	print("\nfor support:",contact)





try:
	import pygame
	import pygame.gfxdraw
except Exception as e:
	shit("i need pygame. please install pygame. sudo apt-get install pygame / yum install pygame ....")
	raise(e)
	
	
	
	

try:
	import Pyro4
except Exception as e:
	shit("i need pyro4. please install. easy_install pyro4")
	raise(e)






Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')



class Screen():

	def __init__(s):

		pygame.init()
		pygame.display.set_caption("lol") #window title

		#sdl, which pygame is based on, has its own keyboard delay and repeat rate
		pygame.key.set_repeat(300,30) #first candidate for a settings block

		s.w = 640
		s.h = 480
		s.s = pygame.display.set_mode((s.w,s.h))

		s.f = pygame.font.SysFont('monospace', 18)
		s.fw = s.f.render(" ",False,(0,0,0)).get_rect().width
		s.fh = s.f.get_height()

		s.setroot([['text', "Hi!", pygame.Color(255,150,0), 0, 0]])
	
	def setroot(s,r):
		
		s.root=r


	def draw(s):
		s.s.fill((0,0,0))
		for i in s.root:
			try:
				if i[0] == 'text':
					s.s.blit(s.f.render(i[1], True, i[2]), (i[3], i[4]))
				if i[0] == 'rect':
					pygame.gfxdraw.rectangle(s.s, i[1], i[2])
			except Exception() as e:
				print i
				raise e

	
		pygame.display.update()
 






def send(x):
	print x




def process_event(e):

	send(e)
	if e.type == pygame.QUIT:
		exit()
	elif e.type == pygame.VIDEOEXPOSE:
		draw()



def main():
	scr = Screen()
	daemon = pyro4.Daemon()
	Pyro4.locateNS().register("lol.scr", daemon.register(scr))
	scr.draw()
	pygame.time.set_timer(pygame.USEREVENT, 1000)#40)#SIGINT timer
	while not done:
		try:
			process_event(pygame.event.wait())
		except KeyboardInterrupt() as e:
			pygame.display.iconify()
			raise e
		except Exception() as e:
			pass


main()

