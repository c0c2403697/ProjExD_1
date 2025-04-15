import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img= pg.image.load("fig/3.png")#練習2
    kk_img= pg.transform.flip(kk_img,True,False)#練習2後半
    gb_img= pg.transform.flip(bg_img,True,False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200 #練習6
       
        screen.blit(bg_img, [-x, 0])#練習6
        
        screen.blit(gb_img, [-x+1600, 0])#練習7
        screen.blit(bg_img, [-x+3200, 0])#練習9
        # screen.blit(kk_img, [300, 200])#練習4
        
        
        screen.blit(kk_img, kk_rct)
        key_lst = pg.key.get_pressed()
        
        # print(f"UP:{key_lst[pg.K_UP]}")
        # print(f"DOWN:{key_lst[pg.K_UP]}")
        # print(f"L:{key_lst[pg.K_LEFT]}")
        # print(f"R:{key_lst[pg.K_RIGHT]}")
        x=0
        y=0
        if key_lst[pg.K_UP]:
            y=-1
        if key_lst[pg.K_DOWN]:
            y=+1
        if key_lst[pg.K_LEFT]:
            x=-1
        if key_lst[pg.K_RIGHT]:
            x=+1
        else:
            x=-1
        kk_rct.move_ip(x, y)
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()