# -*- coding: utf-8 -*-

from src.run import run
import time

def programa_principal(scr):

    mapa_caracteres(scr)
    time.sleep(10)
    wait_for_key(scr)

    scr.clear_screen()
    scr.printf(u'╭')
    for i in range(0,100):
        scr.printf(u'Hola', i, next_line=False)

    scr.poke(10, 10, u'╭', color=0)

    wait_for_key(scr)

    #scr.stop()

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



def wait_for_key(scr):
    key = None
    while not key:
        key = scr.get_key()
        if key:
            print key


run(programa_principal)
