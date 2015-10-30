#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from settings import NUMBER_OF_COLORS

COLORS = [
    ('light_blue'  , ( 0xa6, 0xce, 0xe3) ),
    ('blue'        , (   0x1f,  0x78, 0xb4) ),
    ('light_green'  , ( 0xb2, 0xdf, 0x8a) ),
    ('green'       , (   0x33, 0xa0,  0x2c) ),
    ('pink'       , (   0xfb,   0x9a,   0x99) ),
    ('red'         , ( 0xe3,   0x1a,   0x1c) ),
    ('light_orange'      , ( 0xfd,  0xbf,  0x6f) ),
    ('orange'      , ( 0xff,  0x7f,  0x00) ),
    ('light_violet'      , ( 0xca,  0xb2, 0xd6) ),
    ('violet'      , ( 0x6a,  0x3d, 0x9a) ),
    ('yellow'      , ( 0xff, 0xff, 0x99) ),
    ('brown'       , ( 0xb1,  0x59,  0x28) ),
    ('white'       , ( 255, 255, 255) ),
    ('light_grey'  , ( 0xe0, 0xe0, 0xe0) ),
    ('grey'   , (  0x80,  0x80,  0x80) ),
    ('dark_grey'        , ( 0x40, 0x40, 0x40) ),
    ('black'       , (   0x0,   0x0,   0x0) ),
    # ('red'         , ( 136,   0,   0) ),
    # ('red1'         , ( 255,   21,   0) ),
    # cyan        , ( 0x66, 0xDA, 0xFF)
    # ('cyan'        , ( 0x66, 0xDA, 0xFF)),
    ('cyan'        , ( 0x00, 0xEB, 0xFF)),
    ('purple'   , ( 0xb7, 0x40,  0xff) ),
    ('deep_pink'   , ( 0xff, 0x14,  0x93) ),
    # ('hot_pink'   , ( 0xff, 0x69,  0xb4) ),

    # ('brown'       , ( 102,  68,  0) ),
    # ('light_red'   , ( 255, 119,  119) ),
    # ('orange'      , ( 221,  136,  85) ),
    # ('cyan'        , ( 170, 255, 238) ),
    # 66 DA FF
    #'light_green' , ( 170, 255, 102)
    # light_blue  , ( 0,  136, 255)
    # 97 FF 97 8
    # light_blue  , ( 108,  94, 181)
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

        # for index, color_name in enumerate(self.color_name_list):
        #     print '{:>2} - {:<}'.format(index, color_name)

    def get_color(self, color_code):
        if isinstance(color_code, int):
            color = self.colors_by_number[color_code%NUMBER_OF_COLORS]
        elif isinstance(color_code, basestring):
            try:
                color = self.colors_by_name[color_code]
            except:
                name_and_match = process.extractOne(color_code, self.color_name_list)
                color_name = name_and_match[0]
                color = self.colors_by_name[color_name]
        else:
            color = color_code
        print "Returned color {}".format(color)
        return color

    def get_color_name(self, color_code):
        if isinstance(color_code, int):
            color_name = self.color_name_list[color_code%NUMBER_OF_COLORS]
        else:
             color_name = color_code
        return color_name


colors = Colors()
# https://www.c64-wiki.com/index.php/Color


"""
    ('white'       , ( 255, 255, 255) ),
    ('red'         , ( 136,   0,   0) ),
    ('red1'         , ( 255,   21,   0) ),
    # cyan        , ( 0x66, 0xDA, 0xFF)
    # ('cyan'        , ( 0x66, 0xDA, 0xFF)),
    ('cyan'        , ( 0x00, 0xEB, 0xFF)),
    ('purple'      , ( 204,  68, 204) ),
    ('green'       , (   0, 204,  85) ),
    ('blue'        , (   0,  0, 170) ),
    ('yellow'      , ( 238, 238, 119) ),

    ('orange'      , ( 221,  136,  85) ),
    ('brown'       , ( 102,  68,  0) ),
    ('light_red'   , ( 255, 119,  119) ),
    ('dark_grey'   , (  51,  51,  51) ),
    ('grey'        , ( 119, 119, 119) ),
    ('light_green'  , ( 0x97, 0xFF, 0x97) ),
    ('light_blue'  , ( 0x97, 0x97, 0xFF) ),
    ('light_grey'  , ( 187, 187, 187) ),

"""