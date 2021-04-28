import pygame

WIDTH = 900
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Contiene el diccionario completo de las cartas del juego
diccionario_cartas = {
    "muralla": [[5, "ladrillos"], [10, "hp_muralla"], ["Muralla +10"]],
    "defensa": [[5, "ladrillos"], [10, "hp_muralla"], ["Muralla +10"]]
}


NUMERO_CARTAS_MANO = 8
