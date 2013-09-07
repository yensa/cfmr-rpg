#-*- coding: utf-8 -*-

'''
Created on 6 sept. 2013

@author: romain
'''

import pygame
from pygame import QUIT, KEYDOWN, KEYUP, MOUSEBUTTONUP, MOUSEBUTTONDOWN

from Loader import Loader


class Application(object):
	def __init__(self, resources_path="resources", max_fps=40, mixer_config=None):
		"""
			Initialise pygame et s'occuppe de la boucle principale, envoie aussi
			les événements à la fenêtre.

			@param resources_path: Le chemin vers le dossier contenant les resources
			@param max_fps: Limite le nombre de fps à ce nombre
			@param mixer_config: Dictionnaire contenant la configuration personnalisée du module mixer
		"""
		if not mixer_config is None:
			pygame.mixer.pre_init(**mixer_config)
		pygame.init()

		self._max_fps = max_fps
		self._clock = pygame.time.Clock()

		self._windows = []

		self._loader = Loader(resources_path)

	def register_window(self, win):
		"""
			Ajoute une fenêtre à l'application afin que celle-ci 
			lui envoie les événements.
			
			@param win: La fenêtre à ajouter
		"""
		win.set_loader(self._loader)
		self._windows.append(win)

	def run(self):
		"""
			Lance la boucle principale du jeu
		"""
		q = False
		while not q:
			for event in pygame.event.get():
				if event.type == QUIT:
					q = True
				elif event.type == KEYDOWN:
					for w in self._windows:
						w.keydown(event.key, event.mod)
				elif event.type == KEYUP:
					for w in self._windows:
						w.keyup(event.key, event.mod)
				elif event.type == MOUSEBUTTONDOWN:
					for w in self._windows:
						w.mousebuttondown(event.button, event.pos)
				elif event.type == MOUSEBUTTONUP:
					for w in self._windows:
						w.mousebuttonup(event.button, event.pos)

			for w in self._windows:
				w.draw()

			pygame.display.flip()

			self._clock.tick(self._max_fps)

		pygame.mixer.quit()
		pygame.font.quit()
		pygame.display.quit()
