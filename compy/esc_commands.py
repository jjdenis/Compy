#!/usr/bin/env python
# -*- coding: utf-8 -*-

from compy.color_table import colors
from compy.char_table import CharTable
from compy.settings import INIT_FM_COLOR, INIT_BG_COLOR
from compy.settings import ESC_MESSAGE
import __main__
import wx

name_of_project= __main__.__file__.split('/')[-1]

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
        self.command_mode =False

    def run(self, key):
        if not self.command_mode:
            if key != ESCAPE:
                return key
            else:
                return self.first_escape()

        return self.command(key)

    def command(self, key):
        if key == ESCAPE:
            self.cierra_por_esc()

        elif key == S_KEY:  # Take screenshot
            self.screenshot()

        else:
            self.command_mode = False
        return None

    def first_escape(self):
        self.msg(ESC_MESSAGE)
        self.command_mode = True
        return None

    def screenshot(self):
        self.del_msg(ESC_MESSAGE)
        self.command_mode = False
        img = self.get_img()
        fileName = "{}.png".format(name_of_project[0:-3])
        img.SaveFile(fileName, wx.BITMAP_TYPE_PNG)


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

