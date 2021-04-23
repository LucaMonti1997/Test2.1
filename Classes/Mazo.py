class Mazo(object):
    mazo_1_completo = ["muralla", "defensa", "muralla", "defensa", "muralla", "defensa", "muralla", "defensa",
                       "muralla", "espada", "espada", "espada", "espada"]

    def __init__(self, tipo):
        if tipo == 1:
            self.cartas_restantes = self.mazo_1_completo

    def ComprobarMazo(self):
        if len(self.cartas_restantes) == 0:
            self.cartas_restantes = self.mazo_1_completo
