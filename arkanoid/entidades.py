import os

import pygame as pg
from pygame.sprite import Sprite

from . import ALTO, ANCHO, FPS


class Raqueta(Sprite):
    velocidad = 5
    margen_inferior = 20
    fps_animacion = 12
    limite_iteracion = FPS // fps_animacion
    iteracion = 0

    def __init__(self):
        super().__init__()

        self.sprites = []
        for i in range(3):
            self.sprites.append(pg.image.load(os.path.join(
                "resources", "images", f"electric0{i}.png")))

        self.siguiente_imagen = 0
        self.image = self.sprites[self.siguiente_imagen]

        self.rect = self.image.get_rect(
            midbottom=(ANCHO/2, ALTO - self.margen_inferior))

    def update(self):
        # Comprobamos si hay tecla pulsada y actualizamos la posición
        tecla_mov_raqueta = pg.key.get_pressed()
        if tecla_mov_raqueta[pg.K_RIGHT]:
            self.rect.x += self.velocidad
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO
        if tecla_mov_raqueta[pg.K_LEFT]:
            self.rect.x -= self.velocidad
            if self.rect.left < 0:
                self.rect.left = 0

        # animamos el rayo de la raqueta
        #fps_animacion = 12
        #limite_iteracion = FPS/fps_animacion
        #iteracion = 0
        self.iteracion += 1
        if self.iteracion == self.limite_iteracion:
            self.siguiente_imagen += 1
            if self.siguiente_imagen >= len(self.sprites):
                self.siguiente_imagen = 0
            self.image = self.sprites[self.siguiente_imagen]
            self.iteracion = 0


class Ladrillo(Sprite):
    def __init__(self, fila, columna):
        super().__init__()

        ladrillo_verde = os.path.join("resources", "images", "greenTile.png")

        self.image = pg.image.load(ladrillo_verde)
        ancho_ladrillo = self.image.get_width()
        alto_ladrillo = self.image.get_height()
        self.rect = self.image.get_rect(
            x=columna*ancho_ladrillo, y=fila*alto_ladrillo)


class Pelota(Sprite):
    def __init__(self,**kwargs):
        super().__init__()
        self.image = pg.image.load(os.path.join("resources", "images", "ball1.png"))
        self.rect = self.image.get_rect(**kwargs)

    def update(self,raqueta,juego_iniciado):
        if not juego_iniciado:
            self.rect = self.image.get_rect(midbottom=raqueta.rect.midtop)

