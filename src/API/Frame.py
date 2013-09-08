#-*- coding: utf-8 -*-

'''
Created on 8 sept. 2013

@author: romain
'''

import pygame

from Widget import Widget


class Frame(Widget):
	def __init__(self, rect):
		self.rect = rect
		self._widgets = []

	def add_widget(self, d):
		self._widgets.append(d)

	def draw(self, screen, rect=None):
		for w in self._widgets:
			nrect = w.rect.move(self.rect.topleft)
			if self.rect.contains(nrect):
				w.draw_at_pos(screen, nrect)
			else:
				nw = max(nrect.width - (self.rect.x + self.rect.width), 0)
				nh = max(nrect.height - (self.rect.y + self.rect.height), 0)
				nrect = pygame.Rect(nrect.topleft, (nrect.width - nw, nrect.height - nh))
				w.draw_at_pos(screen, nrect)
