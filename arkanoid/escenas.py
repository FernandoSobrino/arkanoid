import os
import pygame as pg

from inputbox.inputbox import InputBox

from . import ANCHO, ALTO, COLOR_BLANCO, COLOR_FONDO_PORTADA, FPS, PUNTOS_PARTIDA, VIDAS
from .entidades import ContadorVidas, Ladrillo, Marcador, Pelota, Raqueta
from .records import Records


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
        self.pelota = Pelota(midbottom=self.jugador.rect.midtop)
        self.marcador = Marcador()
        self.contador_vidas = ContadorVidas(VIDAS)
        self.crear_muro()

    def bucle_principal(self):
        salir = False
        pelota_en_movimiento = False

        while not salir:
            self.reloj.tick(FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    pelota_en_movimiento = True

            self.pintar_fondo()

            # pintar los marcadores: puntos y vidas
            self.marcador.pintar_marcador(self.pantalla)
            self.contador_vidas.pintar_marcador_vidas(self.pantalla)

            # pintar la raqueta
            self.jugador.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)

            # pintar la pelota
            self.pelota.update(self.jugador, pelota_en_movimiento)
            self.pantalla.blit(self.pelota.image, self.pelota.rect)

            # pintar el muro
            self.ladrillos.draw(self.pantalla)

            # lo que comprueba la colision con la paleta y con los ladrillos
            self.pelota.hay_colision(self.jugador)
            self.golpeados = pg.sprite.spritecollide(
                self.pelota, self.ladrillos, True)
            if len(self.golpeados) > 0:
                self.pelota.velocidad_y *= -1
                for ladrillo in self.golpeados:
                    self.marcador.aumentar(ladrillo.puntos)

            # recargar todos los cambios
            pg.display.flip()

            # parte para comprobar que la pelota se sale de la pantalla, restar vida e iniciar la pelota
            if self.pelota.he_perdido:
                salir = self.contador_vidas.perder_vida()
                pelota_en_movimiento = False
                self.pelota.he_perdido = False
            if salir:
                self.comprobar_record()

            # volver a pintar el muro cuando se acaban los ladrillos
            if len(self.ladrillos.sprites()) == 0:
                self.crear_muro()

    # método para crear el muro de ladrillos

    def crear_muro(self):
        num_filas = 5
        num_columnas = 6
        self.ladrillos = pg.sprite.Group()
        self.ladrillos.empty()
        margen_y = 40

        for fila in range(num_filas):
            puntos = (num_filas - fila)*10
            for columna in range(num_columnas):
                self.ladrillo = Ladrillo(fila, columna, puntos)
                margen_x = (ANCHO - self.ladrillo.image.get_width()
                            * num_columnas) / 2
                self.ladrillo.rect.x += margen_x
                self.ladrillo.rect.y += margen_y
                self.ladrillos.add(self.ladrillo)

    # método para insertar la imagen azul en el fondo de la partida

    def pintar_fondo(self):
        self.pantalla.blit(self.fondo, (0, 0))

    def comprobar_record(self):
        records = Records()
        records.cargar_records()
        min_record = records.puntuacion_menor()
        if min_record < self.marcador.valor:
            # hay record, entramos en el bucle del input
            inputbox = InputBox(self.pantalla)
            nombre = inputbox.get_text()
            print(records.game_records)
            records.insertar_record(nombre, self.marcador.valor)
            records.guardar_records()


class HallOfFame(Escena):

    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)
        bg_file = os.path.join("resources", "images", "background.jpg")
        self.fondo = pg.image.load(bg_file)
        self.records = Records()
        self.records.cargar_records()
        font_file = os.path.join("resources", "fonts", "CabinSketch-Bold.ttf")
        self.tipografia = pg.font.Font(font_file, 20)

    def bucle_principal(self):
        borde = 100
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            self.pintar_fondo()
            self.records.cargar_records()
            for records in range(len(self.records.game_records)):
                texto_render = self.tipografia.render(
                    str(self.records.game_records[records]), True, COLOR_BLANCO)
                pos_x = ANCHO/2 - texto_render.get_width()
                pos_y = records*texto_render.get_height() + borde*2
                self.pantalla.blit(texto_render, (pos_x, pos_y))

            pg.display.flip()

    def pintar_fondo(self):
        self.pantalla.blit(self.fondo, (0, 0))
