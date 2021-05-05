import pygame

# Ancho y alto de la ventana de juego
WIDTH = 900
HEIGHT = 600

# Valores RGB de varios colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Contiene el diccionario completo de las cartas del juego
diccionario_cartas = {
    "muralla": [[5, "ladrillos"], [10, "hp_muralla"], ["Muralla +10"]],
    "defensa": [[5, "ladrillos"], [10, "hp_muralla"], ["Muralla +10"]],
    "espada": [[5, "espadas"], [-10, "hp_muralla"], ["Muralla -10"]]
}

# Numero de cartas que se tienen en mano a la vez
NUMERO_CARTAS_MANO = 8

# Fonts usados en el juego
pygame.font.init()
font = pygame.font.SysFont('Arial', 30)
font_recursos = pygame.font.SysFont('Arial', 20, True)

# Función para limitar un valor entre un minimo y un maximo
def clamp(numero, minimo=0, maximo=100):
    return max(min(numero, maximo), minimo)
