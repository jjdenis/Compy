#!/usr/bin/env python
# -*- coding: utf-8 -*-

from compy.colors import colors
from compy.bitmaps import bitmap_images
from compy.create_web.html_examples import Examples
from compy.create_web.template_to_webpage import t2wp


def make_all_html():
    t2wp('index.html')
    t2wp('install.html')
    t2wp('examples.html')
    t2wp('commands.html')

    make_challenges_html()

    make_colors_html()
    make_keys_html()
    make_chars_html()



def make_challenges_html():

    challenges = Examples()

    challenges.new(title='Draw one line',
                   name='draw_line',
                   comments='Can you draw a yellow line like the one in this example?',
                   challenge =True)

    challenges.new(title='Sum two numbers',
                   name='sum_two_values',
                   comments='This is a simple example, ',
                   challenge =True)

    challenges.new(title='Guess the number',
                   name='guess_the_number',
                   comments='This is a simple example, ',
                   challenge =True)

    t2wp('challenges.html', challenges=challenges)


def make_chars_html():
    bitmaps = []
    for bitmap_code, bitmap_path in enumerate(bitmap_images):
        if bitmap_path:
            path = bitmap_path.replace('compy/chars', 'chars')
            bitmaps.append((bitmap_code, path))
    t2wp('chars.html', bitmaps=bitmaps)


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
    t2wp('keys.html', keys=keys)


def make_colors_html():
    clrs = []
    for col_code in range(0, 20):
        col_tup = colors.get_color(col_code)
        html_color = '#{:02X}{:02X}{:02X}'.format(col_tup[0], col_tup[1], col_tup[2])
        clrs.append((col_code,
                     colors.get_color_name(col_code),
                     html_color))
    t2wp('colors.html', colors=clrs)



