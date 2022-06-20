import pygame as pg

class Escena:
    def __init__(self,pantalla):
        self.pantalla = pantalla

    def bucle_principal(self):
       pass


class Portada(Escena):
    
    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        salir = True
                self.pantalla.fill((99, 0, 0))
                pg.display.flip()
   

class Partida(Escena):
    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        salir = True
                self.pantalla.fill((0, 99, 0))
                pg.display.flip()

class HallOfFame(Escena):
    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        salir = True
                self.pantalla.fill((0, 0, 99))
                pg.display.flip()
