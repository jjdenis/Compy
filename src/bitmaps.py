#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class CharImages(object):
    def __init__(self):
        self.images = [None] * 400
        self.populate()

    def populate(self):
        for dirpath, dirnames, filenames in os.walk('src/chars'):
            break

        for filename in filenames:
            if '.bmp' not in filename:
                continue
            try:
                img_cod = int(filename.replace('.bmp', ''))
            except:
                continue
            if img_cod < 0 or img_cod > 400:
                continue
            full_path= '{}/{}'.format(dirpath, filename)
            self.images[img_cod] = full_path

char_images = CharImages()

class Bitmaps(object):
    def __init__(self, Bitmap):
        self.bitmaps = [None] * 400

        for img_cod in range(0, 400):
            full_path= char_images[img_cod]
            if full_path:
                bitmap = Bitmap(full_path)
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

