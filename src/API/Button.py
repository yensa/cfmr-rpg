#-*- coding: utf-8 -*-

'''
Created on 7 sept. 2013

@author: romain
'''

import pygame


class Button(object):
	def __init__(self, text, color, size, action, pos=(0, 0)):
		self.color = color
		self.rect = pygame.Rect(pos, size)
		self.text = text
		self.action = action

	def draw(self, screen):
		self.rect = pygame.draw.rect(screen, self.color, self.rect)
		screen.blit(self.text, pygame.Rect((self.rect.x, self.rect.y), 
										(self.text.get_width(), self.text.get_height())))

	def mousedown(self, button, pos):
		if self.rect.collidepoint(pos) and button == 1:
			self.action()

	def mouseup(self, button, pos):
		pass
