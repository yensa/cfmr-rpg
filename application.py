#-*- coding: utf-8 -*-

import pygame

from sys import exit


class EventDispatcher:
	listeners = []

	def addListener(self, l):
		self.listeners.append(l)

	def dispatch(self, event, *args):
		for l in self.listeners:
			try:
				func = eval("l.%s"%event)
				r = func(args)
			except:
				continue
			if not r: break
	
	__iadd__ = addListener
	__call__ = dispatch

DISPATCHER = EventDispatcher()

class Listener:
	def __init__(self):
		global DISPATCHER

		DISPATCHER += self

class Application:
	def __init__(self, max_fps = 40):
		pygame.display.init()
		pygame.font.init()
		pygame.mixer.init()

		global DISPATCHER

		self.dispatcher = DISPATCHER

		self.max_fps = max_fps

		self.clock = pygame.time.Clock()
	
	def run(self):
		quit = False
		while !quit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.display.quit()
					pygame.font.quit()
					pygame.mixer.quit()
					quit = True
				elif event.type == pygame.KEYDOWN:
					self.dispatcher("keydown", event.key)
		self.dispatcher("draw")
		pygame.display.flip()
		self.clock.tick(self.max_fps)

	__call__ = run

