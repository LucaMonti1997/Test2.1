import random


class Narrador(object):
    def __init__(self, jugador1, jugador2):
        """
        Se encarga de "dirigir" la partida. Reparte las cartas, gestiona los turnos, generación de recursos, eventos
        aleatorios, etc.
        """
        self.turno_jugador1 = False
        self.turno_jugador2 = False
        self.turno_acabado = False
        self.jugadores = [jugador1, jugador2]

    def IniciarPartida(self):
        """
        Escoje aleatoramente quie empieza.
        """
        self.turno_jugador1 = random.choice([True, False])
        self.turno_jugador2 = not self.turno_jugador1
        self.turno_acabado = True  # Indica si el narrador quiere cambiar turno

    def CambiarTurno(self):
        """
        Cambia el turno de un jugador al otro.
        """
        self.turno_jugador1 = not self.turno_jugador1
        self.turno_jugador2 = not self.turno_jugador1
        self.turno_acabado = False

    def ComprobarPartida(self):
        """
        Comprueba si la partida ha acabado.

        0 -> Partida no acabada

        1 -> Jugador1.hp == 0

        2 -> Jugador1.hp == 100

        3 -> Jugador2.hp == 0

        4 -> Jugador2.hp == 100
        """
        if self.jugadores[0].hp <= 0:
            return 1
        elif self.jugadores[0].hp >= 100:
            return 2
        elif self.jugadores[1].hp <= 0:
            return 3
        elif self.jugadores[1].hp >= 100:
            return 4
        else:
            return 0

    def GenerarRecursos(self):
        """
        Genera los recursos que corresponden.
        """
        if self.turno_jugador1:
            self.jugadores[0].ladrillos += self.jugadores[0].constructores
            self.jugadores[0].armas += self.jugadores[0].soldados
            self.jugadores[0].mana += self.jugadores[0].magos
        else:
            self.jugadores[1].ladrillos += self.jugadores[1].constructores
            self.jugadores[1].armas += self.jugadores[1].soldados
            self.jugadores[1].mana += self.jugadores[1].magos
