import os

import pygame as pg

from . import ANCHO, ALTO, COLOR_BLANCO


class Escena:
    def __init__(self, pantalla: pg.Surface):
        self.pantalla = pantalla

    def bucle_principal(self):
        pass


class Portada(Escena):
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)
        self.logo = pg.image.load(
            os.path.join("resources", "images", "arkanoid_name.png"))
        
        font_file = os.path.join("resources", "fonts", "CabinSketch-Bold.ttf")
        self.tipografia = pg.font.Font(font_file,40)
        

    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                        salir = True
                if event.type == pg.QUIT:
                    pg.quit()
            self.pantalla.fill((99, 0, 0))
            
            self.pintar_logo()
            self.pintar_texto()
            
            pg.display.flip()

    def pintar_logo(self):
        ancho_logo = self.logo.get_width()
        pos_x = (ANCHO - ancho_logo) / 2
        pos_y = ALTO / 3
        self.pantalla.blit(self.logo,(pos_x,pos_y))

    def pintar_texto(self):
        mensaje = "Pulsa espacio para empezar"
        texto = self.tipografia.render(mensaje,True,COLOR_BLANCO)
        ancho_texto = texto.get_width()
        pos_x = (ANCHO - ancho_texto)/2
        pos_y = .75 * ALTO
        self.pantalla.blit(texto,(pos_x,pos_y))


class Partida(Escena):
    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            self.pantalla.fill((0, 99, 0))
            pg.display.flip()


class HallOfFame(Escena):
    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            self.pantalla.fill((0, 0, 99))
            pg.display.flip()
