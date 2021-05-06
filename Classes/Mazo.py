class Mazo(object):

    def __init__(self, tipo):
        """
        Contiene los id's de las cartas restante en el mazo de cada jugador. También posé un copia del mazo completo
        para cuando el mazo se agota.

        :param tipo: Numero. Tipo de mazo. Distintos mazos estan compuesto por diferentes combinaciones de cartas.
        """
        self.mazo_1_completo = ["muralla", "muralla", "muralla", "muralla", "muralla", "espada", "espada", "espada",
                                "espada"]
        self.cartas_restantes = []
        if tipo == 1:
            for item in self.mazo_1_completo:
                self.cartas_restantes.append(item)
        # self.cartas_restantes = self.mazo_1_completo

    def ComprobarMazo(self):
        """
        Comprueba si hay cartas restantes en el mazo. En caso negativo, accede a la copia completa para recargarlas.
        """
        if len(self.cartas_restantes) == 0:
            # Vamos item a item del mazo original porque si no al "asignar" el mazo original, al hacer pops también se
            # modificaba el mazo original
            for item in self.mazo_1_completo:
                self.cartas_restantes.append(item)
