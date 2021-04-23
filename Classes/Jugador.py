import random
from Mazo import *
from Constantes import *
from Carta import *


# Clase de jugador a la qual se le asignaran las siguientes funciones:
#   Generar controlar los recursos de las instancias de los jugafores
#   controlar las cartas asignadas a los jugadores


class Jugador(object):

    def __init__(self):
        # Castillo x muralla
        self.hp_castillo = 20
        self.hp_muralla = 10

        # Generadores
        self.constructores = 2
        self.soldados = 2
        self.magos = 2

        # Recursos
        self.ladrillos = 5
        self.armas = 5
        self.mana = 5

        # Crear mazo a partir de la classe Mazo
        self.mazo = Mazo(1)
        self.mano = []
        self.cartas = []

        # Poblar la mano por primera vez
        random.shuffle(self.mazo.cartas_restantes)
        x = 0
        while len(self.mano) < NUMERO_CARTAS_MANO:
            identificador = self.mazo.cartas_restantes.pop()
            self.mano.append(identificador)
            carta_n = Carta(identificador, True, (50 + 100 * x, 200), (1, 1))
            self.cartas.append(carta_n)
            x += 1

    def CogerUnaCarta(self):
        if self.mazo.cartas_restantes:
            self.mano.append(self.mazo.cartas_restantes.pop())
        else:
            self.mazo.cartas_restantes = self.mazo.mazo_1_completo
            random.shuffle(self.mazo.cartas_restantes)
            self.mano.append(self.mazo.cartas_restantes.pop())

    def MostrarCartas(self, pantalla):

        imagenes = {
            "Imagen1": pygame.image.load("Assets/Templates/images.png").convert_alpha(),
            "Imagen2": pygame.image.load("Assets/TestAssets/Espada1.png").convert_alpha()

        }

        for carta in self.cartas:
            carta.Dibujar(pantalla, imagenes["Imagen1"])
