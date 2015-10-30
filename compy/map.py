#!/usr/bin/env python
# -*- coding: utf-8 -*-

from compy.settings import NUM_COLS, NUM_ROWS, INIT_BG_COLOR
from time import sleep

FIRST_X = 0
LAST_X = NUM_COLS - 1
FIRST_LINE = NUM_ROWS - 1
LAST_LINE  = 0


class PrintMap(object):
    """
    LLeva x e y, la posición (en el mapa xy lógico) del
    próximo carácter donde se va a imprimir con printf

    """
    def __init__(self, clear_screen):
        self.x = None
        self.y = None
        self.go_init_scr()
        self.clear_screen = clear_screen
        self.clear_screen_next=False

    def go_init_scr(self):
        self.go_first_line()
        self.go_first_x()

    def go_first_line(self):
        self.y = FIRST_LINE

    def go_first_x(self):
        self.x = FIRST_X

    def get_next_pos(self):
        posx, posy = (self.x, self.y)
        self.next_x()
        return posx, posy

    def next_x(self):
        if self.clear_screen_next:
            sleep(2)
            self.clear_screen()
            self.clear_screen_next = False

        in_last_x = (self.x == LAST_X)
        if in_last_x:
            self.next_line()
            # self.clear_screen()
        else:
            self.x += 1
        return self.x, self.y

    def next_line(self):
        in_last_line = self.y == LAST_LINE
        if in_last_line:
            self.go_first_line()
            self.clear_screen_next=True
        else:
            self.y -= 1
        self.go_first_x()
        return self.x, self.y



class ScreenMap(object):
    def __init__(self):
        self.map = []
        for x in range(0, NUM_COLS):
            self.map.append([])
            for y in range(0, NUM_ROWS):
                self.map[x].append(Poked(x, y, None, INIT_BG_COLOR))
        self.written = set()

    def clear(self, color):
        for x in range(0, NUM_COLS):
            for y in range(0, NUM_ROWS):
                self.set_poked(x, y, None, color)

    def get_poked(self, x, y):
        x, y = self.check_coords(x, y)
        poked = self.map[x][y]
        return poked.code, poked.color

    def set_poked(self, x, y, code, color):
        x, y = self.check_coords(x, y)

        poked = self.map[x][y]
        poked.code = code
        poked.color = color
        if code == None:
            self.written.discard(poked)
        else:
            self.written.add(poked)

        return x, y

    def check_coords(self, x, y):
        if x < 0:
            x = 0
        elif x >= NUM_COLS:
            x = NUM_COLS - 1
        if y < 0:
            y = 0
        elif y >= NUM_ROWS:
            y = NUM_ROWS - 1
        return x, y


class Poked(object):
    def __init__(self, x, y, code, color):
        self.x = x
        self.y = y
        self.code = code
        self.color = color
    def __repr__(self):
        return str((self.x, self.y, self.code, self.color))
