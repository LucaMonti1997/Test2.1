from Constantes import diccionario_mazos
class Mazo(object):

    def __init__(self, tipo):
        """
        Contiene los id's de las cartas restante en el mazo de cada jugador. También posé un copia del mazo completo
        para cuando el mazo se agota.

        :param tipo: Numero. Tipo de mazo. Distintos mazos estan compuesto por diferentes combinaciones de cartas.
        """
        self.cartas_restantes = []
        self.tipo = tipo

    def InicializarMazo(self):
        """
        Inicializa el mazo
        """
        self.cartas_restantes = diccionario_mazos[self.tipo].copy()

    def ComprobarMazo(self):
        """
        Comprueba si hay cartas restantes en el mazo. En caso negativo, accede a la copia completa para recargarlas.
        """
        if len(self.cartas_restantes) == 0:
            self.cartas_restantes = diccionario_mazos[self.tipo].copy()
