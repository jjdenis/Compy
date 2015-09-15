#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep

from src.key import PressedKey
from src.map import ScreenMap, PrintMap
from src.colors import colors
from src.char_table import CharTable
from src.settings import INIT_MSG
from src.settings import INIT_FM_COLOR, INIT_BG_COLOR, INIT_CH_COLOR


char_table = CharTable()

class Control(object):
    def __init__(self, queue_to_view, queue_from_view):
        self.view = View(queue_to_view, queue_from_view)
        self.key = PressedKey(self.view.receive)
        self.map = ScreenMap()
        self.printmap = PrintMap()
        self.fm_color = INIT_FM_COLOR
        self.bg_color = INIT_BG_COLOR
        self.ch_color = INIT_CH_COLOR
        self._reset_canvas()
        self.printf(INIT_MSG)

    def poke(self, x, y, code, color = None):
        if color:
            color_c = colors.get_color(color)
            self.ch_color = color_c

        if code:
            char_id = char_table.get_identifier(code)
        else:
            char_id = 31
        # c stands for corrected
        self.set_char_in_screen(char_id, x, y)

    def peek(self, x, y):
        char_id, color = self.map.get_poked(x, y)
        return char_id

    def printf(self, to_print='', color=None, next_line = True, iscode=False):
        if color is not None:
            color_c = colors.get_color(color)
            self.ch_color = color_c

        if isinstance(to_print, int) and iscode:
            x, y = self.printmap.next_x()
            self.set_char_in_screen(to_print, x, y)
            return

        string=unicode(to_print)

        if not string and next_line:
            self.printmap.end_line()

        for i, ch in enumerate(string):
            if ch == u'\n':
                self.printmap.next_line()
                self.printmap.end_line()
                continue
            first_char = (i == 0)
            if next_line and first_char:
                x, y = self.printmap.next_line()
            else:
                x, y = self.printmap.next_x()

            char_id = char_table.get_identifier(ch)

            self.set_char_in_screen(char_id, x, y)

    def set_char_in_screen(self, char_id, x, y):
        cx, cy = self.map.set_poked(x, y, char_id, self.ch_color)
        self._send_to_view('poke', cx, cy, char_id, self.ch_color, self.bg_color)

    def set_bg_color(self, color):
        self.bg_color = color
        self._reset_canvas()
        self._write_all_chars()

    def set_fm_color(self, color):
        self.fm_color = color
        self._reset_canvas()
        self._write_all_chars()

    def clear_screen(self):
        self._reset_canvas()
        self.printmap.go_end_scr()
        self.map.clear(self.bg_color)

    def stop(self):
        sleep(1)
        self._send_to_view('close_window')

    def wait_key(self):
        key = self.key.wait_for_key()
        return key

    def check_key(self):
        key = self.key.check_for_key()
        return key

    def _reset_canvas(self):
        self._send_to_view('reset_canvas', self.fm_color, self.bg_color)

    def _write_all_chars(self):
        for poked in self.map.written:
            self._send_to_view('poke', poked.x, poked.y, poked.code, poked.color)

    def _send_to_view(self, *args):
        self.view.send(*args)



class View(object):
    def __init__(self, queue1, queue2):
        self.to_view = queue1
        self.from_view = queue2

    def send(self, *args):
        self.to_view.put(args)

    def receive(self):
        if not self.from_view.empty():
            return self.from_view.get()
        else:
            return None


