class Carta(object):

    def __init__(self, identificador, estado, coordenadas, dimensiones):
        """
        Almcena las propriedades y ubicación de la carta.

        :param identificador: String. Texto que representa el tipo de carta.
        :param estado: Boolean. Indica si la carta es jugable o no.
        :param coordenadas: Lista. Punto central de referencia de la base. [x, y]
        :param dimensiones: Lista. Dimensiones de la carta. [ancho, alto]
        """

        self.id = identificador
        self.estado = estado
        self.coord = coordenadas
        self.dimen = dimensiones

    def Dibujar(self, pantalla, imagen):
        """
        Se dibuja la carta en pantalla.

        :param pantalla: Objeto pygame.display. Donde se muestran las imagenes
        :param imagen: Lista con Objetos pygame.image. Imagen que se dibujará
        """
        if self.estado:
            pantalla.blit(imagen[0], self.coord)
        else:
            pantalla.blit(imagen[1], self.coord)

    def MouseOver(self, pos):
        """
        Comprueba si las posición especificada está por encima suyo

        :param pos: Posición a comprobar
        """
        if self.coord[0] < pos[0] < self.coord[0] + self.dimen[0] and \
                self.coord[1] < pos[1] < self.coord[1] + self.dimen[1]:
            return True
        else:
            return False
