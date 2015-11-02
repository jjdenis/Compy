#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil

import wx

from compy.colors import colors
from compy.bitmaps import bitmap_images
from compy.create_web.create_web_examples import Examples
from compy.create_web.make_html import make_html

import __main__
name_of_project= __main__.__file__.split('/')[-1]

print __main__.__file__

from ..settings import DOCS_PATH

def make_all_html():
    make_html('index.html')
    make_html('install.html')
    make_html('examples.html')
    make_html('commands.html')

    make_colors_html()

    make_keys_html()

    make_chars_html()

    make_challenges_html()


def make_challenges_html():

    challenges = Examples()
    challenges.add(title='Sum two numbers',
                   name='sum_two_values',
                   comments='This is a simple example, ',
                   code='sample_code 1',
                   challenge =True)

    challenges.add(title='Guess the number',
                   name='guess_the_number',
                   comments='This is a simple example, ',
                   code='sample_code 1',
                   challenge =True)

    make_html('challenges.html', challenges=challenges)


def make_chars_html():
    bitmaps = []
    for bitmap_code, bitmap_path in enumerate(bitmap_images):
        if bitmap_path:
            path = bitmap_path.replace('compy/chars', 'chars')
            bitmaps.append((bitmap_code, path))
    make_html('chars.html', bitmaps=bitmaps)


def make_keys_html():
    allowed_keys = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ<,.-+'"
    keys = []
    for key_rep in allowed_keys:
        keys.append((ord(key_rep), key_rep))
    keys.append((314, 'left arrow'))
    keys.append((315, 'up arrow'))
    keys.append((316, 'right arrow'))
    keys.append((317, 'down arrow'))
    keys.append((13, 'enter'))
    keys.append((32, 'space'))
    keys.append((396, 'ctrl'))
    keys.append((306, 'upper'))
    keys.append((307, 'alt'))
    keys.append((308, 'command'))
    keys.append((8, 'backspace'))
    make_html('keys.html', keys=keys)


def make_colors_html():
    clrs = []
    for col_code in range(0, 20):
        col_tup = colors.get_color(col_code)
        html_color = '#{:02X}{:02X}{:02X}'.format(col_tup[0], col_tup[1], col_tup[2])
        clrs.append((col_code,
                     colors.get_color_name(col_code),
                     html_color))
    make_html('colors.html', colors=clrs)


def save_img(img):
    # fn=dtm.datetime.now().strftime('%dd%HH%MM%SS')
    fileName = "docs/img/{}.png".format(name_of_project)
    img.SaveFile(fileName, wx.BITMAP_TYPE_PNG)

def take_code():
    fno = __main__.__file__
    fnc = DOCS_PATH + 'temp/{}'.format(name_of_project)
    shutil.copyfile(fno, fnc)



