#-*- coding: utf-8 -*-

from application import Listener

import pygame


class Window(Listener):
	def __init__(self, *args, **kwargs):
		Listener.__init__(self, *args, **kwargs)

		pygame.display.set_mode((640, 480))

	def keydown(self, key):
		print "keydown :", key
		return False

