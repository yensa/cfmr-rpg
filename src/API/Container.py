#-*- coding: utf-8 -*-

'''
Created on 9 sept. 2013

@author: romain
'''

from Events import EventDispatcher


class Container(EventDispatcher):
	def __init__(self):
		self.add_object = self.add_listener

	def draw(self, *args):
		self.dispatch("draw", *args)
	
	def keydown(self, *args):
		self.dispatch("keydown", *args)
	
	def keyup(self, *args):
		self.dispatch("keyup", *args)
	
	def mousedown(self, *args):
		self.dispatch("mousedown", *args)
	
	def mouseup(self, *args):
		self.dispatch("mouseup", *args)
