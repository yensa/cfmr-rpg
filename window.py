#-*- coding: utf-8 -*-

from application import Listener

import pygame


class Window(Listener):
	def __init__(self, *args, **kwargs):
		Listener.__init__(self, *args, **kwargs)

		self.screen = pygame.display.set_mode((640, 480))

	def keydown(self, key):
		print "keydown :", key
		return False

	def draw(self):
		self.screen.fill((0, 0, 0))
		return True

