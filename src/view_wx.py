#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import random
from time import time

from src.bitmaps import Bitmaps
from src.colors import colors

from src.settings import NUM_COLS, NUM_ROWS, CHAR_PTS_X, CHAR_PTS_Y, FRAME_PTS_X, FRAME_PTS_Y

ORG_ACTIVE_CNVS_X = FRAME_PTS_X
ORG_ACTIVE_CNVS_Y = FRAME_PTS_Y

ACTIVE_CNVS_PTS_X = NUM_COLS * CHAR_PTS_X+1
ACTIVE_CNVS_PTS_Y = NUM_ROWS * CHAR_PTS_Y+1

TOTAL_CNVS_PTS_X = ACTIVE_CNVS_PTS_X + 2 * FRAME_PTS_X
TOTAL_CNVS_PTS_Y = ACTIVE_CNVS_PTS_Y + 2 * FRAME_PTS_Y

ESCAPE = 27

# http://zetcode.com/wxpython/gdi/

class GUIwx(wx.App):
    def __init__(self, queue1, queue2):
        self.queue1 = queue1
        self.queue2 = queue2
        self.key_pressed = None
        self.frame = None
        self.canvas = None
        self.sound = None
        self.timer = None
        self.dc = None
        # self.app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
        self.cierra_por_esc = False
        self.pinta = None
        wx.App.__init__(self, False)

    def OnInit(self):
        self.frame = self.set_frame()
        self.canvas = self.set_canvas(self.frame)
        self.sound = wx.Sound('res/sonido.mp3')
        self.timer = self.set_timer(self.canvas)
        self.pinta = Pinta(self.canvas)
        return True

    def run(self):
        self.frame.Show(True) # Show the frame.
        self.MainLoop()

    def stop(self):
        self.OnClose(1)

    def OnClose(self, event):
        self.timer.Stop()
        self.frame.Destroy()

    def set_frame(self):
        frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
        frame.SetClientSize((TOTAL_CNVS_PTS_X, TOTAL_CNVS_PTS_Y))
        frame.Bind(wx.EVT_CLOSE, self.OnClose)
        frame.Move((30,30)) # Pone la ventana arriba a la izquierda
        return frame

    def set_canvas(self, frame):
        canvas = wx.ScrolledWindow(frame)
        canvas.SetClientSize((TOTAL_CNVS_PTS_X, TOTAL_CNVS_PTS_Y))
        canvas.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        canvas.Refresh()
        canvas.Bind(wx.EVT_KEY_DOWN, self.on_key)
        canvas.Bind(wx.EVT_KEY_UP, self.on_key_release)
        return canvas

    def set_timer(self, canvas):
        timer = wx.Timer(canvas)
        canvas.Bind(wx.EVT_TIMER, self.on_timer, timer)
        timer.Start(10) # ms
        return timer

    def on_key(self, event):
        key = event.GetKeyCode()
        if key == ESCAPE:
            self.cierra_por_esc = True
            self.envia_comando('closing', None, None)
        # self.sound.Play(wx.SOUND_ASYNC)
        # self.pinta_bloque(0, 0, color="blue")
        # self.pinta_bloque(5, 5, color="blue")
        if key != self.key_pressed:
            self.envia_comando('key_pressed', key, time())
            self.key_pressed = key

    def on_key_release(self, event):
        key = event.GetKeyCode()
        self.envia_comando('key_released', key, time())
        print 'v released', key
        self.key_pressed = None

    def envia_comando(self, *args):
        commands = list(args)
        self.queue2.put(commands)

    def on_timer(self, event):

        while not self.queue1.empty():
            msg = self.queue1.get()
            comando = msg[0]
            args = msg[1:]

            if comando == 'poke':
                self.pinta.poke(*args)

            elif comando == 'reset_canvas':
                self.pinta.reset_canvas(fm_color=args[0], bg_color=args[1])

            elif comando == 'close_window':
                self.stop()

        if self.cierra_por_esc:
            self.stop()


class Pinta(object):

    def __init__(self, canvas):
        self.canvas = canvas
        self.bitmaps = Bitmaps(wx.Bitmap)

    def reset_canvas(self, fm_color, bg_color):
        self.set_deep_background(fm_color)
        self.set_background(bg_color)

    def poke(self, x, y, char_id, fg_color, bg_color):

        dcx, dcy = self.to_window_units(x, y)

        dc = wx.WindowDC(self.canvas)

        bmp = self.bitmaps.get_bitmap(char_id)
        print "En canvas", char_id
        print bmp

        dc.BeginDrawing()
        dc.SetTextForeground(fg_color)
        dc.SetTextBackground(bg_color)
        dc.DrawBitmap(bmp, dcx, dcy, useMask= False)
        dc.EndDrawing()
        self.canvas.Refresh()

    def to_window_units(self, x, y):
        dcx = FRAME_PTS_X + x * 16
        dcy = TOTAL_CNVS_PTS_Y - FRAME_PTS_Y - (y + 1) * 16
        return dcx, dcy

    def set_deep_background(self, color):
        dc = wx.WindowDC(self.canvas)
        dc.BeginDrawing()
        dc.SetPen(wx.Pen(color, 1, wx.TRANSPARENT))
        dc.SetBrush(wx.Brush(color, wx.SOLID))
        dc.DrawRectangle(0, 0, TOTAL_CNVS_PTS_X, TOTAL_CNVS_PTS_Y)
        dc.EndDrawing()
        self.canvas.Refresh()

    def set_background(self, color):
        dc = wx.WindowDC(self.canvas)
        dc.BeginDrawing()
        dc.SetPen(wx.Pen(color, 1, wx.TRANSPARENT))
        dc.SetBrush(wx.Brush(color, wx.SOLID))
        dc.DrawRectangle(FRAME_PTS_X, FRAME_PTS_Y, ACTIVE_CNVS_PTS_X, ACTIVE_CNVS_PTS_Y)
        dc.EndDrawing()
        self.canvas.Refresh()


class Q(object):
    def get(self):
        x = int(random.random()*40)
        y = int(random.random()*20)
        code = int(random.random()*24)+32

        return ['poke', x, y, code, (255,255,255)]
    def put(self, comando):
        pass
    def empty(self):
        a = random.choice([True, True, True, True, True, True, True, False])
        return a


if __name__ == '__main__':
    from src.colors import Colors
    colors = Colors()

    q1 = Q()
    q2 = Q()
    gui = GUIwx(q1, q2, colors)
    gui.frame.Show(True) # Show the frame.
    gui.MainLoop()
