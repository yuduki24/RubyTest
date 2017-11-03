import pygame
from pygame.locals import *
import sys
 
SCR_WIDTH,SCR_HEIGHT = 640,480
 
pygame.init()
screen = pygame.display.set_mode((SCR_WIDTH,SCR_HEIGHT))
pygame.display.set_caption(u"画像の移動と跳ね返り処理")
 
img = pygame.image.load("img/my_python.png").convert()
colorkey = img.get_at((0, 0))
img.set_colorkey(colorkey, RLEACCEL)
img_rect = img.get_rect()

img2 = pygame.image.load("img/my_python.png").convert()
colorkey2 = img2.get_at((0, 0))
img2.set_colorkey(colorkey2, RLEACCEL)
img_rect2 = img2.get_rect()
img_rect2.x = SCR_WIDTH - (img2.get_width() / 2)
img_rect2.y = SCR_HEIGHT - (img2.get_height() / 2)

vx = vy = 500  # 1秒間の移動ピクセル
vx2 = vy2 = 120  # 1秒間の移動ピクセル

clock = pygame.time.Clock()
 
while True:
    time_passed = clock.tick(60)  # 60fpsで前回からの経過時間を返す（ミリ秒）
    time_passed_seconds = time_passed / 1000.0  # ミリ秒を秒に変換
    
    # 画像の移動
    img_rect.x += vx * time_passed_seconds
    img_rect.y += vy * time_passed_seconds
    img_rect2.x += vx2 * time_passed_seconds
    img_rect2.y += vy2 * time_passed_seconds
    # 跳ね返り処理
    if img_rect.left < 0 or img_rect.right > SCR_WIDTH:
        vx = -vx
    if img_rect.top < 0 or img_rect.bottom > SCR_HEIGHT:
        vy = -vy
    if img_rect2.left < 0 or img_rect2.right > SCR_WIDTH:
        vx2 = -vx2
    if img_rect2.top < 0 or img_rect2.bottom > SCR_HEIGHT:
        vy2 = -vy2
    
    screen.fill((100,24,255))
    screen.blit(img, img_rect)
    screen.blit(img2, img_rect2)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE: sys.exit()