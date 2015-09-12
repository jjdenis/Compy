#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Bitmaps(object):
    def __init__(self, Bitmap):
        self.bitmaps = [None] * 400

        for dirpath, dirnames, filenames in os.walk('src/chars'):
            break

        for filename in filenames:
            if '.bmp' not in filename:
                continue
            try:
                char_id = int(filename.replace('.bmp', ''))
            except:
                continue
            if char_id < 0 or char_id > 400:
                continue
            bitmap = Bitmap('{}/{}'.format(dirpath, filename))
            bitmap.SetDepth(1)
            self.bitmaps[char_id] = bitmap

    def get_bitmap(self, code):
        bitmap=None
        try:
            bitmap = self.bitmaps[code]
        except:
            pass
        if not bitmap:
            bitmap = self.bitmaps[32]  # Sino menos Interrogation sign

        return bitmap

