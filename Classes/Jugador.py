import random
from Mazo import *
from Constantes import *
from Carta import *
from Base import *


# Clase de jugador a la qual se le asignaran las siguientes funciones:
#   Generar controlar los recursos de las instancias de los jugafores
#   controlar las cartas asignadas a los jugadores


class Jugador(object):

    def __init__(self, coordenada_base, dimensiones_base, mazo):
        # Castillo x muralla
        self.hp_castillo = 69
        self.hp_muralla = 100

        # Generadores
        self.constructores = 2
        self.soldados = 2
        self.magos = 2

        # Recursos
        self.ladrillos = 5
        self.armas = 5
        self.mana = 5

        # Crear mazo a partir de la classe Mazo
        self.mazo = mazo
        self.mano = []
        self.cartas = []

        self.imagenes = {}

        self.base = Base(coordenada_base, dimensiones_base)

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
        if self.mazo.cartas_restantes:
            self.mano.append(self.mazo.cartas_restantes.pop())
        else:
            self.mazo.cartas_restantes = self.mazo.mazo_1_completo
            random.shuffle(self.mazo.cartas_restantes)
            self.mano.append(self.mazo.cartas_restantes.pop())

    def InicialziarImagenes(self):

        # obtenemos el fondo de todas las cartas con una imagen

        self.imagenes = {
            "muralla": pygame.image.load("Assets/Cards/1.png").convert_alpha(),
            "defensa": pygame.image.load("Assets/Cards/2.png").convert_alpha(),
            "espada": pygame.image.load("Assets/Cards/3.png").convert_alpha(),
            "Imagen2": pygame.image.load("Assets/Cards/4.png").convert_alpha(),
            "Imagen1": pygame.image.load("Assets/Cards/5.png").convert_alpha(),
            "Imagen2": pygame.image.load("Assets/Cards/6.png").convert_alpha(),
            "Imagen1": pygame.image.load("Assets/Cards/7.png").convert_alpha(),
            "Imagen2": pygame.image.load("Assets/Cards/1.png").convert_alpha(),

        }

        # modificamos las imagenes para que quepan en pantalla

        for key in self.imagenes:
            self.imagenes[key] = pygame.transform.smoothscale(self.imagenes[key], (
                int(self.imagenes[key].get_width() / 8), int(self.imagenes[key].get_height() / 8)))

    def MostrarCartas(self, pantalla):

        # dibujamos las cartas con la imagen correspondiente segun el id de la carta
        for carta in self.cartas:
            carta.Dibujar(pantalla, self.imagenes[carta.id])

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
