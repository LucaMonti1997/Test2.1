import random

import pygame.font

from Constantes import *

pygame.font.init()
font = pygame.font.SysFont('Arial', 30)


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

        :param carta: Objeto Carta. Carta jugada
        :param jugar: Boolean. Jugamos o no la carta? False es descartar
        """

        if jugar:
            # Vemos cuantos recursos y de que tipo se gastan, y luego los restamos al jugador activo
            recurso = diccionario_cartas[carta.id][0][1]
            cantidad_recurso = diccionario_cartas[carta.id][0][0]
            self.jugadores[self.turno].Set(recurso, self.jugadores[self.turno].Get(recurso) + cantidad_recurso)

            # Vemos el atributo objetivo, y la cantidad a modificar.
            # Según la cantidad afectamos al jugador activo o al oponente
            objetivo = diccionario_cartas[carta.id][1][1]
            cantidad_objetivo = diccionario_cartas[carta.id][1][0]
            # Cantidad positiva. El efecto es para uno mismo.
            if cantidad_objetivo > 0:
                self.jugadores[self.turno].Set(objetivo, self.jugadores[self.turno].Get(objetivo) + cantidad_objetivo)
            # Cantidad negativa. El efecto es para el oponente.
            else:
                self.jugadores[self.Opuesto()].Set(objetivo,
                                                   self.jugadores[self.Opuesto()].Get(objetivo) + cantidad_objetivo)

        #Quitamos la carta de la mano del jugador activo

        self.jugadores[self.turno].mano.remove(carta.id)
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

    # No discrimina entre click izquierdo o derecho
    def DetectarClickCarta(self, pos):
        for carta in self.jugadores[self.turno].cartas:
            if carta.coord[0] < pos[0] < carta.coord[0] + self.jugadores[self.turno].imagenes["muralla"].get_width() \
                    and carta.coord[1] < pos[1] < carta.coord[1] + \
                    self.jugadores[self.turno].imagenes["muralla"].get_height():
                self.JugarTurno(carta, carta.estado)
                return
