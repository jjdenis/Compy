#!/usr/bin/env python
# -*- coding: utf-8 -*-

TITLE = 'Project Compy'
NUM_COLS = 40
NUM_ROWS = 25

CHAR_PTS_X = 16
CHAR_PTS_Y = 16

FRAME_CHARS_X = 4
FRAME_CHARS_Y = 4

FRAME_PTS_X = FRAME_CHARS_X * CHAR_PTS_X
FRAME_PTS_Y = FRAME_CHARS_Y * CHAR_PTS_Y


INIT_MSG =  """
      **** PROJECT COMPY V0.5 ****

"""

NUMBER_OF_COLORS = 20

INIT_FM_COLOR = 'ligh_blue'
INIT_BG_COLOR = 'blue'
INIT_CH_COLOR = 'light_blue'

ESC_MESSAGE = u'esc:exit s:screenshot'

# Two modes of operation, if True, it helps with docs
# this is for development.
# If false, the screenshots will be in the base path.
# This is for use after pip install
SAVE_TO_DOCS_PATH = True

DOCS_PATH   = u'/Users/jjdenis/Dropbox/Familia/Programas/poke/poke/docs/'
SSHOTS_PATH = u'/Users/jjdenis/Dropbox/Familia/Programas/poke/poke/docs/img/'
CODE_PATH   = u'/Users/jjdenis/Dropbox/Familia/Programas/poke/poke/docs/code/'
