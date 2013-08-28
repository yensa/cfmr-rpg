#-*- coding: utf-8 -*-

import pygame.mixer
import pygame

from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))
fond = pygame.image.load("menu_teste.jpg").convert()
fenetre.blit(fond, (0,0))

a=pygame.font.SysFont("Arial",20,True,False)
lancement = a.render("lancer",1,(255,255,255))
fenetre.blit(lancement,(0,0))


pygame.display.flip()

