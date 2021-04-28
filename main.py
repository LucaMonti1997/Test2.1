import pygame
import os
import pygame_widgets
import random
from Constantes import *
from Carta import *
from Jugador import *

# Inizializar pantalla

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('alpha')
jugador1 = Jugador()
jugador1.InicialziarImagenes()
jugador1.base.InicizializarBase()


def renderWindow():
    screen.fill((0, 0, 125))
    jugador1.MostrarCartas(screen)
    jugador1.base.Dibujar(screen)
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
        renderWindow()
    pygame.quit()


if __name__ == "__main__":
    main()
