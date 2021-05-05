import random
import Constantes
import pygame.font

from Mazo import *
from Constantes import *
from Carta import *
from Base import *


# Clase de jugador a la qual se le asignaran las siguientes funciones:
#   Generar controlar los recursos de las instancias de los jugafores
#   controlar las cartas asignadas a los jugadores


class Jugador(object):

    def __init__(self, coordenada_base, dimensiones_base, mazo, identificador):
        # Castillo x muralla
        self.hp_castillo = 69
        self.hp_muralla = 100

        # Generadores
        self.constructores = 2
        self.soldados = 2
        self.magos = 2

        # Recursos
        self.ladrillos = 5
        self.espadas = 5
        self.mana = 5

        # Crear mazo a partir de la classe Mazo
        self.mazo = mazo
        self.mano = []
        self.cartas = []

        self.imagenes = {}
        self.iconos = {}

        self.base = Base(coordenada_base, dimensiones_base)
        self.id = identificador

        # Poblar la mano por primera vez
        random.shuffle(self.mazo.cartas_restantes)
        x = 0
        while len(self.mano) < NUMERO_CARTAS_MANO:
            identificador = self.mazo.cartas_restantes.pop()
            self.mano.append(identificador)
            carta_n = Carta(identificador, True, (50 + 100 * x, HEIGHT - 200), (1, 1))
            self.cartas.append(carta_n)
            x += 1

    def CogerUnaCarta(self):
        self.mazo.ComprobarMazo()
        self.mano.append(self.mazo.cartas_restantes.pop())
        i = 0
        while i < NUMERO_CARTAS_MANO:
            self.cartas[i].id = self.mano[i]
            i += 1

    def InicialziarImagenes(self):

        # obtenemos el fondo de todas las cartas con una imagen

        self.imagenes = {
            "muralla": pygame.image.load("Assets/Cards/1.png").convert_alpha(),
            "defensa": pygame.image.load("Assets/Cards/2.png").convert_alpha(),
            "espada": pygame.image.load("Assets/Cards/3.png").convert_alpha(),
        }
        self.iconos = {
            "ladrillos": pygame.image.load("Assets/Iconos/Bricks.png").convert_alpha(),
            "constructores": pygame.image.load("Assets/Iconos/Builders.png").convert_alpha(),
            "espadas": pygame.image.load("Assets/Iconos/Weapons.png").convert_alpha(),
            "soldados": pygame.image.load("Assets/Iconos/Soldiers.png").convert_alpha(),
            "mana": pygame.image.load("Assets/Iconos/Crystals.png").convert_alpha(),
            "magos": pygame.image.load("Assets/Iconos/Magic.png").convert_alpha(),
        }

        # modificamos las imagenes para que quepan en pantalla

        for key in self.imagenes:
            self.imagenes[key] = pygame.transform.smoothscale(self.imagenes[key], (
                int(self.imagenes[key].get_width() / 8), int(self.imagenes[key].get_height() / 8)))
        for key in self.iconos:
            self.iconos[key] = pygame.transform.smoothscale(self.iconos[key], (
                int(self.iconos[key].get_width() / 1.3), int(self.iconos[key].get_height() / 1.3)))

    def MostrarCartas(self, pantalla):

        # dibujamos las cartas con la imagen correspondiente segun el id de la carta
        for carta in self.cartas:
            carta.Dibujar(pantalla, self.imagenes[carta.id])

    def MostrarRecursos(self, pantalla):
        if self.id == 1:
            recuadro_ladrillos = (20, 20, 50, 50)
            recuadro_espadas = (20, 100, 50, 50)
            recuadro_mana = (20, 180, 50, 50)
        else:
            recuadro_ladrillos = (WIDTH - 70, 20, 50, 50)
            recuadro_espadas = (WIDTH - 70, 100, 50, 50)
            recuadro_mana = (WIDTH - 70, 180, 50, 50)
        pygame.draw.rect(pantalla, RED, recuadro_ladrillos)
        pygame.draw.rect(pantalla, GREEN, recuadro_espadas)
        pygame.draw.rect(pantalla, YELLOW, recuadro_mana)

        texto_constructores = Constantes.font_recursos.render(str(self.constructores), False, (0, 0, 0))
        texto_ladrillos = Constantes.font_recursos.render(str(self.ladrillos), False, (0, 0, 0))
        texto_soldados = Constantes.font_recursos.render(str(self.soldados), False, (0, 0, 0))
        texto_espadas = Constantes.font_recursos.render(str(self.espadas), False, (0, 0, 0))
        texto_magos = Constantes.font_recursos.render(str(self.magos), False, (0, 0, 0))
        texto_mana = Constantes.font_recursos.render(str(self.mana), False, (0, 0, 0))
        if self.id == 1:
            pantalla.blit(texto_constructores, [25, 20])
            pantalla.blit(self.iconos["constructores"], [43, 20])
            pantalla.blit(texto_ladrillos, [25, 45])
            pantalla.blit(self.iconos["ladrillos"], [45, 48])
            pantalla.blit(texto_soldados, [25, 100])
            pantalla.blit(self.iconos["soldados"], [43, 101])
            pantalla.blit(texto_espadas, [25, 125])
            pantalla.blit(self.iconos["espadas"], [42, 125])
            pantalla.blit(texto_magos, [25, 180])
            pantalla.blit(self.iconos["magos"], [45, 182])
            pantalla.blit(texto_mana, [25, 205])
            pantalla.blit(self.iconos["mana"], [44, 205])
        else:
            pantalla.blit(texto_constructores, [WIDTH - 65, 20])
            pantalla.blit(self.iconos["constructores"], [WIDTH - 47, 20])
            pantalla.blit(texto_ladrillos, [WIDTH - 65, 45])
            pantalla.blit(self.iconos["ladrillos"], [WIDTH - 43, 48])
            pantalla.blit(texto_soldados, [WIDTH - 65, 100])
            pantalla.blit(self.iconos["soldados"], [WIDTH - 47, 101])
            pantalla.blit(texto_espadas, [WIDTH - 65, 125])
            pantalla.blit(self.iconos["espadas"], [WIDTH - 47, 125])
            pantalla.blit(texto_magos, [WIDTH - 65, 180])
            pantalla.blit(self.iconos["magos"], [WIDTH - 47, 182])
            pantalla.blit(texto_mana, [WIDTH - 65, 205])
            pantalla.blit(self.iconos["mana"], [WIDTH - 47, 205])

    def MostrarBase(self, pantalla):
        if self.hp_castillo < 40:
            self.base.offset["torre_izquierda"] = 0
            self.base.offset["torre_derecha"] = 0
            self.base.offset["torre_central"] = self.hp_castillo / 40
        elif self.hp_castillo < 70:
            self.base.offset["torre_izquierda"] = (self.hp_castillo - 40) / 30
            self.base.offset["torre_derecha"] = 0
            self.base.offset["torre_central"] = 1
        else:
            self.base.offset["torre_izquierda"] = 1
            self.base.offset["torre_derecha"] = (self.hp_castillo - 70) / 30
            self.base.offset["torre_central"] = 1

        self.base.offset["muralla"] = self.hp_muralla / 100

        # print(self.base.offset["torre_izquierda"], self.base.offset["torre_central"],self.base.offset["torre_derecha"])

        self.base.Dibujar(pantalla)

    def Set(self, attr, value):
        setattr(self, attr, value)

    def Get(self, attr):
        return getattr(self, attr)
