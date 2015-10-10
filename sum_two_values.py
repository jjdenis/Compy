#!/usr/bin/env python
#  -*- coding: utf-8 -*-


from time import sleep
from src.run import run

def main(scrn):

    scrn.clear_screen()

    scrn.printf()
    scrn.printf('    SUM OF TWO VALUES', color = 4)
    scrn.printf('    =================')

    value_one = scrn.input("Give me one value: ")
    value_two = scrn.input("Give me another value: ")

    sum_of_values = value_one + value_two

    scrn.printf('The sum of {} and {} is {}'.format(
        value_one, value_two, sum_of_values), color=6)

run(main)


