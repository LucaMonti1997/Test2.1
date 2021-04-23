import random
from Constantes import *


class Narrador(object):
    def __init__(self, jugador1, jugador2):
        """
        Se encarga de "dirigir" la partida. Reparte las cartas, gestiona los turnos, generación de recursos, eventos
        aleatorios, etc.
        """
        self.turno_jugador1 = False
        self.turno_jugador2 = False
        self.turno = 0
        self.turno_acabado = False
        self.jugadores = [jugador1, jugador2]

    def Opuesto(self):
        """
        Devuelve el turno opuesto, i.e. 0 -> 1 | 1 -> 0
        """
        return abs(self.turno - 1)

    def IniciarPartida(self):
        """
        Escoje aleatoramente quien empieza.
        """
        if random.choice([True, False]):
            self.turno = 0
        else:
            self.turno = 1
        self.turno_acabado = True

    def CambiarTurno(self):
        """
        Cambia el turno de un jugador al otro.
        """
        self.turno = self.Opuesto()
        self.turno_acabado = False

    def GenerarRecursos(self):
        """
        Genera los recursos que corresponden.
        """
        self.jugadores[self.turno].ladrillos += self.jugadores[self.turno].constructores
        self.jugadores[self.turno].armas += self.jugadores[self.turno].soldados
        self.jugadores[self.turno].mana += self.jugadores[self.turno].magos

    def JugarTurno(self, carta, jugar=True):
        """
        Llevará a cabo la acción escogida por el jugador activo.

        Jugar o descartar una carta, basicamente.

        :param carta: String. Identificador de la carta jugada
        :param jugar: Boolean. Jugamos o no la carta? False es descartar
        """

        if jugar:
            # Vemos cuantos recursos y de que tipo se gastan, y luego los restamos al jugador activo
            recurso = diccionario_cartas[carta][0][1]
            cantidad_recurso = diccionario_cartas[carta][0][0]
            self.jugadores[self.turno].set(recurso, self.jugadores[self.turno].get(recurso) + cantidad_recurso)

            # Vemos el atributo objetivo, y la cantidad a modificar.
            # Según la cantidad afectamos al jugador activo o al oponente
            objetivo = diccionario_cartas[carta][1][1]
            cantidad_objetivo = diccionario_cartas[carta][1][0]
            # Cantidad positiva. El efecto es para uno mismo.
            if cantidad_objetivo > 0:
                self.jugadores[self.turno].set(objetivo, self.jugadores[self.turno].get(objetivo) + cantidad_objetivo)
            # Cantidad negativa. El efecto es para el oponente.
            else:
                self.jugadores[self.Opuesto()].set(objetivo,
                                                   self.jugadores[self.Opuesto()].get(objetivo) + cantidad_objetivo)

        # Quitamos la carta de la mano del jugador activo
        self.jugadores[self.turno].mano.remove(carta)
        self.jugadores[self.turno].CogerUnaCarta()
        self.CambiarTurno()

    def ComprobarPartida(self):
        """
        Comprueba si la partida ha acabado.

        0 -> Partida no acabada

        1 -> Jugador1.hp_castillo <= 0

        2 -> Jugador1.hp_castillo >= 100

        3 -> Jugador2.hp_castillo <= 0

        4 -> Jugador2.hp_castillo >= 100
        """
        if self.jugadores[0].hp_castillo <= 0:
            return 1
        elif self.jugadores[0].hp_castillo >= 100:
            return 2
        elif self.jugadores[1].hp_castillo <= 0:
            return 3
        elif self.jugadores[1].hp_castillo >= 100:
            return 4
        else:
            return 0
