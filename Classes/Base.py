import pygame


class Base(object):

    def __init__(self, coordenadas, dimensiones):
        self.coordenadas = coordenadas
        self.dimensiones = dimensiones
        self.imagenesbase = {}

    def InicizializarBase(self):
        self.imagenesbase = {
            "torre": pygame.image.load("Assets/TestAssets/Castillo1/TorreSencilla1.png").convert_alpha(),
            "muralla": pygame.image.load("Assets/TestAssets/Castillo1/Muralla1.png").convert_alpha()
            }

        for key in self.imagenesbase:
            self.imagenesbase[key] = pygame.transform.smoothscale(self.imagenesbase[key], (
                int(self.imagenesbase[key].get_width() * 2), int(self.imagenesbase[key].get_height() * 2)))

    def Dibujar(self, pantalla):
        pantalla.blit(self.imagenesbase["torre"], [200, 200])
        pantalla.blit(self.imagenesbase["muralla"], [200, 200])
