#-*- coding: utf-8 -*-

'''
Created on 9 sept. 2013

@author: romain
'''

from Events import EventDispatcher


class Container(EventDispatcher):	
	def __init__(self, rect):
		super(Container, self).__init__()
		self.add_object = self.add_listener
		
		self.rect = rect

	def add_listener(self, l):
		super(Container, self).add_listener(l)
		l.rect.x, l.rect.y = l.rect.x + self.rect.x, l.rect.y + self.rect.y
		if not self.rect.contains(l.rect):
			l.rect.width = l.rect.width - max(l.rect.right - self.rect.right, 0)
			l.rect.height = l.rect.height - max(l.rect.bottom - self.rect.bottom, 0)

	def draw(self, screen, rect=None):
		for o in self._objects:
			o.draw(screen)

	def keydown(self, *args):
		self.dispatch("keydown", *args)
	
	def keyup(self, *args):
		self.dispatch("keyup", *args)
	
	def mousedown(self, *args):
		self.dispatch("mousedown", *args)
	
	def mouseup(self, *args):
		self.dispatch("mouseup", *args)
