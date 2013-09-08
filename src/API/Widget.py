#-*- coding: utf-8 -*-

'''
Created on 8 sept. 2013

@author: romain
'''

import pygame


class Widget(object):
	rect = pygame.Rect((0, 0), (0, 0))

	def __init__(self):
		"""
			Cette classe définit un widget par défaut depuis lequel les autres
			sont créé
		"""
		pass

	def draw(self, screen, rect=None):
		pass

	def draw_at_pos(self, screen, pos, rect=None):
		if rect is None:
			self.rect.x, self.rect.y = pos
			rect = self.rect
		self.draw(screen, rect)

	def move(self, dep):
		self.rect.move_ip(dep)
