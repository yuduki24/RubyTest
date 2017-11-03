import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (116, 42)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(u"イメージの描画")

# イメージを用意.
myPythonImg1 = pygame.image.load("img/my_python.png").convert()
myPythonImg2 = pygame.image.load("img/my_python.png").convert_alpha()
myPythonImg3 = pygame.image.load("img/my_python.png").convert()
colorkey = myPythonImg3.get_at((10,15))  # (10, 15)の色を透明色に.
myPythonImg3.set_colorkey(colorkey, RLEACCEL)

while True:
    screen.blit(myPythonImg1, (5,5))
    screen.blit(myPythonImg2, (42,5))
    screen.blit(myPythonImg3, (79,5))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()