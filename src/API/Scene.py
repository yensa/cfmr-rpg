#-*- coding: utf-8 -*-

'''
Created on 7 sept. 2013

@author: romain
'''

class Scene(object):
	_drawables = []
	_mousables = []
	_keyables  = []

	def __init__(self, loader):
		self._loader = loader

	def draw(self, screen):
		for d in self._drawables:
			d.draw(screen)

	def keydown(self, key, mod):
		for k in self._keyables:
			k.keydown(key, mod)

	def keyup(self, key, mod):
		for k in self._keyables:
			k.keyup(key, mod)

	def mousedown(self, button, pos):
		for m in self._mousables:
			m.mousedown(button, pos)

	def mouseup(self, button, pos):
		for m in self._mousables:
			m.mouseup(button, pos)
