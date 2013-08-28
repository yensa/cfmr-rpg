#-*- coding: utf-8 -*-

import pygame.mixer
import pygame

from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))
fond = pygame.image.load("menu_teste.jpg").convert()
fenetre.blit(fond, (0,0))

a=pygame.font.SysFont("Arial",16,True,False)
lancement = a.render("lancer",1,(255,255,255))
fenetre.blit(lancement,(0,0))

b=pygame.font.SysFont("Arial",16,True,False)
lancement = b.render("option",1,(255,255,255))
fenetre.blit(lancement,(0,450))

c=pygame.font.SysFont("Arial",16,True,False)
lancement = c.render("charger",1,(255,255,255))
fenetre.blit(lancement,(550,450))

d=pygame.font.SysFont("Arial",16,True,False)
lancement = d.render("charger",1,(255,255,255))
fenetre.blit(lancement,(550,30))


pygame.display.flip()

while True :
    option=input(">")
    if option == ("o") :
        exit()

