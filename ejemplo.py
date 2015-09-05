# -*- coding: utf-8 -*-

from src.run import run
import time

def programa_principal(pnt):

    pnt.printf(u"Hola")

    for i in range(0, 100):
        pnt.printf(i, i, next_line=False)

    pnt.printf(u"Hola", 'cyan')
    pnt.printf()
    pnt.printf(u"Hola", color='green')

run(programa_principal)
