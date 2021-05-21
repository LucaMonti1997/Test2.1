import random
from time import sleep
import pygame.font
import json

import Constantes
from Carta import *
from Constantes import *


# Clase de jugador a la qual se le asignaran las siguientes funciones:
#   Generar controlar los recursos de las instancias de los jugadores
#   controlar las cartas asignadas a los jugadores


class Jugador(object):

    def __init__(self, base, mazo, identificador):
        """
        Almacena toda la información del jugador, y gestiona varias de sus interacciones.

        :param base: Objeto Base.
        :param mazo: Objeto Mazo.
        :param identificador: 0 -> Jugador1; 1 -> Jugador2
        """
        # Vida castillo y muralla
        self.hp_castillo = 0
        self.hp_muralla = 0
        # Generadores de recursos
        self.constructores = 0
        self.soldados = 0
        self.magos = 0
        # Recursos
        self.ladrillos = 0
        self.espadas = 0
        self.mana = 0
        # Cartas en mano
        self.cartas = []
        # Graficos
        self.imagenes = {}
        self.iconos = {}

        self.mazo = mazo
        self.base = base
        self.id = identificador

        self.InicializarJugador()

    def InicializarJugador(self):
        """
        Asigna valor iniciales a los atributo del jugador
        """
        self.hp_castillo = 50
        self.hp_muralla = 35

        self.constructores = 2
        self.soldados = 2
        self.magos = 2

        self.ladrillos = 5
        self.espadas = 5
        self.mana = 5

        self.InicialziarImagenes()
        self.base.InicizializarBase()
        self.mazo.InicializarMazo()
        self.InicializarMano()

    def InicializarMano(self):
        """
        Poblar la mano por primera vez
        """
        self.cartas = []
        random.shuffle(self.mazo.cartas_restantes)
        x = 0
        while len(self.cartas) < NUMERO_CARTAS_MANO:
            identificador_carta = self.mazo.cartas_restantes.pop()
            carta_n = Carta(identificador_carta, True, (50 + (WIDTH - 100) / 8 * x, HEIGHT - 200),
                            (self.imagenes["muralla1"][0].get_width(), self.imagenes["muralla1"][0].get_height()))
            self.cartas.append(carta_n)
            x += 1
        self.ComprobarTodasCartas()

    def InicialziarImagenes(self):
        """
        Precargamos las imagenes en un diccionario y hacemos ajustes a sus dimensiones.
        """

        # Crear archivos para cargar
        with open('imagenes.json') as json_file:
            imagenes = json.load(json_file)

            for imagen in imagenes:
                self.imagenes[imagen] = [
                    pygame.image.load(imagenes[imagen][0]).convert_alpha(),
                    pygame.image.load(imagenes[imagen][1]).convert_alpha()]

        with open('iconos.json') as json_file_iconos:
            iconos = json.load(json_file_iconos)

            for icono in iconos:
                self.iconos[icono] = pygame.image.load(iconos[icono]).convert_alpha()

        # modificamos las imagenes para que quepan en pantalla

        for key in self.imagenes:
            for imagen in self.imagenes[key]:
                imagen = pygame.transform.smoothscale(imagen,
                                                      (int(imagen.get_width() / 1), int(imagen.get_height() / 1)))

        for key in self.iconos:
            ancho = self.iconos[key].get_width()
            nuevo_ancho = int(WIDTH / 25)
            alto = self.iconos[key].get_height()
            nuevo_alto = int((alto * nuevo_ancho) / ancho)
            self.iconos[key] = pygame.transform.smoothscale(self.iconos[key], (nuevo_ancho, nuevo_alto))

    def CogerCartas(self):
        """
        Coge cartas mientras tenga sitio en la mano
        """
        self.mazo.ComprobarMazo()
        for carta in self.cartas:
            if carta.id == "null":
                # Primero cambiamos el id a una imagen vacia/negra o lo que sea para luego hacerla parpadear
                carta.id = "no_card"
                sleep(0.3)
                carta.id = "no_card"
                sleep(0.3)
                carta.id = self.mazo.cartas_restantes.pop()
                sleep(0.5)

    def ComprobarCarta(self, carta):
        """
        Comprueba si una carta se puede jugar, y modifica su atributo estado.

        :param carta: Objeto Carta. Carta que se comprueba
        """
        if self.Get(diccionario_cartas[carta.id][0][1]) >= diccionario_cartas[carta.id][0][0]:
            carta.estado = True
        else:
            carta.estado = False

    def ComprobarTodasCartas(self):
        """
        Llama ComprobarCarta para todas las cartas
        """

        for carta in self.cartas:
            self.ComprobarCarta(carta)

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
        ancho = self.imagenes["magos"][0].get_width()
        alto = self.imagenes["magos"][0].get_height()
        gap = 1.2

        self.DistribuirGraficamente(pantalla, "constructores", 1, 0, ancho, alto, gap, "Recurso")
        self.DistribuirGraficamente(pantalla, "ladrillos", 3, 0, ancho, alto, gap, "Generador")
        self.DistribuirGraficamente(pantalla, "soldados", 1, 1, ancho, alto, gap, "Recurso")
        self.DistribuirGraficamente(pantalla, "espadas", 3, 1, ancho, alto, gap, "Generador")
        self.DistribuirGraficamente(pantalla, "magos", 1, 2, ancho, alto, gap, "Recurso")
        self.DistribuirGraficamente(pantalla, "mana", 3, 2, ancho, alto, gap, "Generador")

    def DistribuirGraficamente(self, pantalla, identidad, mult_hor, mult_ver, ancho, alto, gap, tipo="Recurso"):
        """
        Distribuye los elementos en pantalla.

        :param pantalla: Objeto pygame.display. Donde se muestran las imagenes.
        :param identidad: String. Identificador del tipo de elemento que estamos graficando.
        :param mult_hor: Int. Desplazamiento horizontal. [1 o 3]
        :param mult_ver: Int Numero de veces que hay que sumar la altura.[0,1,2]
        :param ancho: Numero. Ancho base de una imagen.
        :param alto: Numero. Alto base de una imagen.
        :param gap: Float. Proporción de distancia vertical entre imagenes.
        :param tipo: String. Indica si tenemos que mostrar una imagen con el mismo nombre de identidad o no.
        """
        texto = Constantes.font_recursos.render(str(self.Get(identidad)), False, (0, 0, 0))
        espesor = font_recursos.size(str(self.Get(identidad)))
        if tipo == "Recurso":
            pantalla.blit(self.imagenes[identidad][self.id], [(WIDTH / 25) * abs(self.id - 1) +
                                                              (WIDTH - (WIDTH / 25) - ancho) * self.id,
                                                              (HEIGHT / 20) + alto * gap * mult_ver])

        pantalla.blit(texto, [(((WIDTH / 25) + ancho * mult_hor / 4) * abs(self.id - 1) +
                               (WIDTH - (WIDTH / 25) - (ancho * mult_hor / 4)) * self.id) - espesor[0] / 2,
                              (HEIGHT / 20) + alto / 5 + alto * gap * mult_ver])

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


if __name__ == '__main__':
    pass
