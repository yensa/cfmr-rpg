#-*- coding: utf-8 -*-

'''
Created on 6 sept. 2013

@author: romain
'''

from API.Application import Application
from API.Window import Window
from API.Scene import Scene
from API.Image import Image, CENTER
from API.Button import Button

from pygame import font


class Test(Scene):
	def __init__(self, loader):
		super(Test, self).__init__(loader)
		
		self._loader.preload_image(("icon", "icon.png"))
		self._drawables.append(Image(self._loader.images.icon, (320, 240), CENTER))
		def dummy_action():
			print "Hello world"
		f = font.SysFont("Arial", 24).render("Hello world", True, (255, 255, 255))
		button = Button(f, (25, 90, 75), (f.get_width(), f.get_height()), dummy_action, (32, 32))
		self._drawables.append(button)
		self._mousables.append(button)


app = Application("../resources")

window = Window(config={"caption": "Hello World", "icon": "/home/romain/Documents/Projects/workspace/cfmr-rpg/resources/textures/icon.png"})
app.register_window(window)

window.set_scene(Test)

app.run()
