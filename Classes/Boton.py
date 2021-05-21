import pygame


class Boton(object):
    def __init__(self, coord, dimen, identificador):
        """
        Boton interactuable

        :param coord: Coordenadas. [x, y]
        :param dimen: Dimensiones. [ancho, alto]
        :param identificador: Int. Identifica que boton es.
        """

        self.coord = coord
        self.dimen = dimen
        self.id = identificador

    def Dibujar(self, pantalla, imagen):
        """
        Se dibuja la carta en pantalla.

        :param pantalla: Objeto pygame.display. Donde se muestran las imagenes
        :param imagen: Imagen que se dibujará
        """
        pantalla.blit(imagen, self.coord)

    def MouseOver(self, pos):
        """
        Comprueba si las posición especificada está por encima suyo

        :param pos: Posición a comprobar
        """
        if self.coord[0] < pos[0] < self.coord[0] + self.dimen[0] * 2 and \
                self.coord[1] < pos[1] < self.coord[1] + self.dimen[1] * 2:
            return True
        else:
            return False
