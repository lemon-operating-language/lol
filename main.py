#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#lol bootstrap, © koo5





class Node(object):
	pass




class Program(Node):
	"""the root of what the interpreter interprets"""

	def run(self):
		"do eeet"
		self.statements.run()

Rule("doing imports")



  
class Codes(Node):


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
	def __init__(self, items):
		self.items = items

	def run(self):
		


class PythonCall(Node):
	def __init__(self, module, name, 
	


#Rule("importing X")


program = Program(
	imports = List(Import("pygame")),
	codes = Codes(
		items = [
			Import(List(items=['os', 'pygame']))
		
os.putenv("SDL_VIDEO_ALLOW_SCREENSAVER","1")


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

