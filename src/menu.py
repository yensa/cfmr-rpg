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
from pygame.locals import *  # Cette ligne est-elle indispensable?
from pygame import font, Rect # Tu importe Rect, mais il ne te sert à rien


# Ce n'est pas comme ca que l'on fait, pour changer la fréquence du mixer pour la vitesse de la musique
pygame.mixer.init(44100)

# Tu charge et joue la musique avant de créer la fenêtre et l'application en elle-même 
# ce n'est pas là qu'il faut mettre ce code
pygame.mixer.music.load("/home/romain/Documents/Projects/workspace/cfmr-rpg/resources/musique/menu.ogg")
pygame.mixer.music.play(-1)


# Il n'est pas interdit de renommer la Scene en ce que tu veux
# exemple : class Menu(Scene):
# permettra d'avoir une Scene qui s'appelle Menu
class Test(Scene):
        def __init__(self, loader):
                # Dans le cas où tu renommerais Test en Menu cette ligne doit aussi changer en
                # super(Menu, self).__init__(loader)
                super(Test, self).__init__(loader)
                self._loader.preload_image(("icon", "icon.png"))
                self.add_listener(Image(self._loader.images.icon, (320, 240), CENTER))
                
                # Sache que mettre les fonctions que tu appellera avec les boutons directement dans
                # la méthode __init__ de la classe ce n'est pas bien, je ne l'ai fait que pour
                # l'exemple, à l'avenir place ces fonctions autre part
                
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
                
                # Il serait plus facile pour t'y retrouver de nommer les boutons correctement
                # car si jamais dans un mois pour une raison ou une autre tu veux revenir sur
                # le code source du menu, il serait préférable de voir les boutons nommé
                # bouton_jouer, bouton_option, bouton_charger, bouton_quitter
                # plutôt que button, button2, button3, button4
                frame.add_object(button)
                frame.add_object(button2)
                frame.add_object(button3)
                frame.add_object(button4)


# C'est ici que tu peux spécifier la fréquence du mixer (pour la vitesse de la musique)
# pour faire cela, il suffit de faire :
# app = Application("../resources", mixer_config={"frequency": 44100})
app = Application("../resources")

# Il n'y a désormais plus besoin de spécifier l'icone de la fenêtre, la fenêtre cherche désormais
# une image appellée icon.png toute seule et l'utilise comme icone autrement elle ne met pas d'icone personalisée
window = Window(app, config={"caption": "nom du jeux", "icon": "C:/Users/chris/Documents/GitHub/cfmr-rpg/resources/textures/icon.png"})

window.set_scene(Test)

app.run()
