#-*- coding: utf-8 -*-

# Attention ce test requiert l'installation de la bibliothèque BeautifulSoup
# Pour l'installer, il faut lancer easy_install BeautifulSoup en ligne de commande sous windows
# (sudo) pip install BeautifulSoup sous linux

from BeautifulSoup import BeautifulSoup as soup

from pygame import Rect, image, Surface, SRCALPHA


class Tileset:
	def __init__(self, nom, tilesize, img, fgid=1):
		self.nom = nom
		self.tilesize = tilesize
		self.image = image.load(img).convert_alpha()
		self.fgid = fgid

		self.tiles = []

		for i in xrange(self.image.get_height() / self.tilesize[1]):
			for j in xrange(self.image.get_width() / self.tilesize[0]):
				self.tiles.append(self.image.subsurface(Rect(j*self.tilesize[0], i*self.tilesize[1], *self.tilesize)))
	
	def __getitem__(self, idx):
		return self.tiles[idx]

class Map:
	def __init__(self, filename):
		self.doc = soup(open(filename))

		self.info = self.doc.find("map")

		t = self.doc.find("tileset")
		nom = t.get("name", "")
		fgid = int(t.get("firstgid", 1))
		twidth  = int(t.get("tilewidth", 0))
		theight = int(t.get("tileheight", 0))
		img = t.findChild("image").get("source", "")
		self.tileset = Tileset(nom, (twidth, theight), img, fgid)

		self.nw, self.nh = int(self.info["width"]), int(self.info["height"])
		self.tw, self.th = int(self.info["tilewidth"]), int(self.info["tileheight"])
		self.size = (self.nw * self.tw, self.nh * self.th)

		self.layers = [[self.tileset[max(int(tile["gid"])-1, 0)] for tile in l.findChildren("tile")] for l in self.doc.findAll("layer")]
	
	def getImage(self):
		m = Surface(self.size, SRCALPHA).convert()
		for l in self.layers:
			for idx, t in enumerate(l):
				m.blit(t, Rect((idx%self.nw)*self.tw, (idx/self.nw)*self.th, self.tw, self.th))
		return m

if __name__ == "__main__":
	import pygame
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	m = Map("village.tmx")
	mapimg = m.getImage()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: exit()
		screen.fill((0, 0, 0))
		screen.blit(mapimg, (0, 0))
		pygame.display.flip()

