#-*- coding: utf-8 -*-

'''
Created on 7 sept. 2013

@author: romain
'''

import pygame

from Widget import Widget


class Button(Widget):
	def __init__(self, text, color, size, action, pos=(0, 0)):
		self.color = color
		self.rect = pygame.Rect(pos, size)
		self.text = text
		self.action = action

	def draw(self, screen, rect=None):
		self.rect = pygame.draw.rect(screen, self.color, self.rect)
		if rect is None:
			rect = self.rect
		t = self.text.subsurface(pygame.Rect((0, 0), self.rect.size))
		screen.blit(t, self.rect)

	def mousedown(self, button, pos):
		if self.rect.collidepoint(pos) and button == 1:
			self.action()
