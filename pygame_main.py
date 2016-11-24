import pygame
from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((640, 480))
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0, 0))
pygame.display.flip()
continuer = 1

#Boucle infinie
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0