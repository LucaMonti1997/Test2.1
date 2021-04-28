class Estructura:
    def __init__(self, identificador, coordenadas, dimensiones):
        """
        :param identificador: Identificador de la estructura
        :param coordenadas: Coordenadas de la estructura
        :param dimensiones: Dimensiones de la estructua
        """
        self.id = identificador
        self.coord = coordenadas
        self.dimen = dimensiones

    def Dibujar(self, pantalla, imagen):
        pantalla.blit(imagen, self.coord)
