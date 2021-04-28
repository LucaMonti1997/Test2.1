import pygame


class Base(object):

    def __init__(self, coordenadas, dimensiones):
        self.coord = coordenadas
        self.dimen = dimensiones
        self.imagenesbase = {}

    def InicizializarBase(self):
        self.imagenesbase = {
            "torre_central": pygame.image.load("Assets/TestAssets/Castillo1/TorreSencilla1.png").convert_alpha(),
            "torre_lateral": pygame.image.load("Assets/TestAssets/Castillo1/TorreSencilla1.png").convert_alpha(),
            "muralla": pygame.image.load("Assets/TestAssets/Castillo1/Muralla1.png").convert_alpha()
        }
        self.imagenesbase["torre_central"] = pygame.transform.smoothscale(self.imagenesbase["torre_central"],
                                                                          (int(self.imagenesbase[
                                                                                   "torre_central"].get_width() * 1.2),
                                                                           int(self.imagenesbase[
                                                                                   "torre_central"].get_height() * 1.2)))
        self.imagenesbase["muralla"] = pygame.transform.smoothscale(self.imagenesbase["muralla"],
                                                                    (
                                                                        int(self.imagenesbase[
                                                                                "muralla"].get_width() * 0.8),
                                                                        int(self.imagenesbase[
                                                                                "muralla"].get_height() * 0.8)))

    def Dibujar(self, pantalla):
        # Torre central

        pantalla.blit(self.imagenesbase["torre_central"], [int(self.coord[0] + self.dimen[0] / 2), 200])
        # Torre izquierda
        pantalla.blit(self.imagenesbase["torre_lateral"], [self.coord[0], 200])
        pantalla.blit(self.imagenesbase["muralla"],
                      [int(self.coord[0] + self.dimen[0] / 2), 200])
