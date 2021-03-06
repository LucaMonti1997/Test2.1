from Constantes import *


class Base(object):

    def __init__(self, coordenadas, dimensiones):
        """
        Se encarga de graficar todos los componentes de la base.

        :param coordenadas: Lista. Punto central de referencia de la base. [x, y]
        :param dimensiones: Lista. Multiplicador de ancho y alto para ajustar la escala. Valor por defecto 1.
        [mult_ancho, mult_alto]
        """
        self.coord = coordenadas
        self.dimen = dimensiones
        self.imagenesbase = {}
        self.offset = {}

    def InicizializarBase(self):
        """
        Precargamos las imagenes en un diccionario y hacemos ajustes a sus dimensiones.

        Ponemos a 0 los offsets.
        """

        self.imagenesbase = {
            "torre_central": pygame.image.load("Assets/Castillo/Centro.png").convert_alpha(),
            "torre_izquierda": pygame.image.load("Assets/Castillo/Torre_Izquierda.png").convert_alpha(),
            "torre_derecha": pygame.image.load("Assets/Castillo/Torre_Derecha.png").convert_alpha(),
            "muralla": pygame.image.load("Assets/Castillo/Muralla.png").convert_alpha(),
            "base_castillo": pygame.image.load("Assets/Castillo/Base.png").convert_alpha()
        }

        self.imagenesbase["muralla"] = pygame.transform.smoothscale(self.imagenesbase["muralla"],
                                                                    (
                                                                        int(self.imagenesbase[
                                                                                "muralla"].get_width() * 2.1),
                                                                        int(self.imagenesbase[
                                                                                "muralla"].get_height() * 0.8)))
        self.imagenesbase["base_castillo"] = pygame.transform.smoothscale(self.imagenesbase["base_castillo"],
                                                                    (
                                                                        int(self.imagenesbase[
                                                                                "base_castillo"].get_width() * 1.59),
                                                                        int(self.imagenesbase[
                                                                                "base_castillo"].get_height() * 1.2)))
        for key in self.imagenesbase:
            self.imagenesbase[key] = pygame.transform.smoothscale(self.imagenesbase[key], (
                int(self.imagenesbase[key].get_width() * self.dimen[0]),
                int(self.imagenesbase[key].get_height() * self.dimen[1])))

        self.offset = {
            "torre_central": 0,
            "torre_izquierda": 0,
            "torre_derecha": 0,
            "muralla": 0
        }

    def Dibujar(self, pantalla):
        """
        Se dibujan en la pantalla los elementos de base, teniendo en cuenta sus offsets.

        :param pantalla: Objeto pygame.display. Donde se muestran las imagenes
        """
        # Torre central

        pantalla.blit(self.imagenesbase["torre_central"],
                      [self.coord[0] - self.imagenesbase["torre_central"].get_width() / 2,
                       self.coord[1] - self.imagenesbase["torre_central"].get_height() * self.offset["torre_central"]])
        # Torre izquierda
        pantalla.blit(self.imagenesbase["torre_izquierda"],
                      [self.coord[0] - self.imagenesbase["torre_izquierda"].get_width() / 2 - 150 * self.dimen[0],
                       self.coord[1] - self.imagenesbase["torre_izquierda"].get_height() * self.offset[
                           "torre_izquierda"]])

        # Torre derecha
        pantalla.blit(self.imagenesbase["torre_derecha"],
                      [self.coord[0] - self.imagenesbase["torre_derecha"].get_width() / 2 + 150 * self.dimen[0],
                       self.coord[1] - self.imagenesbase["torre_derecha"].get_height() * self.offset["torre_derecha"]])
        # Muralla
        pantalla.blit(self.imagenesbase["muralla"],
                      [self.coord[0] - self.imagenesbase["muralla"].get_width() / 2,
                       self.coord[1] - self.imagenesbase["muralla"].get_height() * self.offset["muralla"]])

        rect = (self.coord[0] - self.imagenesbase["muralla"].get_width() / 2, self.coord[1], self.imagenesbase[
            "muralla"].get_width(), self.imagenesbase["torre_izquierda"].get_height())

        #pygame.draw.rect(pantalla, BLUE, rect)
        pantalla.blit(self.imagenesbase["base_castillo"],
                      (self.coord[0] - self.imagenesbase["muralla"].get_width() / 2, self.coord[1]))
