#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime as dttm

from src.map import ScreenMap, PrintMap
from src.colors import colors

from src.settings import INIT_MSG

from src.settings import INIT_FM_COLOR, INIT_BG_COLOR, INIT_CH_COLOR


class Control(object):
    def __init__(self, queue_to_view, queue_from_view):
        self.view = View(queue_to_view, queue_from_view)
        self.key = PressedKey()
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

        if isinstance(code, basestring):
            code=unicode(code)[0:1]
        else:
            code = char.unicode(code)

        # c stands for corrected
        cx, cy = self.map.set_poked(x, y, code, self.ch_color)
        self._send_to_view('poke', cx, cy, code, self.ch_color, self.bg_color)

    def peek(self, x, y):
        code, color = self.map.get_poked(x, y)
        return code

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


            cx, cy = self.map.set_poked(x, y, ch, self.ch_color)
            self._send_to_view('poke', cx, cy, ch, self.ch_color, self.bg_color)

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
        time.sleep(1)
        self._send_to_view('close_window')

    def get_key(self):
        self._read_from_view()
        time.sleep(0.01)
        return self.key.get()

    def _write_canvas(self):
        self._send_to_view('reset_screen', self.fm_color, self.bg_color)

    def _write_all_chars(self):
        for poked in self.map.written:
            self._send_to_view('poke', poked.x, poked.y, poked.code, poked.color)

    def _send_to_view(self, *args):
        self.view.send(*args)

    def _read_from_view(self):
        while True:
            msg = self.view.receive()
            if not msg:
                break
            if msg[0] == 'key_pressed':
                self.key.pressed(msg[1])
            if msg[0] == 'key_released':
                self.key.released()


class View(object):
    def __init__(self, queue1, queue2):
        self.to_view = queue1
        self.from_view = queue2

    def send(self, *args):
        self.to_view.put(args)

    def receive(self):
        if not self.from_view.empty():
            return self.from_view.get_key()
        else:
            return None





class PressedKey(object):
    """ This object ensures that even a tiny press is sent """
    def __init__(self):
        self.curr_key = None
        self.last_key_pressed = None
        self.time_key_pressed = dttm.datetime.now()
        self.time_key_sent = dttm.datetime.now()

    def pressed(self, key):
        if self.curr_key is None:
            self.time_key_pressed = dttm.datetime.now()

        self.last_key_pressed = key
        self.curr_key = key

    def released(self):
        self.curr_key = None

    def get(self):

        last_key_not_sent = self.time_key_pressed > self.time_key_sent

        if self.curr_key is None and last_key_not_sent:
            self.time_key_sent = dttm.datetime.now()
            return self.last_key_pressed

        if self.curr_key:
            self.time_key_sent = dttm.datetime.now()

        return self.curr_key


#
# def run_control(queue1, queue2, main):
#     try:
#         control = Control(queue1, queue2)
#         main(control)
#         # main finishes here
#         # control.stop()
#     except:
#         print "FATAL: exited while multiprocessing".format()
#         traceback.print_exc()
#
#
#
#
# def run(main):
#
#     q_to_view = multiprocessing.Queue()
#
#     q_from_view = multiprocessing.Queue()
#
#     control_parallel = multiprocessing.Process(
#         target=run_control,
#         args=(q_to_view, q_from_view, main))
#
#     control_parallel.start()
#
#     gui = view.GUIwx(q_to_view, q_from_view)
#     gui.run()
#
#     control_parallel.join()
#
#     while not q_to_view.empty():
#         q_to_view.get()
#     while not q_from_view.empty():
#         q_from_view.get()
#
#     q_to_view.close()
#     q_from_view.close()
#     q_to_view.join_thread()
#     q_from_view.join_thread()
#
#
#
