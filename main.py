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

mazo1 = Mazo(1)
base1 = Base([300, 300], [0.5, 0.5])
jugador1 = Jugador(base1, mazo1, 0)
jugador1.InicialziarImagenes()
jugador1.base.InicizializarBase()

mazo2 = Mazo(1)
base2 = Base([600, 300], [0.5, 0.5])
jugador2 = Jugador(base2, mazo2, 1)
jugador2.InicialziarImagenes()
jugador2.base.InicizializarBase()

narrador = Narrador(jugador1, jugador2)


# Debugeado
# slider = Slider(screen, 100, 100, 200, 40, min=0, max=100, step=1)


def mouseHandler(pos):
    narrador.DetectarClickCarta(pos)


def renderWindow():
    screen.fill(BLUE)

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
            # espera 2 segundos
            rect = (100, 100, 150, 250)
            pygame.draw.rect(screen, RED, rect)
            sleep(2)
            mazo1 = Mazo(1)
            base1 = Base([300, 300], [0.5, 0.5])
            jugador1.__init__(base1, mazo1, 0)
            jugador1.InicialziarImagenes()
            jugador1.base.InicizializarBase()
            mazo2 = Mazo(1)
            base2 = Base([600, 300], [0.5, 0.5])
            jugador2.__init__(base2, mazo2, 1)
            jugador2.InicialziarImagenes()
            jugador2.base.InicizializarBase()


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
