from importlib import resources
import pygame as pg
from arkanoid import ALTO, ANCHO


class Arkanoid:
    def __init__(self):
        print("Arranca el juego")
        pg.init()
        self.display = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Keepkanoid")
        icon = pg.image.load("resources/images/icon.png")
        pg.display.set_icon(icon)

    def jugar(self):
        """Este es el bucle principal"""
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        salir = True
                self.display.fill((99, 99, 99))
                pg.display.flip()
