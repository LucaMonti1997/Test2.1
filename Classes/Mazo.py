class Mazo(object):

    def __init__(self, tipo):
        """
        Contiene los id's de las cartas restante en el mazo de cada jugador. También posé un copia del mazo completo
        para cuando el mazo se agota.

        :param tipo: Numero. Tipo de mazo. Distintos mazos estan compuesto por diferentes combinaciones de cartas.
        """
        self.mazo_1_completo = ["muralla1", "muralla2", "muralla3", "castillo1", "castillo2", "castillo3", "arco1",
                                "arco2", "arco3", "espada1", "espada2", "espada3", "magia1", "magia2", "magia3",
                                "regenerar1", "regenerar2", "regenerar3", "conjurar_ladrillos", "conjurar_espadas",
                                "conjurar_mana"]
        self.cartas_restantes = []
        self.tipo = tipo

    def InicializarMazo(self):
        if self.tipo == 1:
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
