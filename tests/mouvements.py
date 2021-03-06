#-*- coding: utf-8 -*-

import pygame
from pygame import locals

from itertools import cycle

from maploader import Map


#TODO: Améliorer le code, ajouter une carte comme fond

#TODO: Mettre les classes créée pour cet exemple dans des modules et les améliorer

class ImageGrid:
	def __init__(self, surf, col, row):
		w = surf.get_width() / col
		h = surf.get_height() / row

		self.imgs = []

		for i in range(row):
			for j in range(col):
				self.imgs.append(surf.subsurface(pygame.Rect(j*w, i*h, w, h)))
	
	def __getitem__(self, n):
		return self.imgs[n]


class Sprite(pygame.sprite.Sprite):
	def __init__(self, img, *args, **kwargs):
		super(Sprite, self).__init__(*args, **kwargs)

		self.img = img
		self.pos = (0, 0)
		self.width = self.img.get_width()
		self.height = self.img.get_height()

	def set_position(self, x, y):
		self.pos = (x, y)
	
	def getImg(self):
		return (self.img, pygame.Rect(self.pos, (self.width, self.height)))


class Animation(Sprite):
	def __init__(self, img, t=1):
		self.imgs = img
		self.anim = cycle(self.imgs)
		Sprite.__init__(self, self.imgs[0])
		self.t = t
		self._ticks = 0

	def tick(self):
		self._ticks += 1
		if self._ticks%self.t == 0:
			self.img = self.anim.next()

	def reset(self):
		self.img = self.imgs[0]

class Perso:
	def __init__(self, filename):
		self.img = pygame.image.load(filename).convert_alpha()

		self.pos = (0, 0)
		self.movement = (0, 0)
		self.speed = 1.5
		self.moving = False

		self.h = self.img.get_height() / 4
		self.w = self.img.get_width()

		self.up    = Animation(ImageGrid(self.img.subsurface(pygame.Rect(0, 0, self.w, self.h)), 4, 1), 4)
		self.down  = Animation(ImageGrid(self.img.subsurface(pygame.Rect(0, 3*self.h, self.w, self.h)), 4, 1), 4)
		self.right = Animation(ImageGrid(self.img.subsurface(pygame.Rect(0, self.h, self.w, self.h)), 4, 1), 4)
		self.left  = Animation(ImageGrid(self.img.subsurface(pygame.Rect(0, 2*self.h, self.w, self.h)), 4, 1), 4)

		self.sprite = self.down

	@property
	def rect(self):
		return pygame.Rect(self.pos, (self.w / 4, self.h))

	def set(self, pos):
		self.moving = True
		if pos == 0:
			self.sprite = self.up
			self.sprite.set_position(*self.pos)
			self.movement = (self.movement[0], self.speed)
		elif pos == 1:
			self.sprite = self.down
			self.sprite.set_position(*self.pos)
			self.movement = (self.movement[0], -self.speed)
		elif pos == 2:
			self.sprite = self.right
			self.sprite.set_position(*self.pos)
			self.movement = (-self.speed, self.movement[1])
		elif pos == 3:
			self.sprite = self.left
			self.sprite.set_position(*self.pos)
			self.movement = (self.speed, self.movement[1])
	
	def move(self, bnds):
		if self.moving:
			self.pos = (self.pos[0]+self.movement[0], self.pos[1]+self.movement[1])
			self.sprite.set_position(*self.pos)
			if not bnds.contains(self.rect):
				x, y = self.pos
				if self.pos[0] < 0: x = 0
				elif self.pos[0] > (bnds.width - self.rect.width): x = (bnds.width - self.rect.width)

				if self.pos[1] < 0: y = 0
				elif self.pos[1] > (bnds.height - self.rect.height): y = (bnds.height - self.rect.height)
				self.sprite.set_position(x, y)
				self.pos = (x, y)
			self.sprite.tick()
	
	def endMovement(self, p):
		self.sprite.reset()
		if p in [0, 1]:
			self.movement = (self.movement[0], 0)
		elif p in [2, 3]:
			self.movement = (0, self.movement[1])
		if self.movement == (0, 0):
			self.moving = False

pygame.init()

screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

p = Perso("perso.png")
carte = Map("village.tmx").getImage()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: exit()
		elif event.type == pygame.KEYDOWN:
			k = event.key
			if k == pygame.K_LEFT:
				p.set(2)
			elif k == pygame.K_RIGHT:
				p.set(3)
			elif k == pygame.K_DOWN:
				p.set(0)
			elif k == pygame.K_UP:
				p.set(1)
		elif event.type == pygame.KEYUP:
			k = event.key
			if k == pygame.K_LEFT:
				p.endMovement(2)
			elif k == pygame.K_RIGHT:
				p.endMovement(3)
			elif k == pygame.K_DOWN:
				p.endMovement(0)
			elif k == pygame.K_UP:
				p.endMovement(1)
	screen.fill((0, 0, 0))
	screen.blit(carte, (0, 0))
	p.move(pygame.Rect(0, 0, screen.get_width(), screen.get_height()))
	screen.blit(*p.sprite.getImg())
	clock.tick(40)
	pygame.display.flip()

