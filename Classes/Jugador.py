import Mazo
import random


# Clase de jugador a la qual se le asignaran las siguientes funciones:
#   Generar controlar los recursos de las instancias de los jugafores
#   controlar las cartas asignadas a los jugadores


class Jugador(object):

    def __init__(self):
        # Castillo y muralla
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
        self.mazo = Mazo(1).mazo_1_completo
        self.mano = []

        lista_aleatoria = random.sample(range(len(self.mazo) - 1), 8)
        lista_cartas_restantes = [num for num in range(max(lista_aleatoria) + 1) if num not in lista_aleatoria]

        for n in lista_aleatoria:
            self.mano.append(self.mazo[n])

        self.mazo = [self.mazo[x] for x in lista_cartas_restantes]

    def ModificarMano(self):
        pass
