class Mazo(object):

    def __init__(self, tipo):
        self.mazo_1_completo = ["muralla", "defensa", "muralla", "defensa", "muralla", "defensa", "muralla", "defensa",
                                "muralla", "espada", "espada", "espada", "espada"]
        self.cartas_restantes = []
        if tipo == 1:
            for item in self.mazo_1_completo:
                self.cartas_restantes.append(item)
            # self.cartas_restantes = self.mazo_1_completo

    def ComprobarMazo(self):
        if len(self.cartas_restantes) == 0:
            self.cartas_restantes = self.mazo_1_completo
