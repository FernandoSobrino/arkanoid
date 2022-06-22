import os

import pygame as pg
from pygame.sprite import Sprite

from . import ALTO,ANCHO


class Raqueta(Sprite):

    margen_inferior = 20
    

    def __init__(self):
        super().__init__()

        self.sprites = [
            pg.image.load(os.path.join("resources","images","electric00.png")),
            pg.image.load(os.path.join("resources", "images", "electric01.png")),
            pg.image.load(os.path.join("resources", "images", "electric02.png")),
        ]
        self.contador = 0

        image_path = os.path.join("resources","images","electric00.png")
        self.image = pg.image.load(os.path.join(image_path))
        self.rect = self.image.get_rect(midbottom=(ANCHO/2,ALTO - self.margen_inferior))

    def update(self):
        #self.rect.x = self.rect.x + 1
        self.image = self.sprites[self.contador]
        self.contador += 1
        if self.contador > 2:
            self.contador = 0
