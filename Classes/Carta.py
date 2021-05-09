import pygame


class Carta(object):

    def __init__(self, identificador, estado, coordenadas, dimensiones):
        """
        Almcena las propriedades y ubicación de la carta.

        :param identificador: String. Texto que representa el tipo de carta.
        :param estado: Boolean. Indica si la carta es jugable o no.
        :param coordenadas: Lista. Punto central de referencia de la base. [x, y]
        :param dimensiones: Lista. Multiplicador de ancho y alto para ajustar la escala. Valor por defecto 1.
        [mult_ancho, mult_alto]
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
