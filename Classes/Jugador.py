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


    def CrearMano(self):
        pass
