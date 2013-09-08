#-*- coding: utf-8 -*-

'''
Created on 7 sept. 2013

@author: romain
'''

import pygame

from Widget import Widget


"""
	@todo: mettre en place le système de placement des images
"""

CENTER = 1
RIGHT  = 2
LEFT   = 4
TOP    = 8
BOTTOM = 16

class Image(Widget):
	def __init__(self, image, pos = (0, 0), flags=TOP|LEFT):
		"""
			Cette classe représente une image affichable
			
			@param image: L'image qui doit être affichée
		"""
		self._image = image
		self._flags = flags

		size = (self._image.get_width(), self._image.get_height())
		self.rect = pygame.Rect(pos, size)
		if self._flags == CENTER:
			self.rect.x = self.rect.x - self.rect.width/2
			self.rect.y = self.rect.y - self.rect.height/2 

	def draw(self, screen, rect=None):
		if rect is None:
			rect = self.rect
		screen.blit(self._image, rect)
