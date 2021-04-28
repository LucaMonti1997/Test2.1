import pygame


class Base(object):

    def __init__(self, coordenadas, dimensiones):
        self.coord = coordenadas
        self.dimen = dimensiones
        self.imagenesbase = {}

    def InicizializarBase(self):
        self.imagenesbase = {

            "torre_central": pygame.image.load("Assets/Castillo/Centro.png").convert_alpha(),
            "torre_izquierda": pygame.image.load("Assets/Castillo/Torre_Izquierda.png").convert_alpha(),
            "torre_derecha": pygame.image.load("Assets/Castillo/Torre_Derecha.png").convert_alpha(),
            "muralla": pygame.image.load("Assets/Castillo/Muralla.png").convert_alpha()
        }

        self.imagenesbase["muralla"] = pygame.transform.smoothscale(self.imagenesbase["muralla"],
                                                                    (
                                                                        int(self.imagenesbase[
                                                                                "muralla"].get_width() * 2),
                                                                        int(self.imagenesbase[
                                                                                "muralla"].get_height() * 0.8)))

        for key in self.imagenesbase:
            self.imagenesbase[key] = pygame.transform.smoothscale(self.imagenesbase[key], (
                int(self.imagenesbase[key].get_width() * self.dimen[0]),
                int(self.imagenesbase[key].get_height() * self.dimen[1])))

    def Dibujar(self, pantalla):
        # Torre central

        pantalla.blit(self.imagenesbase["torre_central"],
                      [self.coord[0] - self.imagenesbase["torre_central"].get_width() / 2,
                       self.coord[1] - self.imagenesbase["torre_central"].get_height()])
        # Torre izquierda
        pantalla.blit(self.imagenesbase["torre_izquierda"],
                      [self.coord[0] - self.imagenesbase["torre_izquierda"].get_width() / 2 - 150 * self.dimen[0],
                       self.coord[1] - self.imagenesbase["torre_izquierda"].get_height()])

        # Torre derecha
        pantalla.blit(self.imagenesbase["torre_derecha"],
                      [self.coord[0] - self.imagenesbase["torre_derecha"].get_width() / 2 + 150 * self.dimen[0],
                       self.coord[1] - self.imagenesbase["torre_derecha"].get_height()])
        # Muralla
        pantalla.blit(self.imagenesbase["muralla"],
                      [self.coord[0] - self.imagenesbase["muralla"].get_width() / 2,
                       self.coord[1] - self.imagenesbase["muralla"].get_height()])

        rect = (self.coord[0], self.coord[1], 5, 5)

        pygame.draw.rect(pantalla, (0, 0, 0), rect)
