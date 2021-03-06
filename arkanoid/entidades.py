import os

import pygame as pg
from pygame.sprite import Sprite

from . import ALTO, ANCHO, FPS, COLOR_BLANCO, MARGEN_LATERAL, PUNTOS_PARTIDA


class Raqueta(Sprite):
    velocidad = 5
    margen_inferior = 50
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
    puntuacion = PUNTOS_PARTIDA
    def __init__(self, fila, columna,puntuacion):
        super().__init__()

        ladrillo_verde = os.path.join("resources", "images", "greenTile.png")

        self.image = pg.image.load(ladrillo_verde)
        ancho_ladrillo = self.image.get_width()
        alto_ladrillo = self.image.get_height()
        self.puntos = puntuacion
        
        self.rect = self.image.get_rect(
            x=columna*ancho_ladrillo, y=fila*alto_ladrillo)


class Pelota(Sprite):
    velocidad_x = -5
    velocidad_y = -5
    he_perdido = False
    pelota_en_movimiento = False

    def __init__(self, **kwargs):
        super().__init__()
        self.image = pg.image.load(os.path.join(
            "resources", "images", "ball1.png"))
        self.rect = self.image.get_rect(**kwargs)

    def update(self, raqueta, juego_iniciado):
        if not juego_iniciado:
            self.rect = self.image.get_rect(midbottom=raqueta.rect.midtop)
        else:
            self.rect.x += self.velocidad_x
            if self.rect.right > ANCHO or self.rect.left < 0:
                self.velocidad_x = -self.velocidad_x
            self.rect.y += self.velocidad_y
            if self.rect.top <= 0:
                self.velocidad_y = -self.velocidad_y
            if self.rect.top > ALTO:
                self.he_perdido = True

    def hay_colision(self, otro):
        if self.rect.colliderect(otro):
            self.velocidad_y = - self.velocidad_y
    

class Marcador:
    def __init__(self):
        self.valor = 0
        font_file = os.path.join("resources", "fonts", "LibreFranklin-VariableFont_wght.ttf")
        self.tipografia = pg.font.Font(font_file, 20)

    def aumentar(self,puntos):
        self.valor += puntos

    def pintar_marcador(self, pantalla):
        texto_marcador = f"Puntos: {self.valor}"
        texto = self.tipografia.render(str(texto_marcador), True, COLOR_BLANCO)
        pos_x = 20
        pos_y = ALTO-texto.get_height()-10
        pg.surface.Surface.blit(pantalla, texto, (MARGEN_LATERAL,pos_y))


class ContadorVidas:
    def __init__(self,vidas_iniciales):
        self.vidas = vidas_iniciales
        font_file = os.path.join("resources", "fonts",
                                 "LibreFranklin-VariableFont_wght.ttf")
        self.tipografia = pg.font.Font(font_file, 20)

    def perder_vida(self):
        self.vidas -= 1
        return self.vidas < 1

    def pintar_marcador_vidas(self,pantalla):
        texto_marcador_vidas = f"Vidas: {self.vidas}"
        texto = self.tipografia.render(str(texto_marcador_vidas),True,COLOR_BLANCO)
        pos_x = texto.get_width()
        pos_y = ALTO -texto.get_height()-10
        pg.surface.Surface.blit(pantalla,texto,(ANCHO-pos_x-MARGEN_LATERAL,pos_y))

