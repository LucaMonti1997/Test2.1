import random


class Narrador(object):
    def __init__(self):
        """
        Se encarga de "dirigir" la partida. Reparte las cartas, gestiona los turnos, generación de recursos, eventos
        aleatorios, etc.
        """
        self.player1_turn = random.choice([True, False])
        self.player2_turn = not self.player1_turn
        self.turno_acabado = True  # Indica si el narrador quiere cambiar turno

    def CambiarTurno(self):
        self.player1_turn = not self.player1_turn
        self.player2_turn = not self.player1_turn
        self.turno_acabado = False
