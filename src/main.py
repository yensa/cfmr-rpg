#-*- coding: utf-8 -*-

'''
Created on 6 sept. 2013

@author: romain
'''

from API.Application import Application
from API.Window import Window
from API.Scene import Scene
from API.Image import Image, CENTER


class Test(Scene):
	def __init__(self, loader):
		super(Test, self).__init__(loader)
		
		self._loader.preload_image(("icon", "icon.png"))
		self._drawables.append(Image(self._loader.images.icon, (320, 240), CENTER))


app = Application("../resources")

window = Window(config={"caption": "Hello World", "icon": "C:/Users/chris/Documents/GitHub/cfmr-rpg/resources/textures/icon.png"})
app.register_window(window)

window.set_scene(Test)

app.run()
