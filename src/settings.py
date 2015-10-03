#!/usr/bin/env python
# -*- coding: utf-8 -*-


NUM_COLS = 40
NUM_ROWS = 25

CHAR_PTS_X = 16
CHAR_PTS_Y = 16

FRAME_CHARS_X = 4
FRAME_CHARS_Y = 4

FRAME_PTS_X = FRAME_CHARS_X * CHAR_PTS_X
FRAME_PTS_Y = FRAME_CHARS_Y * CHAR_PTS_Y


INIT_MSG =  """
      **** DENIS SISTEMA POKE ****
Pulsa la tecla "escape" para salir

"""

NUMBER_OF_COLORS = 20

from src.colors import colors

INIT_FM_COLOR = colors.cyan
INIT_BG_COLOR = colors.white
INIT_CH_COLOR = colors.blue

