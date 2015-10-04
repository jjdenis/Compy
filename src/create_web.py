#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import markdown2
from jinja2 import Environment, PackageLoader
import wx
import os

env = Environment(loader=PackageLoader('src', 'templates'))

def make_html_challenges():

    template = env.get_template('challenges.md')

    md_text = template.render(prueba='variables')

    html_text = markdown2.markdown(md_text)
    f = codecs.open('docs/challenges.html', 'w', 'utf-8')
    f.write(html_text)
    f.close()

def TakeScreenShot(name_of_project, frame):
    if not name_of_project:
        return
    os.system('screencapture docs/img/scr.png')
    screen = wx.Bitmap('docs/img/scr.png')
    rect = frame.GetRect()
    bitmap = screen.GetSubBitmap(rect)
    img = bitmap.ConvertToImage()
    # fn=dtm.datetime.now().strftime('%dd%HH%MM%SS')
    fileName = "docs/img/{}.png".format(name_of_project)
    img.SaveFile(fileName, wx.BITMAP_TYPE_PNG)

def take_code(name_of_project):
    if not name_of_project:
        return
    print fn
    fn = '{}.py'.format(name_of_project)
    f = codecs.open(fn, 'r', 'utf-8')
    code = f.read()
    f.close()

    fn = 'docs/{}.ppy'.format(name_of_project)
    f = codecs.open(fn, 'w', 'utf-8')
    f.write(code)
    f.close()
