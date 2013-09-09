#-*- coding: utf-8 -*-

'''
Created on 7 sept. 2013

@author: romain
'''

from Events import EventDispatcher


class Scene(EventDispatcher):
	def __init__(self, loader):
		self._loader = loader
