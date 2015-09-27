#!/usr/bin/env python
# -*- coding: utf-8 -*-

# git push blanco master
# En final: git pull

import traceback
import multiprocessing

from src.control import Control

from src import view_wx as view


def run_control(queue1, queue2, main):
    try:
        control = Control(queue1, queue2)
        main(control)
        # main finishes here
        # control.stop()
    except:
        print "FATAL: exited while multiprocessing".format()
        traceback.print_exc()


def run(main):

    q_to_view = multiprocessing.Queue()

    q_from_view = multiprocessing.Queue()

    control_parallel = multiprocessing.Process(
        target=run_control,
        args=(q_to_view, q_from_view, main))

    control_parallel.start()

    gui = view.GUIwx(q_to_view, q_from_view)
    gui.run()

    print("Gui terminada")

    while not q_to_view.empty():
        q_to_view.get()
    while not q_from_view.empty():
        q_from_view.get()

    q_to_view.close()
    q_from_view.close()
    q_to_view.join_thread()
    q_from_view.join_thread()

    control_parallel.terminate()
    control_parallel.join()

    print("Control terminada")
