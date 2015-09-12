# -*- coding: utf-8 -*-

from src.run import run
from time import time, sleep

def programa_principal(scr):

    mapa_caracteres(scr)
    scr.wait_key()

    prueba_print(scr)
    scr.wait_key()

    prueba_move(scr)
    scr.stop()

    #scr.stop()


def prueba_print(scr):
    scr.clear_screen()
    scr.printf(u'╭')
    for i in range(0, 100):
        scr.printf(u'Hola', i, next_line=False)
    scr.poke(10, 10, u'╭', color=0)


def mapa_caracteres(scr):
    scr.clear_screen()
    scr.printf('\nPinta todos los caracteres\n')

    for i in range(0, 400):
        scr.printf('{:>03}='.format(i), next_line=False)
        scr.printf(i, next_line=False, iscode=True)
        scr.printf('  '.format(i), next_line=False)
        if (i+1)%100 == 0:
            scr.wait_key()
            scr.clear_screen()
            scr.printf('\n')
        if (i+1)%5 == 0:
            scr.printf('')
    # i = 0
    # color = 0
    # for y in range(20, -1, -1):
    #     for x in range(0, 40):
    #         print "Pintando caracter", i
    #         scr.poke(x, y, i, color)
    #         i = i + 1
    #         color = color + 1
    #         if color == 6:
    #             color = 7
    #         if color == 16:
    #             color = 0
    #
    #




def prueba_move(scr):
    scr.clear_screen()
    A = 65
    B = 66
    Q = 81
    DCHA = 316
    IZDA = 314
    ABAJO = 317
    ARRIBA = 315

    x = 0
    y = 0
    scr.poke(x, y, B, 'light_green')
    scr.poke(10, 20, A, 'light_green')
    scr.poke(5, 5, A, 'light_green')
    while True:
        a = scr.check_key()
        if not a:
            continue
        scr.poke(x, y, None, 'red')
        if a == DCHA:
            x += 1
        elif a == IZDA:
            x -= 1
        elif a == ARRIBA:
            y += 1
        elif a == ABAJO:
            y += -1
        elif a == Q: # q
            break
        else:
            pass

        if scr.peek(x, y+1) == A:
            scr.poke(x, y, B, 'red')
        else:
            scr.poke(x, y, B, 'light_red')


run(programa_principal)
