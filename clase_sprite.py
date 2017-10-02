import pygame
from math import *
import random

ALTO = 400
ANCHO = 640

ROJO = [255,0,0]
BLANCO = [255,255,255]
AZUL = [0,0,255]

class Jugador(pygame.sprite.Sprite):
    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an,al])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.var_x = 0
        self.var_y = 0


    def update(self):
        #if self.rect <(ANCHO-70):
        self.rect.x += self.var_x
        self.rect.y += self.var_y

class Rival(pygame.sprite.Sprite):
    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an,al])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.var_x = 0
        self.var_y =2
        self.temporizador=random.randrange(1000)

    def update(self):
        if self.temporizador > 0:
            self.temporizador -= 1
        else:
            self.rect.y += self.var_y

'''
        if self.rect.y > ANCHO:
            self.var_y = -4

        if self.rect.y < 0:
            self.var_y = 4

        self.rect.x += self.var_x
'''


if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pantalla.fill(BLANCO)
    jp = Jugador(70,5)
    general = pygame.sprite.Group()
    general.add(jp)
    reloj = pygame.time.Clock()
    jp.rect.x = (ANCHO/2)-35
    jp.rect.y = ALTO-20

    rivales = pygame.sprite.Group()
    n = 10
    ls_col = pygame.sprite.Group()
    for i in range(n):
        r = Rival(20,20)
        r.rect.x=  random.randrange(0, ANCHO )
        r.rect.y=-20
        #r.rect.x = random.randrange(0, ANCHO )
        #r.rect.y = random.randrange(0, ALTO  )
        rivales.add(r)
        general.add(r)

    pygame.display.flip()
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jp.var_x = 10
                '''if event.key == pygame.K_UP:
                    jp.var_y = -5'''
                if event.key == pygame.K_LEFT:
                    jp.var_x = -10
                '''if event.key == pygame.K_DOWN:
                    jp.var_y = 5'''
                if event.key == pygame.K_SPACE:
                    jp.var_y = 0
                    jp.var_x = 0
            if event.type == pygame.KEYUP:
                jp.var_y = 0
                jp.var_x = 0
            if event.type == pygame.QUIT:
                fin = True

        #gestion de colision
        ls_col=pygame.sprite.spritecollide(jp, rivales, True)

        #actualizacion de pantalla
        general.update()
        #rivales.update()
        pantalla.fill(BLANCO)
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
