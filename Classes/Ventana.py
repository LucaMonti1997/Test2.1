import pygame
from Constantes import *
from Boton import *


class Ventana:
    def __init__(self, pantalla, identificador, dimen=None):
        """
        Ventana que se muestran en pantalla. Puede ser el menu principal, el ventana_juego en si, opciones, etc.

        :param pantalla: Objeto pygame.display. Donde se mostrará la ventana.
        :param identificador: String. Identifica que ventana es.
        :param dimen: Lista. Dimensiones de la ventana. Por defecto coincide con el display. [ancho, alto]
        """
        self.pantalla = pantalla
        self.id = identificador
        if dimen is None:
            self.dimen = [WIDTH, HEIGHT]

        # El atributo .activa decide si la ventana será dibujada cuando se llame renderWindow.
        # El atributo .focus decide si se puede interectuar con la ventana.
        # e.g. La ventana del ventana de juego está activa, pero la del menú de opciones también, y es la segunda quien
        # tiene el focus, por lo tanto de fondo se ve el ventana de juego, pero por encima está el menu de opciones
        # con el cual se puede interactuar
        self.activa = False
        self.focus = False

        self.imagenes = {}
        self.botones = []

    def InicializarInterfaz(self):
        self.botones = []
        x = 0
        if self.id == "menu_principal":
            while len(self.botones) < 3:
                boton_n = Boton([WIDTH / 2, 50 + (HEIGHT - 100) / 4 * x], [WIDTH / 6, HEIGHT / 8], x)
                self.botones.append(boton_n)
                x += 1

    def InicializarImagenes(self):
        self.imagenes = {
            0: pygame.image.load("Assets/NewCards/Button renders/Jugar.png").convert_alpha(),
            1: pygame.image.load("Assets/NewCards/Button renders/Opciones.png").convert_alpha(),
            2: pygame.image.load("Assets/NewCards/Button renders/Salir.png").convert_alpha()
        }

        for key in self.imagenes:
            imagen = pygame.transform.smoothscale(self.imagenes[key], (int(WIDTH / 6), int(HEIGHT / 8)))

    def MostrarBotones(self):
        x = 0
        for boton in self.botones:
            boton.Dibujar(self.pantalla, self.imagenes[x])
            x += 1

    def DetectarBoton(self, pos):
        for boton in self.botones:
            if boton.MouseOver(pos):
                return boton.id
        print("nada")
        return -1

    def Activar(self):
        """
        Activa la ventana como principal
        """
        self.activa = True
        self.focus = True

    def Desactivar(self):
        """
        Desactiva la ventana por completo
        """
        self.activa = False
        self.focus = False

    def GainFocus(self):
        """
        Otorga a esta ventana el focus, si ya está activa
        """
        if self.activa:
            self.focus = True
        else:
            print("Ventana desactivada quería focus")

    def LoseFocus(self):
        """
        Cancela el focus de esta ventana sin desactivarla
        """
        self.focus = False