#-*- coding: utf-8 -*-

'''
Created on 8 sept. 2013

@author: romain
'''

from Widget import Widget
from Container import Container


class Frame(Widget, Container):
	def __init__(self, rect):
		Container.__init__(self, rect)
		Widget.__init__(self)

	def draw(self, screen, rect=None):
		for w in self._objects:
			w.draw(screen)
