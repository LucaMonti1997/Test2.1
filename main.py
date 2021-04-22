import pygame
import os
import pygame_widgets
import random
from Constantes import *

# Inizializar pantalla

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('alpha')

# Contiene el diccionario completo de las cartas del juego
diccionario_cartas = {
    "Muralla": [[5, "ladrillos"], [10, "hp_muralla"], ["Muralla +10"]],
    "Defensa": [[5, "ladrillos"], [10, "hp_muralla"], ["Muralla +10"]]
}


def renderWindow():
    screen.fill((0, 0, 125))
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
