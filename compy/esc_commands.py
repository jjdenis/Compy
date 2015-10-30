#!/usr/bin/env python
# -*- coding: utf-8 -*-

from compy.create_web import make_all_html, take_code, save_img
from compy.colors import colors
from compy.char_table import CharTable
from compy.settings import INIT_FM_COLOR, INIT_BG_COLOR
from compy.settings import ESC_MESSAGE

S_KEY = 83
H_KEY = 72
__author__ = 'jjdenis'
ESCAPE = 27


class EscapeCommands(object):
    def __init__(self, poke, envia_comando, cierra_por_esc, get_img):
        self.poke = poke
        self.cierra_por_esc = cierra_por_esc
        self.envia_comando = envia_comando
        self.get_img = get_img
        self.char_table = CharTable()
        self.accepting_commands =False

    def run(self, key):
        if not self.accepting_commands:
            if key == ESCAPE:
                self.msg(ESC_MESSAGE)
                self.accepting_commands =True
                return None
            else:
                return key

        if key == ESCAPE:
            self.cierra_por_esc()
        elif key == S_KEY: # Take screenshot
            self.del_msg(ESC_MESSAGE)
            take_code()
            self.accepting_commands = False
            img = self.get_img()
            save_img(img)
        elif key == H_KEY: # Recreate web site
            make_all_html()
            self.accepting_commands = False
            self.del_msg(ESC_MESSAGE)
        else:
            self.accepting_commands = False

        return None

    def msg(self, msg):
        color_c = colors.get_color(INIT_BG_COLOR)
        color_b = colors.get_color(INIT_FM_COLOR)

        for i, ch in enumerate(msg):
            char_id = self.char_table.get_code(ch)
            self.poke(0+i, -2, char_id, color_c, color_b)

    def del_msg(self, msg):
        color_b = colors.get_color(INIT_BG_COLOR)
        color_c = colors.get_color(INIT_FM_COLOR)

        for i, ch in enumerate(msg):
            char_id = self.char_table.get_code(u'█')
            self.poke(0+i, -2, char_id, color_c, color_b)

