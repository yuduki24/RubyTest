import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Hello, pygame world!!!!!")

# フォントの作成.
sysfont = pygame.font.SysFont(None, 80)

sysfont.set_bold(True)
sysfont.set_italic(True)
sysfont.set_underline(True)


# テキストを描画したSurfaceを作成.
# render( 描画したい文字列, Trueにすると文字がなめらか,
#         文字の色, 背景の色(所略すと透明))
hello1 = sysfont.render("Hello, world!1", False, (0, 0, 0,))
hello2 = sysfont.render("Hello, world!2", True, (0, 0, 0,))
hello3 = sysfont.render("Hello, world!3", True, (255, 0, 0), (255, 255, 0))

while True:
    screen.fill((0, 0, 255))

    # テキストを描画する.
    screen.blit(hello1, (20, 50))
    screen.blit(hello2, (20, 150))
    screen.blit(hello3, (20, 250))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
