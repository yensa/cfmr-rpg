#-*- coding: utf-8 -*-

'''
Created on 9 sept. 2013

@author: romain
'''

def safe_call(o, m, *args):
	def dummy(*args, **kwargs):
		pass
	func = getattr(o, m, dummy)
	return func(*args)

class EventDispatcher(object):
	def __init__(self):
		self._objects = []

	def dispatch(self, method, *args):
		for o in self._objects:
			safe_call(o, method, *args)

	def add_listener(self, l):
		self._objects.append(l)