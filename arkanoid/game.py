import os

import pygame as pg

from arkanoid import ALTO, ANCHO
from arkanoid.escenas import Portada, Partida, HallOfFame


class Arkanoid:
    def __init__(self):
        print("Arranca el juego")
        pg.init()
        self.display = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Fernanoid")
        game_logo_path = os.path.join("resources", "images", "icon.png")
        icon = pg.image.load(game_logo_path)
        pg.display.set_icon(icon)

        self.escenas = [
            Portada(self.display),
            Partida(self.display),
            HallOfFame(self.display),
        ]

    def jugar(self):
        """Este es el bucle principal"""
        for escena in self.escenas:
            escena.bucle_principal()
