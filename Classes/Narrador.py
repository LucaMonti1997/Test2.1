import random


class Narrador(object):
    def __init__(self):
        """
        Se encarga de "dirigir" la partida. Reparte las cartas, gestiona los turnos, generación de recursos, eventos
        aleatorios, etc.
        """
        self.turno_jugador1 = False
        self.turno_jugador2 = False
        self.turno_acabado = False
        self.jugadores = ''

    def IniciarPartida(self):
        self.turno_jugador1 = random.choice([True, False])
        self.turno_jugador2 = not self.turno_jugador1
        self.turno_acabado = True  # Indica si el narrador quiere cambiar turno

    def CambiarTurno(self):
        self.turno_jugador1 = not self.turno_jugador1
        self.turno_jugador2 = not self.turno_jugador1
        self.turno_acabado = False
