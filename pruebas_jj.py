# -*- coding: utf-8 -*-

from src.run import run
from time import time, sleep

def programa_principal(scr):

    mapa_caracteres(scr)

    scr.get_key()

    prueba_print(scr)

    scr.get_key()

    prueba_move(scr)

    #scr.stop()


def prueba_print(scr):
    scr.clear_screen()
    scr.printf(u'╭')
    for i in range(0, 100):
        scr.printf(u'Hola', i, next_line=False)
    scr.poke(10, 10, u'╭', color=0)


def mapa_caracteres(scr):
    scr.clear_screen()
    i = 0
    color = 0
    for y in range(24, -1, -1):
        for x in range(0, 40):
            scr.poke(x, y, i, color)
            i = i + 1
            color = color + 1
            if color == 6:
                color = 7
            if color == 16:
                color = 0






def prueba_move(scr):
    scr.poke(10, 20, 65, 'light_green')
    x = 0
    y = 0
    while True:
        a = scr.get_key()
        if a:
            scr.poke(x, y, None, 'red')
        if a == 316:
            x += 1
        if a == 314:
            x -= 1
        if a == 315:
            y += 1
        if a == 317:
            y += -1
        if a == 81: # q
            break

        if scr.peek(x, y+1) == 65:
            scr.poke(x, y, 66, 'red')
        else:
            scr.poke(x, y, 66, 'light_red')


run(programa_principal)
