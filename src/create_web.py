#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import markdown2
from jinja2 import Environment, PackageLoader
import wx
import os
import __main__
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

name_of_project= __main__.__file__.split('/')[-1].replace('.py', '')
env = Environment(loader=PackageLoader('src', 'templates'))

def make_html_challenges():

    template = env.get_template('challenges.html')

    md_text = template.render(prueba='variables')

    # html_text = markdown2.markdown(md_text)
    f = codecs.open('docs/challenges.html', 'w', 'utf-8')
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
