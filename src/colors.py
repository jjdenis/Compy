#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

COLORS = [
    ('black'       , (   0,   0,   0) ),
    ('white'       , ( 255, 255, 255) ),
    ('red'         , ( 136,   0,   0) ),
    # cyan        , ( 0x66, 0xDA, 0xFF)
    ('cyan'        , ( 170, 255, 238) ),
    # 66 DA FF
    ('purple'      , ( 204,  68, 204) ),
    ('green'       , (   0, 204,  85) ),
    ('blue'        , (   0,  0, 170) ),
    ('yellow'      , ( 238, 238, 119) ),
    ('orange'      , ( 221,  136,  85) ),
    ('brown'       , ( 102,  68,  0) ),
    ('light_red'   , ( 255, 119,  119) ),
    ('dark_grey'   , (  51,  51,  51) ),
    ('grey'        , ( 119, 119, 119) ),
    #'light_green' , ( 170, 255, 102)
    ('light_green'  , ( 0x97, 0xFF, 0x97) ),
    # light_blue  , ( 0,  136, 255)
    ('light_blue'  , ( 0x97, 0x97, 0xFF) ),
    # 97 FF 97 8
    # light_blue  , ( 108,  94, 181)
    ('light_grey'  , ( 187, 187, 187) )
]

class Colors(object):

    def __init__(self):

        self.colors_by_name = {}
        self.colors_by_number = []
        self.color_name_list = []

        # self.black       = (0x00, 0x00, 0x00)
        # self.white       = (0xFF, 0xFF, 0xFF)
        # self.red         = (0xAB, 0x31, 0x26)
        # self.cyan        = (0x66, 0xDA, 0xFF)
        # self.purple      = (0xBB, 0x3F, 0xB8)
        # self.green       = (0x55, 0xCE, 0x58)
        # self.blue        = (0x1D, 0x0E, 0x97)
        # self.yellow      = (0xEA, 0xF5, 0x7C)
        # self.orange      = (0xB9, 0x74, 0x18)
        # self.brown       = (0x78, 0x53, 0x00)
        # self.light_red   = (0xDD, 0x93, 0x87)
        # self.dark_grey   = (0x5B, 0x5B, 0x5B)
        # self.grey        = (0x8B, 0x8B, 0x8B)
        # self.light_green = (0xB0, 0xF4, 0xAC)
        # self.light_blue  = (0xAA, 0x9D, 0xEF)
        # self.light_grey  = (0xB8, 0xB8, 0xB8)

        for name, value in COLORS:
            self.__dict__[name]=value
            self.colors_by_number.append(value)
            self.colors_by_name[name]=value
            self.color_name_list.append(name)

        for index, color_name in enumerate(self.color_name_list):
            print '{:>2} - {:<}'.format(index, color_name)

    def get_color(self, color_code):
        if isinstance(color_code, int):
            color = self.colors_by_number[color_code%16]
        elif isinstance(color_code, basestring):
            try:
                color = self.colors_by_name[color_code]
            except:
                name_and_match = process.extractOne(color_code, self.color_name_list)
                color_name = name_and_match[0]
                color = self.colors_by_name[color_name]
        else:
            color = color_code
        return color





colors = Colors()
# https://www.c64-wiki.com/index.php/Color


