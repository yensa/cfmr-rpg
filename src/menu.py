#-*- coding: utf-8 -*-

'''
Created on 19 sept. 2013

@author: chris
'''
from API.Application import Application
from API.Window import Window
from API.Scene import Scene
from API.Image import Image, CENTER
from API.Button import Button
from API.VMenu import VMenu
import pygame.mixer
from pygame.locals import *
from pygame import font, Rect

pygame.mixer.init(44100)

pygame.mixer.music.load("C:/Users/chris/Documents/GitHub/cfmr-rpg/resources/musique/menu.ogg")
pygame.mixer.music.play(-1)

class Test(Scene):
        def __init__(self, loader):
                super(Test, self).__init__(loader)
                self._loader.preload_image(("icon", "icon.png"))
                self.add_listener(Image(self._loader.images.icon, (320, 240), CENTER))
                
                def jouer():
                        print "jouer"
                f = font.SysFont("Arial", 24).render("jouer", True, (255, 255, 255))
                button = Button(f, (25, 90, 75), (f.get_width(), f.get_height()), jouer, (32, 32))
                
                def option():
                        print "option"
                f2 = font.SysFont("Arial", 24).render("option", True, (255, 255, 255))
                button2 = Button(f2, (50, 45, 78), (f2.get_width(), f2.get_height()), option, (32, 32))
                
                def charger():
                        print "option"
                f3 = font.SysFont("Arial", 24).render("charger", True, (255, 255, 255))
                button3 = Button(f3, (50, 45, 78), (f3.get_width(), f3.get_height()), charger, (32, 32))
                
                def quitter():
                        print "quitter"
                f4 = font.SysFont("Arial", 24).render("quitter", True, (255, 255, 255))
                button4 = Button(f4, (50, 45, 78), (f4.get_width(), f4.get_height()), quitter, (32, 32))
                
                frame = VMenu(Rect(25, 25, 300, 300))
                self.add_listener(frame)
                frame.add_object(button)
                frame.add_object(button2)
                frame.add_object(button3)
                frame.add_object(button4)


app = Application("../resources")

window = Window(config={"caption": "nom du jeux", "icon": "C:/Users/chris/Documents/GitHub/cfmr-rpg/resources/textures/icon.png"})
app.register_window(window)

window.set_scene(Test)

app.run()
