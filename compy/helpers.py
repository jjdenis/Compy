#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'jjdenis'

Q = 81
ARRIBA = 315
from compy.colors import colors

class MapaDeCaracteres(object):
    def __init__(self, screen):
        global scr
        scr=screen
        self.resetea_pantalla()
        init_cod=0
        num_continuation = 0
        while True:
            self.pinta_100(init_cod)
            tecla = scr.wait_key()
            if tecla == Q:
                break
            if tecla == ARRIBA and init_cod > 0:
                init_cod=init_cod-100
            elif tecla == ARRIBA and init_cod == 0:
                pass
            elif init_cod == 200:
                num_continuation +=1
                if num_continuation == 4:
                    break
                pass
            else:
                init_cod = init_cod + 100


            # if final_de_linea:
            #     self.pinta_separador_filas()


    def pinta_100(self, init_code):
        self.resetea_pantalla()
        for fila in range(0,10):
            char_cod = 10 * fila + init_code
            self.pinta_separador_filas()
            self.nombre_fila(char_cod)
            for columna in range(0,10):
                char_cod = 10 * fila + columna + init_code
                self.pinta_caracter(char_cod)

        self.pinta_separador_filas()


    def resetea_pantalla(self):
        scr.set_bg_color(1)
        scr.clear_screen()
        scr.printf('')

    def pinta_separador_filas(self):
        scr.printf()
        scr.printf('       ', stay=True)
        for k in range(5, 26):
            scr.printf(31, color=8, stay=True, iscode=True)
        scr.printf()

    def nombre_fila(self, char_cod):
        scr.printf('{:>03}-{:>03}'.format(char_cod, char_cod + 9), stay=True)
        scr.printf(31, color=8, stay=True, iscode=True)

    def pinta_caracter(self, char_cod):
        scr.printf(char_cod, color=4, stay=True, iscode=True)
        scr.printf(31, color=8, stay=True, iscode=True)

class ListaDeColores(object):
    def __init__(self, screen):
        global scr
        scr=screen
        self.resetea_pantalla()
        scr.printf('    Lista de colores \n')
        scr.printf('')

        for i in range(0, 20):
            color_name=colors.get_color_name(i)
            scr.printf('    {:>2} '.format(i), color=i, stay=True)
            scr.printf(color_name, color=i)
        scr.wait_key()


    def resetea_pantalla(self):
        scr.clear_screen()
        scr.printf('')


class ListOfKeys(object):
    def __init__(self, screen):
        global scr
        scr=screen
        self.resetea_pantalla()
        scr.printf('Pulsa una tecla (Q para terminar)')
        while True:
            a = scr.wait_key()
            scr.clear_screen()
            scr.printf(u'El código de tecla pulsado es ' + str(a))
            scr.printf('Pulsa una tecla (Q para terminar)')
            if a == Q:
                break

    def resetea_pantalla(self):
        scr.clear_screen()
        scr.printf('')

