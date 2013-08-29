#-*- coding: utf-8 -*-

import pygame.mixer
import pygame

from pygame.locals import *


# pygame.init(), initialise tous les modules avec des valeurs par défaut
# dans notre cas on doit initialiser les modules avec des valeurs perso (en tout cas pour la musique)

# Pour initialiser les polices
pygame.font.init()

# Pour initialiser la musique
# 32000 étant la vitesse de la musique en hertz (récupérée grâce à audacity)
pygame.mixer.init(32000)

pygame.mixer.music.load("menu.ogg")
pygame.mixer.music.play(-1)

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

continuer = True

while continuer:
    for event in pygame.event.get():   
        if event.type == QUIT:     
            continuer = False
        elif event.type ==K_DOWN :
            pass
        elif event.type ==K_RIGHT :
            pass
        elif event.type ==K_UP :
            pass
        elif event.type ==K_LEFT :
            pass
        
