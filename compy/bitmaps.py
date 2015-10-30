#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class BitmapImages(object):
    def __init__(self):
        self.images = [None] * 400
        self.populate()

    def populate(self):
        for dirpath, dirnames, filenames in os.walk('compy/chars'):
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

    def __iter__(self):
        """Makes 'for self in ...' work """
        for image in self.images:
              yield image

    def __getitem__(self, key):
        """Defines self[key] """
        return self.images[key]


bitmap_images = BitmapImages()

class Bitmaps(object):
    def __init__(self, Bitmap):
        self.bitmaps = [None] * 400

        for img_cod in range(0, 400):
            full_path= bitmap_images[img_cod]
            if full_path:
                bitmap = Bitmap(full_path)
                bitmap.SetDepth(1)
                self.bitmaps[img_cod] = bitmap

    def get_bitmap(self, code):
        bitmap=None
        try:
            bitmap = self.bitmaps[code]
        except:
            pass
        if not bitmap:
            bitmap = self.bitmaps[32]  # Sino menos Interrogation sign

        return bitmap

