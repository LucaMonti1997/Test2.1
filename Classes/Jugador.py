import random
import Constantes
import pygame.font

from Mazo import *
from Constantes import *
from Carta import *


# Clase de jugador a la qual se le asignaran las siguientes funciones:
#   Generar controlar los recursos de las instancias de los jugadores
#   controlar las cartas asignadas a los jugadores


class Jugador(object):

    def __init__(self, base, mazo, identificador):
        """
        Almacena toda la información del jugador, y gestiona varias de sus interacciones.

        :param base: Objeto Base.
        :param mazo: Objeto Mazo.
        :param identificador: 0 -> Jugador1; 1 -> Jugador2
        """
        # Vida castillo y muralla
        self.hp_castillo = 0
        self.hp_muralla = 0
        # Generadores de recursos
        self.constructores = 0
        self.soldados = 0
        self.magos = 0
        # Recursos
        self.ladrillos = 0
        self.espadas = 0
        self.mana = 0
        # Cartas en mano
        self.mano = []
        self.cartas = []
        # Graficos
        self.imagenes = {}
        self.iconos = {}

        self.mazo = mazo
        self.base = base
        self.id = identificador

        self.InicializarJugador()

    def InicializarJugador(self):
        """
        Asigna valor iniciales a los atributo del jugador
        """
        self.hp_castillo = 69
        self.hp_muralla = 42

        self.constructores = 2
        self.soldados = 2
        self.magos = 2

        self.ladrillos = 5
        self.espadas = 5
        self.mana = 5

        self.InicialziarImagenes()
        self.base.InicizializarBase()
        self.mazo.InicializarMazo()
        self.InicializarMano()

    def InicializarMano(self):
        """
        Poblar la mano por primera vez
        """
        random.shuffle(self.mazo.cartas_restantes)
        x = 0
        while len(self.mano) < NUMERO_CARTAS_MANO:
            identificador_carta = self.mazo.cartas_restantes.pop()
            self.mano.append(identificador_carta)
            carta_n = Carta(identificador_carta, True, (50 + (WIDTH - 100) / 8 * x, HEIGHT - 200), (1, 1))
            self.ComprobarCarta(carta_n)
            self.cartas.append(carta_n)
            x += 1

    def InicialziarImagenes(self):
        """
        Precargamos las imagenes en un diccionario y hacemos ajustes a sus dimensiones.
        """

        self.imagenes = {
            "muralla1": [pygame.image.load("Assets/NewCards/Card renders/Muralla1_a.png").convert_alpha(),
                         pygame.image.load("Assets/NewCards/Card renders/Muralla1_b.png").convert_alpha()],
            "muralla2": [pygame.image.load("Assets/NewCards/Card renders/Muralla2_a.png").convert_alpha(),
                         pygame.image.load("Assets/NewCards/Card renders/Muralla2_b.png").convert_alpha()],
            "muralla3": [pygame.image.load("Assets/NewCards/Card renders/Muralla3_a.png").convert_alpha(),
                         pygame.image.load("Assets/NewCards/Card renders/Muralla3_b.png").convert_alpha()],
            "castillo1": [pygame.image.load("Assets/NewCards/Card renders/Castillo1_a.png").convert_alpha(),
                          pygame.image.load("Assets/NewCards/Card renders/Castillo1_b.png").convert_alpha()],
            "castillo2": [pygame.image.load("Assets/NewCards/Card renders/Castillo2_a.png").convert_alpha(),
                          pygame.image.load("Assets/NewCards/Card renders/Castillo2_b.png").convert_alpha()],
            "castillo3": [pygame.image.load("Assets/NewCards/Card renders/Castillo3_a.png").convert_alpha(),
                          pygame.image.load("Assets/NewCards/Card renders/Castillo3_b.png").convert_alpha()],
            "constructores_amigos": [
                pygame.image.load("Assets/NewCards/Card renders/ConstructoresAmigos_a.png").convert_alpha(),
                pygame.image.load("Assets/NewCards/Card renders/ConstructoresAmigos_b.png").convert_alpha()],
            "constructores_enemigos": [
                pygame.image.load("Assets/NewCards/Card renders/ConstructoresEnemigos_a.png").convert_alpha(),
                pygame.image.load("Assets/NewCards/Card renders/ConstructoresEnemigos_b.png").convert_alpha()],

            "espada1": [pygame.image.load("Assets/NewCards/Card renders/Espada1_a.png").convert_alpha(),
                        pygame.image.load("Assets/NewCards/Card renders/Espada1_b.png").convert_alpha()],
            "espada2": [pygame.image.load("Assets/NewCards/Card renders/Espada2_a.png").convert_alpha(),
                        pygame.image.load("Assets/NewCards/Card renders/Espada2_b.png").convert_alpha()],
            "espada3": [pygame.image.load("Assets/NewCards/Card renders/Espada3_a.png").convert_alpha(),
                        pygame.image.load("Assets/NewCards/Card renders/Espada3_b.png").convert_alpha()],
            "arco1": [pygame.image.load("Assets/NewCards/Card renders/Arco1_a.png").convert_alpha(),
                      pygame.image.load("Assets/NewCards/Card renders/Arco1_b.png").convert_alpha()],
            "arco2": [pygame.image.load("Assets/NewCards/Card renders/Arco2_a.png").convert_alpha(),
                      pygame.image.load("Assets/NewCards/Card renders/Arco2_b.png").convert_alpha()],
            "arco3": [pygame.image.load("Assets/NewCards/Card renders/Arco3_a.png").convert_alpha(),
                      pygame.image.load("Assets/NewCards/Card renders/Arco3_b.png").convert_alpha()],
            "soldados_amigos": [
                pygame.image.load("Assets/NewCards/Card renders/SoldadosAmigos_a.png").convert_alpha(),
                pygame.image.load("Assets/NewCards/Card renders/SoldadosAmigos_b.png").convert_alpha()],
            "soldados_enemigos": [
                pygame.image.load("Assets/NewCards/Card renders/SoldadosEnemigos_a.png").convert_alpha(),
                pygame.image.load("Assets/NewCards/Card renders/SoldadosEnemigos_b.png").convert_alpha()],

            "magia1": [pygame.image.load("Assets/NewCards/Card renders/Magia1_a.png").convert_alpha(),
                       pygame.image.load("Assets/NewCards/Card renders/Magia1_b.png").convert_alpha()],
            "magia2": [pygame.image.load("Assets/NewCards/Card renders/Magia2_a.png").convert_alpha(),
                       pygame.image.load("Assets/NewCards/Card renders/Magia2_b.png").convert_alpha()],
            "magia3": [pygame.image.load("Assets/NewCards/Card renders/Magia3_a.png").convert_alpha(),
                       pygame.image.load("Assets/NewCards/Card renders/Magia3_b.png").convert_alpha()],
            "regenerar1": [pygame.image.load("Assets/NewCards/Card renders/Regenerar1_a.png").convert_alpha(),
                           pygame.image.load("Assets/NewCards/Card renders/Regenerar1_b.png").convert_alpha()],
            "regenerar2": [pygame.image.load("Assets/NewCards/Card renders/Regenerar2_a.png").convert_alpha(),
                           pygame.image.load("Assets/NewCards/Card renders/Regenerar2_b.png").convert_alpha()],
            "regenerar3": [pygame.image.load("Assets/NewCards/Card renders/Regenerar3_a.png").convert_alpha(),
                           pygame.image.load("Assets/NewCards/Card renders/Regenerar3_b.png").convert_alpha()],
            "conjurar_ladrillos": [
                pygame.image.load("Assets/NewCards/Card renders/ConjurarLadrillos_a.png").convert_alpha(),
                pygame.image.load("Assets/NewCards/Card renders/ConjurarLadrillos_b.png").convert_alpha()],
            "conjurar_espadas": [
                pygame.image.load("Assets/NewCards/Card renders/ConjurarEspadas_a.png").convert_alpha(),
                pygame.image.load("Assets/NewCards/Card renders/ConjurarEspadas_b.png").convert_alpha()],
            "conjurar_mana": [
                pygame.image.load("Assets/NewCards/Card renders/ConjurarMana_a.png").convert_alpha(),
                pygame.image.load("Assets/NewCards/Card renders/ConjurarMana_b.png").convert_alpha()],
            "magos_amigos": [
                pygame.image.load("Assets/NewCards/Card renders/MagosAmigos_a.png").convert_alpha(),
                pygame.image.load("Assets/NewCards/Card renders/MagosAmigos_b.png").convert_alpha()],
            "magos_enemigos": [
                pygame.image.load("Assets/NewCards/Card renders/MagosEnemigos_a.png").convert_alpha(),
                pygame.image.load("Assets/NewCards/Card renders/MagosEnemigos_b.png").convert_alpha()],

            "recurso_constructores": [
                pygame.image.load("Assets/NewCards/Card renders/Recursos/Constructores_a.png").convert_alpha(),
                pygame.image.load("Assets/NewCards/Card renders/Recursos/Constructores_b.png").convert_alpha()],
            "recurso_soldados": [
                pygame.image.load("Assets/NewCards/Card renders/Recursos/Soldados_a.png").convert_alpha(),
                pygame.image.load("Assets/NewCards/Card renders/Recursos/Soldados_b.png").convert_alpha()],
            "recurso_magia": [
                pygame.image.load("Assets/NewCards/Card renders/Recursos/Magia_a.png").convert_alpha(),
                pygame.image.load("Assets/NewCards/Card renders/Recursos/Magia_b.png").convert_alpha()]
        }
        self.iconos = {

            "escudo": pygame.image.load("Assets/Iconos/escudo.png").convert_alpha(),
            "corazon": pygame.image.load("Assets/Iconos/Corazon.png").convert_alpha(),
        }

        # modificamos las imagenes para que quepan en pantalla

        for key in self.imagenes:
            for imagen in self.imagenes[key]:
                imagen = pygame.transform.smoothscale(imagen,
                                                      (int(imagen.get_width() / 1), int(imagen.get_height() / 1)))
        for key in self.iconos:
            ancho = self.iconos[key].get_width()
            nuevo_ancho = int(WIDTH / 25)
            alto = self.iconos[key].get_height()
            nuevo_alto = int((alto * nuevo_ancho) / ancho)
            self.iconos[key] = pygame.transform.smoothscale(self.iconos[key], (nuevo_ancho, nuevo_alto))

    def CogerUnaCarta(self):
        """
        Coge cartas mientras tenga sitio en la mano
        """
        self.mazo.ComprobarMazo()
        self.mano.append(self.mazo.cartas_restantes.pop())
        i = 0
        while i < NUMERO_CARTAS_MANO:
            self.cartas[i].id = self.mano[i]
            self.ComprobarCarta(self.cartas[i])
            i += 1

    def ComprobarCarta(self, carta):
        """
        Comprueba si una carta se puede jugar, y modifica su atributo estado.

        :param carta: Objeto Carta. Carta que se comprueba
        """
        if self.Get(diccionario_cartas[carta.id][0][1]) >= diccionario_cartas[carta.id][0][0]:
            carta.estado = True
        else:
            carta.estado = False

    def ComprobarTodasCartas(self):
        """
        Llama ComprobarCarta para todas las cartas
        """

        for carta in self.cartas:
            self.ComprobarCarta(carta)

    def MostrarCartas(self, pantalla):
        """
        Se llama el metodo Dibujar de cada carta para mostrarla en pantalla.

        :param pantalla: Objeto pygame.display. Donde se muestran las imagenes
        """

        # dibujamos las cartas con la imagen correspondiente segun el id de la carta
        for carta in self.cartas:
            carta.Dibujar(pantalla, self.imagenes[carta.id])

    def MostrarRecursos(self, pantalla):
        """
        Se dibujan los recursos en pantalla.

        :param pantalla: Objeto pygame.display. Donde se muestran las imagenes
        """
        # Ancho y alto base de los rectangulos
        ancho = self.imagenes["recurso_magia"][0].get_width()
        alto = self.imagenes["recurso_magia"][0].get_height()
        gap = 1.2

        texto_constructores = Constantes.font_recursos.render(str(self.constructores), False, (0, 0, 0))
        texto_ladrillos = Constantes.font_recursos.render(str(self.ladrillos), False, (0, 0, 0))
        texto_soldados = Constantes.font_recursos.render(str(self.soldados), False, (0, 0, 0))
        texto_espadas = Constantes.font_recursos.render(str(self.espadas), False, (0, 0, 0))
        texto_magos = Constantes.font_recursos.render(str(self.magos), False, (0, 0, 0))
        texto_mana = Constantes.font_recursos.render(str(self.mana), False, (0, 0, 0))

        # Costructores y ladrillos
        pantalla.blit(self.imagenes["recurso_constructores"][self.id], [(WIDTH / 25) * abs(self.id - 1) +
                                                                        (WIDTH - (WIDTH / 25) - ancho) * self.id,
                                                                        (HEIGHT / 20) + alto * gap * 0])
        espesor = font_recursos.size(str(self.constructores))
        pantalla.blit(texto_constructores, [(((WIDTH / 25) + ancho / 4) * abs(self.id - 1) +
                                             (WIDTH - (WIDTH / 25) - (ancho / 4)) * self.id) - espesor[0] / 2,
                                            (HEIGHT / 20) + alto / 5 + alto * gap * 0])
        espesor = font_recursos.size(str(self.ladrillos))
        pantalla.blit(texto_ladrillos, [(((WIDTH / 25) + ancho * 3 / 4) * abs(self.id - 1) +
                                         (WIDTH - (WIDTH / 25) - (ancho * 3 / 4)) * self.id) - espesor[0] / 2,
                                        (HEIGHT / 20) + alto / 5 + alto * gap * 0])

        # Soldados y espadas
        pantalla.blit(self.imagenes["recurso_soldados"][self.id], [(WIDTH / 25) * abs(self.id - 1) +
                                                                   (WIDTH - (WIDTH / 25) - ancho) * self.id,
                                                                   (HEIGHT / 20) + alto * gap])
        espesor = font_recursos.size(str(self.soldados))
        pantalla.blit(texto_constructores, [(((WIDTH / 25) + ancho / 4) * abs(self.id - 1) +
                                             (WIDTH - (WIDTH / 25) - (ancho / 4)) * self.id) - espesor[0] / 2,
                                            (HEIGHT / 20) + alto / 5 + alto * gap * 1])
        espesor = font_recursos.size(str(self.espadas))
        pantalla.blit(texto_ladrillos, [(((WIDTH / 25) + ancho * 3 / 4) * abs(self.id - 1) +
                                         (WIDTH - (WIDTH / 25) - (ancho * 3 / 4)) * self.id) - espesor[0] / 2,
                                        (HEIGHT / 20) + alto / 5 + alto * gap * 1])

        # Magos
        pantalla.blit(self.imagenes["recurso_magia"][self.id], [(WIDTH / 25) * abs(self.id - 1) +
                                                                (WIDTH - (WIDTH / 25) - ancho) * self.id,
                                                                (HEIGHT / 20) + alto * gap * 2])
        espesor = font_recursos.size(str(self.magos))
        pantalla.blit(texto_magos, [(((WIDTH / 25) + ancho / 4) * abs(self.id - 1) +
                                     (WIDTH - (WIDTH / 25) - (ancho / 4)) * self.id) - espesor[0] / 2,
                                    (HEIGHT / 20) + alto / 5 + alto * gap * 2])
        espesor = font_recursos.size(str(self.mana))
        pantalla.blit(texto_mana, [(((WIDTH / 25) + ancho * 3 / 4) * abs(self.id - 1) +
                                    (WIDTH - (WIDTH / 25) - (ancho * 3 / 4)) * self.id) - espesor[0] / 2,
                                   (HEIGHT / 20) + alto / 5 + alto * gap * 2])

    def MostrarBase(self, pantalla):
        """
        Primero se calculan los offsets de los atributos de base, luego se llama a base.Dibujar para que se muestre
        en pantalla

        :param pantalla: Objeto pygame.display. Donde se muestran las imagenes
        """
        if self.hp_castillo < 40:
            self.base.offset["torre_izquierda"] = 0
            self.base.offset["torre_derecha"] = 0
            self.base.offset["torre_central"] = self.hp_castillo / 40
        elif self.hp_castillo < 70:
            self.base.offset["torre_izquierda"] = (self.hp_castillo - 40) / 30
            self.base.offset["torre_derecha"] = 0
            self.base.offset["torre_central"] = 1
        else:
            self.base.offset["torre_izquierda"] = 1
            self.base.offset["torre_derecha"] = (self.hp_castillo - 70) / 30
            self.base.offset["torre_central"] = 1

        self.base.offset["muralla"] = self.hp_muralla / 100

        # print(self.base.offset["torre_izquierda"], self.base.offset["torre_central"],self.base.offset["torre_derecha"])

        self.base.Dibujar(pantalla)

        texto_hp_castillo = Constantes.font_recursos.render(str(self.hp_castillo), False, (0, 0, 0))
        texto_hp_muralla = Constantes.font_recursos.render(str(self.hp_muralla), False, (0, 0, 0))
        pantalla.blit(texto_hp_castillo, [self.base.coord[0] - 75, self.base.coord[1] - 200])
        pantalla.blit(self.iconos["corazon"], [self.base.coord[0] - 65, self.base.coord[1] - 209])
        pantalla.blit(texto_hp_muralla, [self.base.coord[0] + 25, self.base.coord[1] - 200])
        pantalla.blit(self.iconos["escudo"], [self.base.coord[0] + 50, self.base.coord[1] - 213])

    def Set(self, attr, value):
        setattr(self, attr, value)

    def Get(self, attr):
        return getattr(self, attr)
