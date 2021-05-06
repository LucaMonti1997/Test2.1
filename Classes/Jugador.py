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

    def __init__(self, base, mazo, identificador):
        """
        Almacena toda la información del jugador, y gestiona varias de sus interacciones.

        :param base: Objeto Base.
        :param mazo: Objeto Mazo.
        :param identificador: 0 -> Jugador1; 1 -> Jugador2
        """
        # Castillo x muralla
        self.hp_castillo = 69
        self.hp_muralla = 42

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

        self.base = base
        self.id = identificador

        # Poblar la mano por primera vez
        random.shuffle(self.mazo.cartas_restantes)
        x = 0
        while len(self.mano) < NUMERO_CARTAS_MANO:
            identificador_carta = self.mazo.cartas_restantes.pop()
            self.mano.append(identificador_carta)
            carta_n = Carta(identificador_carta, True, (50 + (WIDTH-100)/8 * x, HEIGHT - 200), (1, 1))
            self.cartas.append(carta_n)
            x += 1

    def CogerUnaCarta(self):
        """
        Coge cartas mientras tenga sitio en la mano
        """
        self.mazo.ComprobarMazo()
        self.mano.append(self.mazo.cartas_restantes.pop())
        i = 0
        while i < NUMERO_CARTAS_MANO:
            self.cartas[i].id = self.mano[i]
            i += 1

    def InicialziarImagenes(self):
        """
        Precargamos las imagenes en un diccionario y hacemos ajustes a sus dimensiones.
        """

        self.imagenes = {
            "muralla": pygame.image.load("Assets/NewCards/1.png").convert_alpha(),
            "espada": pygame.image.load("Assets/NewCards/2.png").convert_alpha(),
        }
        self.iconos = {
            "ladrillos": pygame.image.load("Assets/Iconos/Bricks.png").convert_alpha(),
            "constructores": pygame.image.load("Assets/Iconos/Builders.png").convert_alpha(),
            "espadas": pygame.image.load("Assets/Iconos/Weapons.png").convert_alpha(),
            "soldados": pygame.image.load("Assets/Iconos/Soldiers.png").convert_alpha(),
            "mana": pygame.image.load("Assets/Iconos/Crystals.png").convert_alpha(),
            "magos": pygame.image.load("Assets/Iconos/Magic.png").convert_alpha(),
            "escudo": pygame.image.load("Assets/Iconos/escudo.png").convert_alpha(),
            "corazon": pygame.image.load("Assets/Iconos/Corazon.png").convert_alpha(),
        }

        # modificamos las imagenes para que quepan en pantalla

        for key in self.imagenes:
            self.imagenes[key] = pygame.transform.smoothscale(self.imagenes[key], (
                int(self.imagenes[key].get_width() / 1), int(self.imagenes[key].get_height() / 1)))
        for key in self.iconos:
            ancho = self.iconos[key].get_width()
            nuevo_ancho = int(WIDTH / 25)
            alto = self.iconos[key].get_height()
            nuevo_alto = int((alto * nuevo_ancho) / ancho)
            self.iconos[key] = pygame.transform.smoothscale(self.iconos[key], (nuevo_ancho, nuevo_alto))

    def MostrarCartas(self, pantalla):
        """
        Se llama el metodo Dibujar de cada carta para mostrarla en pantalla.

        :param pantalla: Objeto pygame.display. Donde se muestran las imagenes
        """

        # dibujamos las cartas con la imagen correspondiente segun el id de la carta
        for carta in self.cartas:
            carta.Dibujar(pantalla, self.imagenes[carta.id])

    def MostrarRecursos(self, pantalla):
        """
        Se dibujan los recursos en pantalla.

        :param pantalla: Objeto pygame.display. Donde se muestran las imagenes
        """
        # Ancho y alto base de los rectangulos
        ancho = WIDTH / 10
        alto = ancho
        gap = 1.2
        recuadro_ladrillos = ((WIDTH / 25) * abs((self.id - 1)) + (WIDTH - (WIDTH / 25) - ancho) * self.id,
                              HEIGHT / 20, ancho, alto)
        recuadro_espadas = ((WIDTH / 25) * abs((self.id - 1)) + (WIDTH - (WIDTH / 25) - ancho) * self.id,
                            (HEIGHT / 20) + alto * gap, ancho, alto)
        recuadro_mana = ((WIDTH / 25) * abs((self.id - 1)) + (WIDTH - (WIDTH / 25) - ancho) * self.id,
                         (HEIGHT / 20) + alto * gap * 2, ancho, alto)
        pygame.draw.rect(pantalla, RED, recuadro_ladrillos)
        pygame.draw.rect(pantalla, GREEN, recuadro_espadas)
        pygame.draw.rect(pantalla, YELLOW, recuadro_mana)

        texto_constructores = Constantes.font_recursos.render(str(self.constructores), False, (0, 0, 0))
        texto_ladrillos = Constantes.font_recursos.render(str(self.ladrillos), False, (0, 0, 0))
        texto_soldados = Constantes.font_recursos.render(str(self.soldados), False, (0, 0, 0))
        texto_espadas = Constantes.font_recursos.render(str(self.espadas), False, (0, 0, 0))
        texto_magos = Constantes.font_recursos.render(str(self.magos), False, (0, 0, 0))
        texto_mana = Constantes.font_recursos.render(str(self.mana), False, (0, 0, 0))

        # Costructores
        pantalla.blit(texto_constructores,
                      [((WIDTH / 25) + ancho * 3 / 15) * abs((self.id - 1)) +
                       (WIDTH - (WIDTH / 25) - ancho + ancho * 3 / 15) * self.id, (HEIGHT / 20) + (alto * 2 / 15)])
        pantalla.blit(self.iconos["constructores"], [
            ((WIDTH / 25) + ancho * 13 / 15 - self.iconos["constructores"].get_width()) * abs((self.id - 1)) +
            (WIDTH - (WIDTH / 25) - ancho + ancho * 13 / 15 - self.iconos["constructores"].get_width()) * self.id,
            (HEIGHT / 20) + (alto * 1 / 15)])

        # Ladrillos
        pantalla.blit(texto_ladrillos,
                      [((WIDTH / 25) + ancho * 3 / 15) * abs((self.id - 1)) +
                       (WIDTH - (WIDTH / 25) - ancho + ancho * 3 / 15) * self.id,
                       (HEIGHT / 20) + (alto * 2 / 15) + (alto / 2)])
        pantalla.blit(self.iconos["ladrillos"], [
            ((WIDTH / 25) + ancho * 13 / 15 - self.iconos["ladrillos"].get_width()) * abs((self.id - 1)) +
            (WIDTH - (WIDTH / 25) - ancho + ancho * 13 / 15 - self.iconos["ladrillos"].get_width()) * self.id,
            (HEIGHT / 20) + (alto * 1 / 15) + (alto / 2)])

        # Soldados
        pantalla.blit(texto_soldados,
                      [((WIDTH / 25) + ancho * 3 / 15) * abs((self.id - 1)) +
                       (WIDTH - (WIDTH / 25) - ancho + ancho * 3 / 15) * self.id,
                       (HEIGHT / 20) + (alto * 2 / 15) + alto * gap])
        pantalla.blit(self.iconos["soldados"], [
            ((WIDTH / 25) + ancho * 13 / 15 - self.iconos["soldados"].get_width()) * abs((self.id - 1)) +
            (WIDTH - (WIDTH / 25) - ancho + ancho * 13 / 15 - self.iconos["soldados"].get_width()) * self.id,
            (HEIGHT / 20) + (alto * 1 / 15) + (alto * gap)])

        # Espadas
        pantalla.blit(texto_espadas,
                      [((WIDTH / 25) + ancho * 3 / 15) * abs((self.id - 1)) +
                       (WIDTH - (WIDTH / 25) - ancho + ancho * 3 / 15) * self.id,
                       (HEIGHT / 20) + (alto * 2 / 15) + (alto / 2) + (alto * gap)])
        pantalla.blit(self.iconos["espadas"], [
            ((WIDTH / 25) + ancho * 13 / 15 - self.iconos["espadas"].get_width()) * abs((self.id - 1)) +
            (WIDTH - (WIDTH / 25) - ancho + ancho * 13 / 15 - self.iconos["espadas"].get_width()) * self.id,
            (HEIGHT / 20) + (alto * 1 / 15) + (alto / 2) + (alto * gap)])

        # Magos
        pantalla.blit(texto_magos,
                      [((WIDTH / 25) + ancho * 3 / 15) * abs((self.id - 1)) +
                       (WIDTH - (WIDTH / 25) - ancho + ancho * 3 / 15) * self.id,
                       (HEIGHT / 20) + (alto * 2 / 15) + alto * gap * 2])
        pantalla.blit(self.iconos["magos"], [
            ((WIDTH / 25) + ancho * 13 / 15 - self.iconos["magos"].get_width()) * abs((self.id - 1)) +
            (WIDTH - (WIDTH / 25) - ancho + ancho * 13 / 15 - self.iconos["magos"].get_width()) * self.id,
            (HEIGHT / 20) + (alto * 1 / 15) + (alto * gap * 2)])

        # Mana
        pantalla.blit(texto_mana,
                      [((WIDTH / 25) + ancho * 3 / 15) * abs((self.id - 1)) +
                       (WIDTH - (WIDTH / 25) - ancho + ancho * 3 / 15) * self.id,
                       (HEIGHT / 20) + (alto * 2 / 15) + (alto / 2) + (alto * gap * 2)])
        pantalla.blit(self.iconos["mana"], [
            ((WIDTH / 25) + ancho * 13 / 15 - self.iconos["mana"].get_width()) * abs((self.id - 1)) +
            (WIDTH - (WIDTH / 25) - ancho + ancho * 13 / 15 - self.iconos["mana"].get_width()) * self.id,
            (HEIGHT / 20) + (alto * 1 / 15) + (alto / 2) + (alto * gap * 2)])

    def MostrarBase(self, pantalla):
        """
        Primero se calculan los offsets de los atributos de base, luego se llama a base.Dibujar para que se muestre
        en pantalla

        :param pantalla: Objeto pygame.display. Donde se muestran las imagenes
        """
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

        texto_hp_castillo = Constantes.font_recursos.render(str(self.hp_castillo), False, (0, 0, 0))
        texto_hp_muralla = Constantes.font_recursos.render(str(self.hp_muralla), False, (0, 0, 0))
        pantalla.blit(texto_hp_castillo, [self.base.coord[0] - 75, self.base.coord[1] - 200])
        pantalla.blit(self.iconos["corazon"], [self.base.coord[0] - 65, self.base.coord[1] - 209])
        pantalla.blit(texto_hp_muralla, [self.base.coord[0] + 25, self.base.coord[1] - 200])
        pantalla.blit(self.iconos["escudo"], [self.base.coord[0] + 50, self.base.coord[1] - 213])

    def Set(self, attr, value):
        setattr(self, attr, value)

    def Get(self, attr):
        return getattr(self, attr)
