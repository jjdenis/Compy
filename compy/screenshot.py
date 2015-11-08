#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import wx

import __main__

name_of_project= __main__.__file__.split('/')[-1]

print __main__.__file__

from compy.settings import SSHOTS_PATH, CODE_PATH


class CodeScreenshot(object):

    def __init__(self, get_img):
        self.set_paths()
        self.take_code()
        img = get_img()
        self.save_img(img)

    def set_paths(self):
        pass

    def save_img(self, img):
        # fn=dtm.datetime.now().strftime('%dd%HH%MM%SS')
        fileName = self.sshots_dir+"{}.png".format(name_of_project[0:-3])
        img.SaveFile(fileName, wx.BITMAP_TYPE_PNG)

    def take_code(self):
        pass


class CodeScreenShotSimple(CodeScreenshot):

    def set_paths(self):
        self.sshots_dir = 'screenshots/'
        self.ensure_dir(self.sshots_dir)

    def take_code(self):
        pass

    def ensure_dir(self, dir_name):
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)


class CodeScreenShotDocs(CodeScreenshot):
    def set_paths(self):
        self.sshots_dir = SSHOTS_PATH
        self.code_dir = CODE_PATH

    def take_code(self):
        fno = __main__.__file__
        fnc = self.code_dir + '{}'.format(name_of_project)
        shutil.copyfile(fno, fnc)