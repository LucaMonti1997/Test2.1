import threading

from Base import *
from Jugador import *
from Mazo import *
from Narrador import *
from Ventana import *

import pygame
from pygame_widgets import *

pygame.init()

# Inicializamos fonts
pygame.font.init()

# Inizializar pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('beta')
fondo = pygame.image.load("Assets/Castillo/Mapa Fondo.png").convert_alpha()
fondo = pygame.transform.smoothscale(fondo, (int(fondo.get_width() / 1.7), int(fondo.get_height() / 1.7)))

# Declaramos ventanas
ventana_menu_principal = Ventana(screen, "menu_principal")
ventana_menu_opciones = Ventana(screen, "menu_opciones", [300, HEIGHT * 6 / 8])
ventana_juego = Ventana(screen, "juego")
ventana_final_partida = Ventana(screen, "final_partida")

ventana_menu_principal.InicializarImagenes()
ventana_menu_principal.InicializarInterfaz()
ventana_menu_opciones.InicializarImagenes()
ventana_menu_opciones.InicializarInterfaz()


# Declaramos jugadores
mazo1 = Mazo(1)
base1 = Base([WIDTH*3/10, 300], [0.5, 0.5])
jugador1 = Jugador(base1, mazo1, 0)

mazo2 = Mazo(1)
base2 = Base([WIDTH*7/10, 300], [0.5, 0.5])
jugador2 = Jugador(base2, mazo2, 1)

narrador = Narrador(jugador1, jugador2)


# Debugeado
# slider = Slider(screen, 100, 100, 200, 40, min=0, max=100, step=1)


def mouseHandler(pos, state):
    """
    Comprueba si el click del ratón tiene que provocar alguna reacción.

    :param pos: Posición del ratón a comprobar
    :param state: QUe click se ha hecho. 0 -> izquierda, 1 -> medio, 2 -> derecho
    :return:
    """
    # Si estamos en la ventana de juego, comprobamos si hemos click en alguna carta
    if ventana_juego.focus:
        if state == 1:
            narrador.DetectarClickCarta(pos, True)
        elif state == 3:
            narrador.DetectarClickCarta(pos, False)

    # En la ventana del menu principal, el primer boton es jugar, el ultimo es salir
    elif ventana_menu_principal.focus and state == 1:
        if ventana_menu_principal.DetectarBoton(pos) == "jugar":
            ventana_menu_principal.Desactivar()
            jugador1.InicializarJugador()
            jugador2.InicializarJugador()
            ventana_juego.Activar()
        elif ventana_menu_principal.DetectarBoton(pos) == "salir":
            pass
            pygame.event.post(pygame.event.Event(fin_aplicacion))

    # En la ventana de fin de partida, el click medio avanza al menu principal. TODO cambiar esto
    elif ventana_final_partida.focus and state == 2:
        ventana_final_partida.Desactivar()
        ventana_juego.Desactivar()
        ventana_menu_principal.Activar()

    elif ventana_menu_opciones.focus and state == 1:

        if ventana_menu_opciones.DetectarBoton(pos) == "cargar":
            jugador1.Retraer_Cartas_Guardadas()
            jugador2.Retraer_Cartas_Guardadas()

        elif ventana_menu_opciones.DetectarBoton(pos) == "guardar":
            jugador1.Guardar_Cartas()
            jugador2.Guardar_Cartas()

        ventana_menu_opciones.Desactivar()
        ventana_juego.GainFocus()


def renderWindow():
    """
    Actualiza la pantalla
    """
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        if ventana_menu_principal.activa:
            pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT))
            ventana_menu_principal.MostrarBotones()

        if ventana_juego.activa:
            screen.blit(fondo, (0, 0))

            jugador1.MostrarBase(screen)
            jugador1.MostrarRecursos(screen)
            jugador2.MostrarBase(screen)
            jugador2.MostrarRecursos(screen)
            if narrador.turno == 0:
                jugador1.MostrarCartas(screen)
            else:
                jugador2.MostrarCartas(screen)
            texto_turno = font.render("Turno jugador: " + str(narrador.turno), False, (0, 0, 0))
            screen.blit(texto_turno, [(WIDTH / 2) - 100, 25])

        if ventana_menu_opciones.activa:
            rect = ((WIDTH / 2) - 150, HEIGHT / 8, 300, HEIGHT * 6 / 8)
            pygame.draw.rect(screen, BLACK, rect)
            ventana_menu_opciones.MostrarBotones()

        if ventana_final_partida.activa:
            rect = (100, 100, 150, 250)
            pygame.draw.rect(screen, RED, rect)

        pygame.display.update()


def main():
    clock = pygame.time.Clock()
    # Declaramos thread
    threads = []
    thread_grafico = threading.Thread(target=renderWindow, daemon=True)
    thread_click = threading.Thread(target=mouseHandler)
    threads.append(thread_grafico)
    thread_grafico.start()
    run = True
    ventana_menu_principal.Activar()
    while run:
        clock.tick(30)
        for e in pygame.event.get():

            # Clickear la X cierra todas las ventanas y la aplicación
            if e.type == pygame.QUIT or e.type == fin_aplicacion:
                run = False
                ventana_final_partida.Desactivar()
                ventana_juego.Desactivar()
                ventana_menu_principal.Desactivar()
                ventana_menu_opciones.Desactivar()
                for t in threads:
                    t.join(0.1)

            if e.type == pygame.KEYDOWN:
                # ESC muestra o esconde el menu de opciones
                if e.key == pygame.K_ESCAPE:
                    if ventana_juego.focus:
                        ventana_juego.LoseFocus()
                        ventana_menu_opciones.Activar()
                    elif ventana_menu_opciones.focus:
                        ventana_menu_opciones.Desactivar()
                        ventana_juego.GainFocus()

            if e.type == pygame.MOUSEBUTTONDOWN:
                if not thread_click.is_alive():
                    thread_click = threading.Thread(target=mouseHandler, args=(pygame.mouse.get_pos(), e.button))
                    threads.append(thread_click)
                    thread_click.start()

            if e.type == fin_partida:
                ventana_juego.LoseFocus()
                ventana_menu_opciones.Desactivar()
                ventana_final_partida.Activar()

    pygame.quit()


if __name__ == "__main__":
    main()
