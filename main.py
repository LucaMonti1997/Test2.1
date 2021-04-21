import pygame
import os
import pygame_widgets
import random
from Constantes import *


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen
    pygame.quit()


# Inizializar pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))

if __name__ == "__main__":
    main()
