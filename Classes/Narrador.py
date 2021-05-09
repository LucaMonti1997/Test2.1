import random

import pygame.font

from Constantes import *


class Narrador(object):
    def __init__(self, jugador1, jugador2):
        """
        Se encarga de "dirigir" la partida. Reparte las cartas, gestiona los turnos, generación de recursos, eventos
        aleatorios, etc.

        :param jugador1: Objeto Jugador. Jugador 1, tipicamente el unico humano
        :param jugador2: Objeto Jugador. Jugador 2, tipicamente la IA
        """
        self.turno = 0
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

    def CambiarTurno(self):
        """
        Cambia el turno de un jugador al otro.
        """
        self.turno = self.Opuesto()

    def GenerarRecursos(self):
        """
        Genera los recursos que corresponden.
        """
        self.jugadores[self.turno].ladrillos += self.jugadores[self.turno].constructores
        self.jugadores[self.turno].espadas += self.jugadores[self.turno].soldados
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
            self.jugadores[self.turno].Set(recurso, self.jugadores[self.turno].Get(recurso) - cantidad_recurso)

            # Vemos el atributo objetivo, y la cantidad a modificar.
            # Según la cantidad afectamos al jugador activo o al oponente
            objetivo = diccionario_cartas[carta.id][1][1]
            cantidad_objetivo = diccionario_cartas[carta.id][1][0]
            # Cantidad positiva. El efecto es para uno mismo.
            if cantidad_objetivo > 0:
                self.jugadores[self.turno].Set(objetivo,
                                               clamp(self.jugadores[self.turno].Get(objetivo) + cantidad_objetivo))
            # Cantidad negativa. El efecto es para el oponente.
            else:
                if objetivo == "hp_muralla" and self.jugadores[self.Opuesto()].Get("hp_muralla") == 0:
                    objetivo = "hp_castillo"
                self.jugadores[self.Opuesto()].Set(objetivo, clamp(self.jugadores[self.Opuesto()].Get(objetivo) +
                                                                   cantidad_objetivo))

        # Quitamos la carta de la mano del jugador activo
        self.jugadores[self.turno].mano.remove(carta.id)
        self.jugadores[self.turno].CogerUnaCarta()
        self.CambiarTurno()
        self.GenerarRecursos()
        self.jugadores[self.turno].ComprobarTodasCartas()

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
        """
        Detecta cual carta ha sido clickeada, y actua en consecuencia

        :param pos: Lista. Coordenadas donde se ha hecho click. [x, y]
        """
        for carta in self.jugadores[self.turno].cartas:
            if carta.coord[0] < pos[0] < carta.coord[0] + self.jugadores[self.turno].imagenes["muralla1"][0].get_width() \
                    and carta.coord[1] < pos[1] < carta.coord[1] + \
                    self.jugadores[self.turno].imagenes["muralla1"][0].get_height():
                self.JugarTurno(carta, carta.estado)
                return

    def CalculoIA(self):
        """
        La IA escoge la mejor carta
        """
        ponderacion = {}
        for carta in self.jugadores[self.turno].mano:
            nota = 0
            # Preservación
            if self.jugadores[self.turno].hp_muralla < 10:
                # Urge construir muralla
                pass
            elif self.jugadores[self.turno].hp_muralla < 40:
                # Urge menos construir muralla
                pass
            else:
                # No urge menos construir muralla
                pass
            if self.jugadores[self.turno].hp_castillo < 30:
                # Urge construir muralla
                pass
            elif self.jugadores[self.turno].hp_castillo < 60:
                # Urge menos construir muralla
                pass
            else:
                # No urge menos construir muralla
                pass

            # Comparación

            # Comparamos nuestra muralla con la enemiga.
            if diccionario_cartas[carta][1][0] > 0 and diccionario_cartas[carta][1][1] == "hp_muralla":
                # La carta construye muralla
                if (self.jugadores[self.turno].hp_muralla - self.jugadores[self.Opuesto()].hp_muralla) > 20:
                    # Tenemos bastante margen, no corre prisa construir mas muralla
                    pass
                elif (self.jugadores[self.turno].hp_muralla - self.jugadores[self.Opuesto()].hp_muralla) > 0:
                    # Tenemos algo de margen, no corre prisa construir mas muralla
                    pass
                elif (self.jugadores[self.turno].hp_muralla - self.jugadores[self.Opuesto()].hp_muralla) > -20:
                    # Tenemos algo de desventaja, considerar recuperarla
                    pass
            elif diccionario_cartas[carta][1][0] < 0 and diccionario_cartas[carta][1][1] == "hp_muralla":
                # La carta ataca la muralla enemiga
                if (self.jugadores[self.turno].hp_muralla - self.jugadores[self.Opuesto()].hp_muralla) > 20:
                    # Tenemos bastante margen, no corre prisa construir mas muralla
                    pass
                elif (self.jugadores[self.turno].hp_muralla - self.jugadores[self.Opuesto()].hp_muralla) > 0:
                    # Tenemos algo de margen, no corre prisa construir mas muralla
                    pass
                elif (self.jugadores[self.turno].hp_muralla - self.jugadores[self.Opuesto()].hp_muralla) > -20:
                    # Tenemos algo de desventaja, considerar recuperarla
                    pass

            # Comparamos nuestro castillo con el enemigo.
            if diccionario_cartas[carta][1][0] > 0 and diccionario_cartas[carta][1][1] == "hp_castillo":
                # La carta construye castillo
                if (self.jugadores[self.turno].hp_castillo - self.jugadores[self.Opuesto()].hp_castillo) > 30:
                    # Tenemos bastante margen, no corre prisa construir mas castillo
                    pass
                elif (self.jugadores[self.turno].hp_castillo - self.jugadores[self.Opuesto()].hp_castillo) > 0:
                    # Tenemos algo de margen, no corre prisa construir mas castillo
                    pass
                elif (self.jugadores[self.turno].hp_castillo - self.jugadores[self.Opuesto()].hp_castillo) > -10:
                    # Tenemos algo de desventaja, considerar recuperarla
                    pass
            elif diccionario_cartas[carta][1][0] < 0 and diccionario_cartas[carta][1][1] == "hp_castillo":
                # La carta ataca el castillo enemigo
                if (self.jugadores[self.turno].hp_castillo - self.jugadores[self.Opuesto()].hp_castillo) > 30:
                    # Tenemos bastante margen, no corre prisa construir mas castillo
                    pass
                elif (self.jugadores[self.turno].hp_castillo - self.jugadores[self.Opuesto()].hp_castillo) > 0:
                    # Tenemos algo de margen, no corre prisa construir mas castillo
                    pass
                elif (self.jugadores[self.turno].hp_castillo - self.jugadores[self.Opuesto()].hp_castillo) > -10:
                    # Tenemos algo de desventaja, considerar recuperarla
                    pass

            # Miramos de ir consiguiendo generadores a lo largo de la partida
            if carta.id == "constructores_amigos":
                if (self.jugadores[self.turno].constructores - self.jugadores[self.Opuesto()].constructores) < 1:
                    # Queremos tener por lo menos uno mas que el oponente
                    pass
                else:
                    pass
            if carta.id == "soldados_amigos":
                if (self.jugadores[self.turno].soldados - self.jugadores[self.Opuesto()].soldados) < 1:
                    # Queremos tener por lo menos uno mas que el oponente
                    pass
                else:
                    pass
            if carta.id == "magos_amigos":
                if (self.jugadores[self.turno].magos - self.jugadores[self.Opuesto()].magos) < 1:
                    # Queremos tener por lo menos uno mas que el oponente
                    pass
                else:
                    pass

            # Hostilidad

            # Comprobamos si matamos el enemigo
            if diccionario_cartas[carta][1][0] < 0 and diccionario_cartas[carta][1][1] == "hp_castillo":
                if (self.jugadores[self.Opuesto()].hp_castillo - diccionario_cartas[carta][1][0]) < 0:
                    # Destruimos el castillo enemigo. MVP
                    pass
                if (self.jugadores[self.Opuesto()].hp_castillo - diccionario_cartas[carta][1][0]) < 5:
                    # Practicamente destruimos el castillo enemigo.
                    pass
                if (self.jugadores[self.Opuesto()].hp_castillo - diccionario_cartas[carta][1][0]) < 15:
                    # Casi destruimos el castillo enemigo.
                    pass
                else:
                    # El castillo enemigo no peligra aún.
                    pass

            # Longevidad

            # Miramos de ir consiguiendo generadores a lo largo de la partida
            if carta.id == "constructores_amigos":
                if self.turno_jugados < 5 and self.jugadores[self.turno].constructores < 5:
                    # Urgen mas cosntructores
                    pass
                elif self.turno_jugados < 10 and self.jugadores[self.turno].constructores < 8:
                    # No urgen tanto los constructores
                    pass
                elif self.jugadores[self.turno].constructores < 8:
                    # Realemente nos dan igual los constructores
                    pass
            if carta.id == "soldados_amigos":
                if self.turno_jugados < 5 and self.jugadores[self.turno].soldados < 5:
                    # Urgen mas cosntructores
                    pass
                elif self.turno_jugados < 10 and self.jugadores[self.turno].soldados < 8:
                    # No urgen tanto los constructores
                    pass
                elif self.jugadores[self.turno].soldados < 8:
                    # Realemente nos dan igual los constructores
                    pass
            if carta.id == "magos_amigos":
                if self.turno_jugados < 5 and self.jugadores[self.turno].magos < 5:
                    # Urgen mas cosntructores
                    pass
                elif self.turno_jugados < 10 and self.jugadores[self.turno].magos < 8:
                    # No urgen tanto los constructores
                    pass
                elif self.jugadores[self.turno].magos < 8:
                    # Realemente nos dan igual los constructores
                    pass

            # Costes/Beneficios

            if (self.jugadores[self.turno].Get(diccionario_cartas[carta][0][1]) - diccionario_cartas[carta][0][0]) < 5:
                # Esta carta gasta te deja con muy poca cantidad de sus recursos
                pass
            elif (self.jugadores[self.turno].Get(diccionario_cartas[carta][0][1]) - diccionario_cartas[carta][0][
                0]) < 10:
                # Esta carta gasta te deja con poca cantidad de sus recursos
                pass
            elif (self.jugadores[self.turno].Get(diccionario_cartas[carta][0][1]) - diccionario_cartas[carta][0][
                0]) < 15:
                # Esta carta gasta te deja con un poquillo de sus recursos
                pass
            else:
                # Los recursos no peligran con estos recursos
                pass
