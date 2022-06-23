import os

import pygame as pg

from . import ANCHO, ALTO, COLOR_BLANCO, COLOR_FONDO_PORTADA,FPS
from .entidades import Raqueta, Ladrillo


class Escena:
    def __init__(self, pantalla: pg.Surface):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pass


class Portada(Escena):
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)
        self.logo = pg.image.load(
            os.path.join("resources", "images", "arkanoid_name.png"))

        font_file = os.path.join("resources", "fonts", "CabinSketch-Bold.ttf")
        self.tipografia = pg.font.Font(font_file, 30)

    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True
                if event.type == pg.QUIT:
                    pg.quit()
            self.pantalla.fill((COLOR_FONDO_PORTADA))

            self.pintar_logo()
            self.pintar_texto()
            

            pg.display.flip()

    def pintar_logo(self):
        ancho_logo = self.logo.get_width()
        pos_x = (ANCHO - ancho_logo) / 2
        pos_y = ALTO / 3
        self.pantalla.blit(self.logo, (pos_x, pos_y))

    def pintar_texto(self):
        mensaje = "Pulsa 'ESPACIO' para comenzar partida"
        texto = self.tipografia.render(mensaje, True, COLOR_BLANCO)
        ancho_texto = texto.get_width()
        pos_x = (ANCHO - ancho_texto)/2
        pos_y = .75 * ALTO
        self.pantalla.blit(texto, (pos_x, pos_y))


class Partida(Escena):
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)
        bg_file = os.path.join("resources", "images", "background.jpg")
        self.fondo = pg.image.load(bg_file)
        self.jugador = Raqueta()
        self.crear_muro()

    def bucle_principal(self):
        salir = False
        while not salir:
            self.reloj.tick(FPS)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            self.pintar_fondo()
            
            #pintar la raqueta
            self.jugador.update()
            self.pantalla.blit(self.jugador.image,self.jugador.rect)
            
            #pintar el muro
            self.ladrillos.draw(self.pantalla)
            pg.display.flip()

    def pintar_fondo(self):
        self.pantalla.blit(self.fondo, (0, 0))

    def crear_muro(self):
        num_filas = 5
        num_columnas = 6
        self.ladrillos = pg.sprite.Group()
        self.ladrillos.empty()
        margen_y = 40
        

        for fila in range(num_filas):
            for columna in range(num_columnas):
                ladrillo = Ladrillo(fila,columna)
                margen_x = (ANCHO - ladrillo.image.get_width()*num_columnas) / 2 
                ladrillo.rect.x += margen_x
                ladrillo.rect.y += margen_y
                self.ladrillos.add(ladrillo)


        


class HallOfFame(Escena):
    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            self.pantalla.fill((0, 0, 99))
            pg.display.flip()
