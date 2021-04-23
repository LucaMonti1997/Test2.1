import pygame


class Carta(object):

    def __init__(self, identificador, estado, coordenadas, dimensiones):
        self.id = identificador
        self.estado = estado
        self.coord = coordenadas
        self.dimen = dimensiones

    def Dibujar(self, pantalla, imagen):
        pantalla.blit(imagen, self.coord)
