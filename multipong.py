import pygame as pg
from pygame.locals import (K_LEFT, K_RIGHT)

VINDU_BREDDE = 546
VINDU_HOYDE = 720
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
pg.display.set_caption("Breakout")
lyseblaa = (171, 195, 251)
morkeblaa = (31, 48, 159, 255)
gronn = (122, 255, 137, 255)
rosa = (255, 86, 120, 255)

farge = (4, 4, 4)

FPS = 60

blokknr = 0

class Plattform:
    def __init__(self):
        self.bredde = (VINDU_BREDDE/4)
        self.hoyde = (VINDU_HOYDE/20)
        self.x = ((VINDU_BREDDE/2) - (self.bredde/2))
        self.y = (VINDU_HOYDE/1.15)
        self.rect = pg.Rect(self.x, self.y, self.bredde, self.hoyde)
        self.fart = 10

    def tegn(self):
        pg.draw.rect(vindu, lyseblaa, self.rect)

    def flytt(self, taster):
        if taster[K_LEFT] and self.rect.x - self.fart > -7: #Kollisjon venstre side
            self.rect.x -= self.fart
        if taster[K_RIGHT]  and self.rect.x + self.fart + self.bredde < VINDU_BREDDE + 7: #Kollisjon høyre side
            self.rect.x += self.fart
        
firkant_liste = []
firkantX = []
firkantY = []

class Firkant:
    def __init__(self):
        self.radius = 12
        self.x = VINDU_BREDDE / 2
        self.y = VINDU_HOYDE / 2
        self.fart_x = 3
        self.fart_y = 3
        self.rect = pg.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.game_over = 0
        

    def tegn(self):
        pg.draw.rect(vindu, morkeblaa, self.rect)
        
    def flytt(self):
        kollisjon_tolleranse = 5
        if self.rect.x <= 0 or self.rect.x >= VINDU_BREDDE - (self.radius * 2):
            self.fart_x *= -1
        #Sjekker topp kollisjon
        if self.rect.y <= 0:
            self.fart_y *= -1
        #Sjekker om spiller treffer bakken, og taper
        if self.rect.y >= VINDU_HOYDE - (self.radius * 2):
            self.game_over = -1
            
        #Sjekker kollisjon med plattform
        if self.rect.colliderect(plattform):
            if abs(self.rect.bottom - plattform.rect.top) < kollisjon_tolleranse:
                self.fart_y *= -1
            else:
                self.fart_x *= -1


        self.rect.x += self.fart_x
        self.rect.y += self.fart_y

plattform = Plattform()
firkant = Firkant()

def tegn_vindu():
    vindu.fill(farge)
    plattform.tegn()
    firkant.tegn()
    firkant.flytt()
    trykkede_taster = pg.key.get_pressed()
    plattform.flytt(trykkede_taster)
    pg.display.update()
    

def main():
    clock = pg.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        tegn_vindu()
        
    pg.quit()
    
if __name__ == "__main__":
    main()