#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time, sleep
import datetime as dttm
import sys
from src.map import ScreenMap, PrintMap
from src.colors import colors
from src.char_table import CharTable
from src.settings import INIT_MSG
from src.settings import INIT_FM_COLOR, INIT_BG_COLOR, INIT_CH_COLOR

SENSIBILIDAD_TECLADO = 0.05

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
        self._write_canvas()
        self.printf(INIT_MSG)

    def poke(self, x, y, code, color = None):
        if color:
            color_c = colors.get_color(color)
            self.ch_color = color_c

        char_id = char_table.get_identifier(code)
        # c stands for corrected
        cx, cy = self.map.set_poked(x, y, char_id, self.ch_color)
        self._send_to_view('poke', cx, cy, char_id, self.ch_color, self.bg_color)

    def peek(self, x, y):
        char_id, color = self.map.get_poked(x, y)
        return char_id

    def printf(self, to_print='', color=None, next_line = True):
        if color is not None:
            color_c = colors.get_color(color)
            self.ch_color = color_c
        if isinstance(to_print, basestring):
            string=unicode(to_print)
        else:
            string = unicode(to_print)
        if not string and next_line:
            self.printmap.next_line()
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

            cx, cy = self.map.set_poked(x, y, char_id, self.ch_color)
            self._send_to_view('poke', cx, cy, char_id, self.ch_color, self.bg_color)

    def set_bg_color(self, color):
        self.bg_color = color
        self._write_canvas()
        self._write_all_chars()

    def set_fm_color(self, color):
        self.fm_color = color
        self._write_canvas()
        self._write_all_chars()

    def clear_screen(self):
        self._write_canvas()
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

    def _write_canvas(self):
        self._send_to_view('reset_screen', self.fm_color, self.bg_color)

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


class PressedKey(object):
    """ This object ensures that even a tiny press is sent """
    def __init__(self, receive):
        self.receive_from_view = receive
        self.curr_key = None
        self.last_time_read = 0
        self.key_this_pass = None
        self.key_queue = []

    def wait_for_key(self):
        self._read_from_view()
        while not self.key_this_pass:
            self._read_from_view()
        return self.key_this_pass

    def check_for_key(self):
        self._read_from_view()
        if self.curr_key:
            return self.curr_key
        else:
            if self.key_queue:
                return self.key_queue.pop(0)
        return None

    def _read_from_view(self):
        while time() - self.last_time_read <= SENSIBILIDAD_TECLADO:
            pass

        self.key_this_pass = None
        while True:
            msg = self.receive_from_view()
            if not msg:
                break
            comando, tecla, tiempo = msg
            print comando, tecla, tiempo
            if comando == 'key_pressed':
                if tecla != self.curr_key:
                    self.key_queue.append(tecla)
                self.curr_key = tecla
                self.key_this_pass = tecla
            elif comando == 'key_released':
                self.curr_key = None
            elif comando == 'closing':
                sys.exit()
            else:
                pass
        self.last_time_read = time()

