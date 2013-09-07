#-*- coding: utf-8 -*-

'''
Created on 7 sept. 2013

@author: romain
'''

import pygame
import weakref
import os


class ResourceController(object):
	"""
		Cet objet permet de charger les resources seulement quand on
		en a besoin
	"""
	def __init__(self, loader):
		"""
			@param loader: La fonction permettant de charger les resource
		"""
		self.__dict__.update(dict(
								names = {},
								cache = weakref.WeakValueDictionary(),
								loader = loader
								))
	
	def __setattr__(self, name, value):
		self.names[name] = value

	def __setitem__(self, name, value):
		self.names[name] = value

	def __getattr__(self, name):
		try:
			res = self.cache[name]
		except KeyError:
			res = self.loader(self.names[name])
			self.cache[name] = res
		return res

	def __getitem__(self, name):
		try:
			res = self.cache[name]
		except KeyError:
			res = self.loader(self.names[name])
			self.cache[name] = res
		return res

class ImageController(ResourceController):
	def __init__(self):
		super(ImageController, self).__init__(self._load)
	
	def _load(self, image):
		"""
			Cette fonction permet de charger une image
		"""
		return pygame.image.load(image).convert_alpha()
	
class SoundController(ResourceController):
	def __init__(self):
		super(SoundController, self).__init__(self._load)

	def _load(self, sound):
		"""
			Cette fonction permet de charger un son
		"""
		return pygame.mixer.Sound(sound)


class Loader(object):
	def __init__(self, path):
		"""
			Le Loader est une classe permettant de gérer tous les types de
			resources
			
			@param path: Le chemin vers le dossier contenant les resources
		"""
		self._path = path

		self.images = ImageController()
		self.sounds = SoundController()

	def preload_image(self, image):
		"""
			Permet de precharger une image
			
			@param image: Un tuple contenant deux entrées, la première représente le nom de la resource, 
						  la seconde, le chemin vers cette resource
		"""
		name, path = image
		self.images[name] = os.path.join(self._path, "textures", path)

	def preload_sound(self, sound):
		"""
			Permet de precharger un son
			
			@param sound: Un tuple contenant deux entrées, la première représente le nom de la resource,
						  la seconde, le chemin vers cette resource
		"""
		name, path = sound
		self.sounds[name] = os.path.join(self._path, "sounds", path)
