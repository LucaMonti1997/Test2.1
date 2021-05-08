import pygame
import os
from time import sleep
from pygame_widgets import Slider, TextBox
import random
from Constantes import *
from Carta import *
from Base import *
from Jugador import *
from Mazo import *
from Narrador import *

pygame.font.init()
# Inizializar pantalla


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('alpha')
fondo = pygame.image.load("Assets/Castillo/Mapa Fondo.png").convert_alpha()
fondo = pygame.transform.smoothscale(fondo, (int(fondo.get_width() / 1.7), int(fondo.get_height() / 1.7)))

mazo1 = Mazo(1)
base1 = Base([300, 300], [0.5, 0.5])
jugador1 = Jugador(base1, mazo1, 0)
jugador1.InicializarJugador()

mazo2 = Mazo(1)
base2 = Base([600, 300], [0.5, 0.5])
jugador2 = Jugador(base2, mazo2, 1)
jugador2.InicializarJugador()

narrador = Narrador(jugador1, jugador2)


# Debugeado
# slider = Slider(screen, 100, 100, 200, 40, min=0, max=100, step=1)


def mouseHandler(pos):
    narrador.DetectarClickCarta(pos)


def renderWindow():
    # screen.fill(BLUE)
    screen.blit(fondo, (0, 0))

    jugador1.MostrarBase(screen)
    jugador1.MostrarRecursos(screen)
    jugador2.MostrarBase(screen)
    jugador2.MostrarRecursos(screen)
    if narrador.turno == 0:
        jugador1.MostrarCartas(screen)
    else:
        jugador2.MostrarCartas(screen)
    # slider.draw()
    texto_turno = font.render("Turno jugador: " + str(narrador.turno), False, (0, 0, 0))
    screen.blit(texto_turno, [(WIDTH / 2) - 100, 25])
    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    # main loop
    run = True
    restart = True
    while run:
        # Reinicia la partida de manera bruta.
        # Considerar craer metodo a posta
        if narrador.ComprobarPartida() != 0:
            # Muestra el mensaje de victoria (aprox.) y espera 2 segundos
            rect = (100, 100, 150, 250)
            pygame.draw.rect(screen, RED, rect)
            pygame.display.update()
            sleep(2)
            # Reinicia los valores de los jugadores
            jugador1.InicializarJugador()
            jugador2.InicializarJugador()

        clock.tick(30)
        events = pygame.event.get()
        evento = pygame.event.poll()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(pygame.mouse.get_pressed())
                mouseHandler(pygame.mouse.get_pos())
        # slider.listen(events)
        #
        # jugador1.hp_castillo = (slider.getValue())
        renderWindow()
    pygame.quit()


if __name__ == "__main__":
    main()
