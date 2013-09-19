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
from API.VMenu import VMenu


from pygame import font, Rect


class Test(Scene):
	def __init__(self, loader):
		super(Test, self).__init__(loader)

		self.add_listener(Image(self._loader.images.icon, (320, 240), CENTER))

		def dummy_action():
			print "Hello world"

		f = font.SysFont("Arial", 24).render("Hello world", True, (255, 255, 255))
		button = Button(f, (25, 90, 75), (f.get_width(), f.get_height()), dummy_action, (32, 32))

		def dummy_action2():
			print "dummy_2"

		f2 = font.SysFont("Arial", 24).render("Foobar", True, (255, 255, 255))

		button2 = Button(f2, (50, 45, 78), (f2.get_width(), f2.get_height()), dummy_action2, (32, 32))

		frame = VMenu(Rect(25, 25, 300, 300))
		self.add_listener(frame)

		frame.add_object(button)
		frame.add_object(button2)


app = Application("../resources")

<<<<<<< HEAD
window = Window(config={"caption": "Hello World", "icon": "C:/Users/chris/Documents/GitHub/cfmr-rpg/resources/textures/icon.png"})
=======
window = Window(app, config={"caption": "Hello World"})
>>>>>>> 2ac6e1ce3a254fb099fc644e5b3f144ec979692c
app.register_window(window)

window.set_scene(Test)

app.run()
