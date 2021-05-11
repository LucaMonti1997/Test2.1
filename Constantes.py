import pygame

# Ancho y alto de la ventana de juego
WIDTH = 1000
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
    # Carta que usan ladrillos
    "muralla1": [[5, "ladrillos"], [5, "hp_muralla"]],
    "muralla2": [[10, "ladrillos"], [10, "hp_muralla"]],
    "muralla3": [[20, "ladrillos"], [25, "hp_muralla"]],
    "castillo1": [[5, "ladrillos"], [3, "hp_castillo"]],
    "castillo2": [[10, "ladrillos"], [6, "hp_castillo"]],
    "castillo3": [[20, "ladrillos"], [15, "hp_castillo"]],
    "constructores_amigos": [[7, "ladrillos"], [1, "constructores"]],
    "constructores_enemigos": [[20, "ladrillos"], [-1, "constructores"]],

    # Carta que usan espadas
    "espada1": [[5, "espadas"], [-2, "hp_muralla"]],
    "espada2": [[10, "espadas"], [-4, "hp_muralla"]],
    "espada3": [[20, "espadas"], [-15, "hp_muralla"]],
    "arco1": [[7, "espadas"], [-2, "hp_castillo"]],
    "arco2": [[14, "espadas"], [-4, "hp_castillo"]],
    "arco3": [[25, "espadas"], [-20, "hp_castillo"]],
    "soldados_amigos": [[7, "espadas"], [1, "soldados"]],
    "soldados_enemigos": [[20, "espadas"], [-1, "soldados"]],

    # Carta que usan mana

    "magia1": [[9, "mana"], [-2, "hp_muralla"]],
    "magia2": [[18, "mana"], [-4, "hp_muralla"]],
    "magia3": [[40, "mana"], [-15, "hp_muralla"]],
    "regenerar1": [[8, "mana"], [5, "hp_muralla"]],
    "regenerar2": [[16, "mana"], [10, "hp_muralla"]],
    "regenerar3": [[24, "mana"], [15, "hp_castillo"]],
    "conjurar_ladrillos": [[3, "mana"], [5, "ladrillos"]],
    "conjurar_espadas": [[3, "mana"], [5, "espadas"]],
    "conjurar_mana": [[3, "mana"], [5, "mana"]],
    "magos_amigos": [[7, "mana"], [1, "magos"]],
    "magos_enemigos": [[20, "mana"], [-1, "magos"]],

}

# Contiene distintos mazos que se pueden jugar
diccionario_mazos = {
    1: ["muralla1", "muralla2", "muralla3", "castillo1", "castillo2", "castillo3",
        "constructores_amigos", "constructores_enemigos", "arco1",
        "arco2", "arco3", "espada1", "espada2", "espada3", "soldados_amigos",
        "soldados_enemigos", "magia1", "magia2", "magia3",
        "regenerar1", "regenerar2", "regenerar3", "conjurar_ladrillos", "conjurar_espadas",
        "conjurar_mana", "magos_amigos", "magos_enemigos"]
}
# Numero de cartas que se tienen en mano a la vez
NUMERO_CARTAS_MANO = 8

# Fonts usados en el juego
pygame.font.init()
font = pygame.font.SysFont('Arial', 30)
font_recursos = pygame.font.SysFont('Cambria', 20, True)


# Función para limitar un valor entre un minimo y un maximo
def clamp(numero, minimo=0, maximo=100):
    return max(min(numero, maximo), minimo)
