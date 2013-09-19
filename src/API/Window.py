#-*- coding: utf-8 -*-

'''
Created on 6 sept. 2013

@author: romain
'''

import pygame


class Window(object):
	_currentScene = None

	_loader = None

	def __init__(self, application, config={}):
		"""
			Crée une fenêtre pygame.

			@param config: Dictionnaire contenant la configuration de la fenêtre
		"""
		self.app = application
		self.app.register_window(self)

		if config.has_key("caption"): caption = config.pop("caption")
		else: caption = "pygame API Window"

		size = config.get('size', (640, 480))
		flags = config.get('flags', pygame.DOUBLEBUF | pygame.HWSURFACE)
		depth = config.get('depth', 32)

		self._screen = pygame.display.set_mode(size, flags, depth)

		pygame.display.set_caption(caption)
		icon = self.app.get_icon()
		if not icon is None:
			pygame.display.set_icon(icon)

	def set_scene(self, scene):
		"""
			Change la scene actuelle
			
			@param scene: La nouvelle scene
		"""
		self._currentScene = scene(self._loader)

	def set_loader(self, loader):
		"""
			Permet de changer le loader de cette fenêtre
			
			@param loader: Le nouveau loader
		"""
		self._loader = loader

	def draw(self):
		"""
			Dessine la fenêtre et tout ce qu'elle contient
		"""
		self._screen.fill((0, 0, 0))
		
		self._currentScene.dispatch("draw", self._screen)

	def keydown(self, key, mod):
		"""
			Lance l'événement keydown
			
			@param key: La touche qui vient d'être enfoncée
			@param mod: L'éventuelle touche modificatrice enfoncée
		"""
		self._currentScene.dispatch("keydown", key, mod)

	def keyup(self, key, mod):
		"""
			Lance l'événement keyup
			
			@param key: La touche qui vient d'être relevée
			@param mod: L'éventuelle touche modificatrice enfoncée
		"""
		self._currentScene.dispatch("keyup", key, mod)

	def mousebuttondown(self, button, pos):
		"""
			Lance l'événement mousebuttondown
			
			@param button: Le bouton de la souris enfoncé
			@param pos: La position du curseur de la souris
		"""
		self._currentScene.dispatch("mousedown", button, pos)

	def mousebuttonup(self, button, pos):
		"""
			Lance l'événement mousebuttonup
			
			@param button: Le bouton de la souris relevé
			@param pos: La position du curseur de la souris
		"""
		self._currentScene.dispatch("mouseup", button, pos)
