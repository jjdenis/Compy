#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep, time
import sys

from src.key import PressedKey
from src.map import ScreenMap, PrintMap
from src.colors import colors
from src.char_table import CharTable
from src.settings import INIT_MSG
from src.settings import INIT_FM_COLOR, INIT_BG_COLOR, INIT_CH_COLOR
from src.helpers import MapaDeCaracteres, ListaDeColores, ListOfKeys

ENTER = 13
LIMIT_WO_KEYSTROKE = 120 #secs

class Control(object):
    def __init__(self, queue_to_view, queue_from_view):
        self.map = ScreenMap()
        self.char_table = CharTable()
        self.printmap = PrintMap(self.clear_screen)
        self.fm_color = colors.get_color(INIT_FM_COLOR)
        self.bg_color = colors.get_color(INIT_BG_COLOR)
        self.ch_color = colors.get_color(INIT_CH_COLOR)
        self.last_comm_time = time()

        self.comm_to_view = CommToView(queue_to_view, queue_from_view)
        self.key = PressedKey(self._receive_from_view)
        self._reset_canvas()
        self.printf(INIT_MSG)

    def poke(self, x, y, code, color = None, reverse=False):
        if color:
            color_c = colors.get_color(color)
            self.ch_color = color_c

        if isinstance(code, int):
            char_id = self.char_table.get_code(code)
            self.set_char_in_screen(char_id, x, y, reverse)
        else:
            char_id = 31
            self.set_char_in_screen(char_id, x, y)

        # c stands for corrected

    def xyprint(self, x, y, *args):
        string = u''
        for to_chain in args:
            if isinstance(to_chain, str):
                to_chain=to_chain.decode('utf-8')
            to_chain=unicode(to_chain)
            string += to_chain

        for i, ch in enumerate(string):
            if ch == u'\n':
                continue
            char_id = self.char_table.get_code(ch)
            self.set_char_in_screen(char_id, x, y)
            x=x+1

    def peek(self, x, y):
        char_id, color = self.map.get_poked(x, y)
        return char_id

    def printf(self, to_print='', color=None, next_line = True, iscode=False, reverse=False):
        if color is not None:
            color_c = colors.get_color(color)
            self.ch_color = color_c

        if to_print == '' or to_print is None:
            self.printmap.next_line()
            return

        if isinstance(to_print, int) and iscode:
            x, y = self.printmap.next_x()
            self.set_char_in_screen(to_print, x, y, reverse)
            return
        elif isinstance(to_print, str):
            to_print=to_print.decode('utf-8')

        string=unicode(to_print)


        for i, ch in enumerate(string):
            if ch == u'\n':
                self.printmap.next_line()
                print 'nono'
                continue

            x, y = self.printmap.get_next_pos()

            char_id = self.char_table.get_code(ch)
            self.set_char_in_screen(char_id, x, y, reverse)

        if next_line:
            self.printmap.next_line()

    def set_char_in_screen(self, char_id, x, y, reverse=False):
        if not reverse:
            cx, cy = self.map.set_poked(x, y, char_id, self.ch_color)
            self._send_to_view('poke', cx, cy, char_id, self.ch_color, self.bg_color)
        else:
            cx, cy = self.map.set_poked(x, y, char_id, self.bg_color)
            self._send_to_view('poke', cx, cy, char_id, self.bg_color, self.ch_color)

    def set_bg_color(self, color):
        if color is None:
            return
        color_c = colors.get_color(color)
        self.bg_color = color_c
        self._reset_canvas()
        self._write_all_chars()

    def set_fm_color(self, color):
        if color is None:
            return
        color_c = colors.get_color(color)
        self.fm_color = color_c
        self._reset_canvas()
        self._write_all_chars()

    def clear_screen(self):
        self._reset_canvas()
        self.printmap.go_init_scr()
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

    def input(self, message = '', color=None):
        if color is not None:
            color_c = colors.get_color(color)
            self.ch_color = color_c

        self.printf(message, next_line=False)
        input = ''
        key = 0
        while key != ENTER:
            key = self.key.wait_for_key()
            char=self.char_table.get_unicode(key)
            if char:
                input +=char
                self.printf(char, next_line=False)
        try:
            input=int(input)
        except:
            try:
                input=float(input)
            except:
                pass
        self.printf()
        return input

    def mapa(self):
        MapaDeCaracteres(self)

    def colors(self):
        ListaDeColores(self)

    def keys(self):
        ListOfKeys(self)

    def _reset_canvas(self):

        self._send_to_view('reset_canvas', self.fm_color, self.bg_color)

    def _write_all_chars(self):
        for poked in self.map.written:
            self._send_to_view('poke', poked.x, poked.y, poked.code, poked.color, self.bg_color)

    def _send_to_view(self, *args):
        self.comm_to_view.send(*args)
        self._check_comm_time()

    def _receive_from_view(self):
        msg = self.comm_to_view.receive()
        if msg:
            self.last_comm_time = time()
        self._check_comm_time()
        return msg

    def _check_comm_time(self):
        elapsed = time() - self.last_comm_time
        if elapsed > LIMIT_WO_KEYSTROKE:
            print 'stop por tiempo'
            self.stop()



class CommToView(object):
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


