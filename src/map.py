#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.settings import NUM_COLS, NUM_ROWS, INIT_BG_COLOR


FIRST_X = 0
LAST_X = NUM_COLS - 1
FIRST_LINE = NUM_ROWS - 1
LAST_LINE  = 0


class PrintMap(object):
    """
    LLeva x e y, la posición (en el mapa xy lógico) del último carácter que se imprimió con printf

    """
    def __init__(self):
        self.x = None
        self.y = None
        self.go_end_scr()

    def end_line(self):
        self.x = LAST_X

    def next_line(self):
        in_last_line = self.y == LAST_LINE
        if in_last_line:
            self.go_first_line()
        else:
            self.y -= 1
        self.go_first_x()
        return self.x, self.y

    def next_x(self):
        in_last_x = (self.x == LAST_X)
        if in_last_x:
            self.next_line()
        else:
            self.x += 1
        return self.x, self.y

    def go_first_line(self):
        self.y = FIRST_LINE

    def go_first_x(self):
        self.x = FIRST_X

    def go_end_scr(self):
        self.x = LAST_X
        self.y = LAST_LINE


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
        poked = self.map[x][y]
        return poked.code, poked.color

    def set_poked(self, x, y, code, color):
        if x >= NUM_COLS:
            x = NUM_COLS -1
        if y >= NUM_ROWS:
            y = NUM_ROWS-1

        poked = self.map[x][y]
        poked.code = code
        poked.color = color
        if code == None:
            self.written.discard(poked)
        else:
            self.written.add(poked)

        return x, y


class Poked(object):
    def __init__(self, x, y, code, color):
        self.x = x
        self.y = y
        self.code = code
        self.color = color
    def __repr__(self):
        return str((self.x, self.y, self.code, self.color))
