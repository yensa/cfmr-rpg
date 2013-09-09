#-*- coding: utf-8 -*-

'''
Created on 7 sept. 2013

@author: romain
'''

from Events import EventDispatcher


class Scene(EventDispatcher):
	def __init__(self, loader):
		super(Scene, self).__init__()
		self._loader = loader
