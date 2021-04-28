import pygame
import os
from pygame_widgets import Slider
import random
from Constantes import *
from Carta import *
from Jugador import *
from Mazo import *

# Inizializar pantalla

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('alpha')
mazo1 = Mazo(1)
jugador1 = Jugador([300, 300], [0.5, 0.5], mazo1)
jugador1.InicialziarImagenes()
jugador1.base.InicizializarBase()
mazo2 = Mazo(1)
jugador2 = Jugador([600, 300], [0.5, 0.5], mazo2)
jugador2.InicialziarImagenes()
jugador2.base.InicizializarBase()


# Debugeado
# slider = Slider(screen, 100, 100, 200, 40, min=0, max=100, step=1)


def renderWindow():
    screen.fill(BLUE)

    jugador1.MostrarBase(screen)
    jugador2.MostrarBase(screen)
    jugador1.MostrarCartas(screen)
    # slider.draw()
    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    # main loop
    run = True
    while run:
        clock.tick(30)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
        # slider.listen(events)
        #
        # jugador1.hp_castillo = (slider.getValue())
        renderWindow()
    pygame.quit()


if __name__ == "__main__":
    main()
