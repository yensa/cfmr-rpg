#-*- coding: utf-8 -*-

import math

import pygame
from pygame.locals import *


class Circle:
	def __init__(self, surf, pos = (0, 0)):
		self.surf = surf
		self.pos = (pos[0] + 10, pos[1] + 10)

		self.color = (200, 150, 0)

		self.rect = pygame.draw.circle(self.surf, self.color, self.pos, 10)

		self.goal = self.pos

		self.speed = 5

		self.distance = 0

	@property
	def _deplacement(self):
		return (self.goal[0] - self.pos[0], self.goal[1] - self.pos[1])

	def set_goal(self, goal):
		self.goal = goal
		self.distance = math.sqrt(self._deplacement[0]**2 + self._deplacement[1]**2)

	def move(self):
		if self.distance > 0:
			dep = self._deplacement
			norm = (dep[0] / self.distance, dep[1] / self.distance)
			movement = (norm[0]*self.speed, norm[1]*self.speed)
			self.distance -= math.sqrt(movement[0]**2 + movement[1]**2)
			self.pos = (int(self.pos[0] + movement[0]), int(self.pos[1] + movement[1]))

	def draw(self):
		self.rect = pygame.draw.circle(self.surf, self.color, self.pos, 10)

if __name__ == "__main__":
	pygame.init()

	screen = pygame.display.set_mode((640, 480))

	clock = pygame.time.Clock()

	c = Circle(screen)

	while True:
		for event in pygame.event.get():
			if event.type == QUIT: exit()
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				c.set_goal(pygame.mouse.get_pos())

		c.move()

		screen.fill((0, 0, 0))
		c.draw()
		pygame.display.flip()
		clock.tick(40)

