#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
from jinja2 import Environment, PackageLoader
import wx
from src.colors import colors
from src.bitmaps import char_images
import __main__
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

name_of_project= __main__.__file__.split('/')[-1].replace('.py', '')
env = Environment(loader=PackageLoader('src', 'templates'))

def make_all_html():
    make_html('challenges.html', prueba='variables')
    make_html('index.html')
    make_html('install.html')
    make_html('examples.html')
    clrs = []
    for col_code in range(0, 20):
        col_tup =colors.get_color(col_code)
        html_color = '#{:02X}{:02X}{:02X}'.format(col_tup[0],col_tup[1], col_tup[2])
        clrs.append((col_code,
                    colors.get_color_name(col_code),
                    html_color))
    allowed_keys="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ<,.-+'"
    keys=[]
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

    make_html('reference.html', colors = clrs, keys=keys)


def make_html(name_html, **kwargs):

    template = env.get_template(name_html)

    md_text = template.render(**kwargs)

    final_path = 'docs/{}'.format(name_html)
    f = codecs.open(final_path, 'w', 'utf-8')
    f.write(md_text)
    f.close()

def save_img(img):
    # fn=dtm.datetime.now().strftime('%dd%HH%MM%SS')
    fileName = "docs/img/{}.png".format(name_of_project)
    img.SaveFile(fileName, wx.BITMAP_TYPE_PNG)

def take_code():
    print name_of_project
    fn = '{}.py'.format(name_of_project)
    f = codecs.open(fn, 'r', 'utf-8')
    code = f.read()
    code_html = highlight(code, PythonLexer(), HtmlFormatter())

    f.close()

    fn = 'src/templates/{}.html'.format(name_of_project)
    f = codecs.open(fn, 'w', 'utf-8')
    f.write(code_html)
    f.close()
