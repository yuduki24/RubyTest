import pygame
from pygame.locals import *
import sys
 
SCR_RECT = Rect(0, 0, 640, 480)
 
class MySprite(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, vx, vy):
        # デフォルトグループをセット
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey, RLEACCEL)
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = Rect(x, y, width, height)
        self.vx = vx
        self.vy = vy
        
        
    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        # 壁にぶつかったら跳ね返る
        if self.rect.left < 0 or self.rect.right > SCR_RECT.width:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > SCR_RECT.height:
            self.vy = -self.vy
        # 画面からはみ出ないようにする
        self.rect = self.rect.clamp(SCR_RECT)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
 
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption(u"スプライトの使い方")
    
    # スプライトグループを作成してスプライトクラスに割り当て
    group = pygame.sprite.RenderUpdates()
    MySprite.containers = group
    
    # スプライトを作成
    python1 = MySprite("img/my_python.png", 0, 0, 2, 2)
    python2 = MySprite("img/my_python.png", 10, 10, 5, 5)
    python3 = MySprite("img/my_python.png", 320, 240, -2, 3)
    python4 = MySprite("img/my_python.png", 200, 200, -20, 15)
    python5 = MySprite("img/my_python.png", 0, 150, -2, 10)
    python6 = MySprite("img/my_python.png", 150, 0, -6, 3)
    
    clock = pygame.time.Clock()
    
    # 背景の作成と描画（背景は最初に1回だけ描画）
    background = pygame.Surface(SCR_RECT.size)
    background.fill((0,0,255))
    screen.blit(background, (0,0))
    pygame.display.update()

    while True:
        clock.tick(60)  # 60fps
        # 背景の全体描画はしない!
        # screen上のSpriteを背景で消去
        group.clear(screen, background)

        # スプライトグループを更新
        group.update()
        print (python1.rect)

        # スプライトグループを描画
        # RenderUpdateのdraw()は変化があった部分の矩形（dirty rect）を返す
        dirty_rects = group.draw(screen)
        print (dirty_rects)
        # updateにdirty rectを渡すとその部分だけ更新するので効率よい
        pygame.display.update(dirty_rects)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
 
if __name__ == "__main__":
    main()