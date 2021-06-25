from Boton import *
from Constantes import *


class Ventana:
    def __init__(self, pantalla, identificador, dimensiones=None):
        """
        Ventana que se muestran en pantalla. Puede ser el menu principal, el ventana_juego en si, opciones, etc.

        :param pantalla: Objeto pygame.display. Donde se mostrará la ventana.
        :param identificador: String. Identifica que ventana es.
        :param dimensiones: Lista. Dimensiones de la ventana. Por defecto coincide con el display. [ancho, alto]
        """
        self.pantalla = pantalla
        self.id = identificador
        if dimensiones is None:
            self.dimen = [WIDTH, HEIGHT]
        else:
            self.dimen = dimensiones

        # El atributo .activa decide si la ventana será dibujada cuando se llame renderWindow.
        # El atributo .focus decide si se puede interectuar con la ventana.
        # e.g. La ventana del ventana de juego está activa, pero la del menú de opciones también, y es la segunda quien
        # tiene el focus, por lo tanto de fondo se ve el ventana de juego, pero por encima está el menu de opciones
        # con el cual se puede interactuar
        self.activa = False
        self.focus = False

        self.imagenes = {}
        self.lista_botones = []  # Lista con los botones que está ventana posé
        self.botones = []  # Objetos Boton

    def InicializarInterfaz(self):
        self.botones = []
        i = 0

        ancho = self.dimen[0]
        alto = self.dimen[1]
        ancho_b = self.imagenes["jugar"].get_width()
        alto_b = self.imagenes["jugar"].get_height()
        x = (WIDTH - ancho) / 2
        y = (HEIGHT - alto) / 2

        if self.id == "menu_principal":
            self.lista_botones = ["jugar", "opciones", "salir"]
            while len(self.botones) < 3:
                boton_n = Boton([(ancho / 2) + x - ancho_b / 2,
                                 y - (alto_b / 2) + (alto / 5) + ((alto - (alto * 2 / 5)) / 2) * i],
                                [ancho_b, alto_b],
                                self.lista_botones[i])
                self.botones.append(boton_n)
                i += 1
        elif self.id == "menu_opciones":
            self.lista_botones = ["cargar", "guardar"]
            while len(self.botones) < 2:
                boton_n = Boton([(ancho / 2) + x - ancho_b / 2,
                                 y - (alto_b / 2) + (alto / 5) + ((alto - (alto * 2 / 5)) / 1) * i],
                                [ancho_b, alto_b],
                                self.lista_botones[i])
                self.botones.append(boton_n)
                i += 1

    def InicializarImagenes(self):
        self.imagenes = {
            "jugar": pygame.image.load("Assets/NewCards/Button renders/Jugar.png").convert_alpha(),
            "opciones": pygame.image.load("Assets/NewCards/Button renders/Opciones.png").convert_alpha(),
            "salir": pygame.image.load("Assets/NewCards/Button renders/Salir.png").convert_alpha(),
            "cargar": pygame.image.load("Assets/NewCards/Button renders/Cargar.png").convert_alpha(),
            "guardar": pygame.image.load("Assets/NewCards/Button renders/Guardar.png").convert_alpha()
        }

        for key in self.imagenes:
            self.imagenes[key] = pygame.transform.smoothscale(self.imagenes[key],
                                                              (int(self.dimen[0] / 2), int(self.dimen[1] / 3)))

    def MostrarBotones(self):
        x = 0
        for boton in self.botones:
            boton.Dibujar(self.pantalla, self.imagenes[self.lista_botones[x]])
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
