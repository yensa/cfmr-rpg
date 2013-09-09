#-*- coding: utf-8 -*-

'''
Created on 9 sept. 2013

@author: romain
'''

from API.Container import Container
from API.Widget import Widget


class VMenu(Widget, Container):
	def __init__(self, rect):
		Container.__init__(self, rect)
		Widget.__init__(self)
		
		self._lastYPos = -5

	def add_listener(self, l):
		l.rect.x, l.rect.y = 0, (self._lastYPos + 5) - self.rect.y * min(len(self._objects), 1)
		super(VMenu, self).add_listener(l)
		self._lastYPos = l.rect.bottom

	def draw(self, screen, rect=None):
		for w in self._objects:
			w.draw(screen)
