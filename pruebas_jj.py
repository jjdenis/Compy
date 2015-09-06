# -*- coding: utf-8 -*-

from src.run import run
import time

def programa_principal(scr):
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

    scr.poke(10, 10, u'╭')


run(programa_principal)
