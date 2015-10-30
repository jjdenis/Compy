#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from time import sleep


def programa_principal():
    scr.clear_screen()
    scr.printf('')
    scr.printf('Sum two values challenge'.upper().center(39), color=6)
    scr.printf('')
    scr.set_name_of_project('sum_two_values')
    v1 = scr.input('Give me one value: ', color=10)
    v2 = scr.input('Give me another value: ')
    scr.printf()
    ans = 'The sum of {} and {} is {}'.format(v1, v2, v1+v2)
    scr.printf(ans)

def dame_el_doble(numero):
    return numero+numero+1

def otro():
    inicio_ana()

    while True:
        opi = input_scrn("Dime un numero ")
        print_scrn(opi, color=opi)
        print_scrn('Hola', color=opi)
        print_scrn(opi, color=0)


def inicio_ana():
    clear_scrn()
    bg_color_scrn(4)

    fm_color_scrn(6)
    print_scrn()
    num_color = 0
    while num_color<16:
        print_scrn('           hola ', color=num_color, next_line=False)
        print_scrn(num_color)
        sleep(0.1)
        num_color = num_color+1

    num_color=0
    while num_color<21:
        bg_color_scrn(num_color)
        sleep(0.1)
        num_color = num_color+1

    num_color=0
    while num_color<23:
        fm_color_scrn(num_color)
        sleep(0.1)
        num_color = num_color+1


    clear_scrn()













##################
##################

from compy.run import run
def pg(screen):
    global scr, print_scrn, bg_color_scrn, fm_color_scrn, clear_scrn, input_scrn, colors_scrn
    scr=screen
    print_scrn=scr.printf
    bg_color_scrn=scr.set_bg_color
    fm_color_scrn=scr.set_fm_color
    clear_scrn = scr.clear_screen
    input_scrn = scr.input
    colors_scrn =scr.colors
    programa_principal()
run(pg)

##################
##################



unichar = [

    (0,  u'♥',  'Black Heart Suit'),
    (1,  u'♣',  'Black Club Suit'),
    (2,  u'♦',  'Black Diamond Suit'),
    (3,  u'♠',  'Black Spade Suit'),
    (4,  u'●',  'Black Circle'),
    (5,  u'○',  'White Circle'),
    (6,  u'π',  'Greek Small Letter Pi'),
    (7,  u'£',  'Pound Sign'),
    (8,  u'◤',  'Black Upper Left Triangle'),
    (9,  u'◥',  'Black Upper Right Triangle'),

    (31,   u'█',   'Full Block'),
    (32,   u' ',   'Space'),
    (33,   u'!',   'Exclamation mark'),
    (34,   u'"',   'Double quotes (or speech marks)'),
    (35,   u'#',   'Number'),
    (36,   u'$',   'Dollar'),
    (37,   u'%',   'Procenttecken'),
    (38,   u'&',   'Ampersand'),
    (39,   u"'",   'Single quote'),
    (40,   u'(',   'Open parenthesis (or open bracket)'),
    (41,   u')',   'Close parenthesis (or close bracket)'),
    (42,   u'*',   'Asterisk'),
    (43,   u'+',   'Plus'),
    (44,   u',',   'Comma'),
    (45,   u'-',   'Hyphen'),
    (46,   u'.',   'Period, dot or full stop'),
    (47,   u'/',   'Slash or divide'),
    (48,   u'0',   'Zero'),
    (49,   u'1',   'One'),
    (50,   u'2',   'Two'),
    (51,   u'3',   'Three'),
    (52,   u'4',   'Four'),
    (53,   u'5',   'Five'),
    (54,   u'6',   'Six'),
    (55,   u'7',   'Seven'),
    (56,   u'8',   'Eight'),
    (57,   u'9',   'Nine'),
    (58,   u',',   'Colon'),
    (59,   u';',   'Semicolon'),
    (60,   u'<',   'Less than (or open angled bracket)'),
    (61,   u'=',   'Equals'),
    (62,   u'>',   'Greater than (or close angled bracket)'),
    (63,   u'?',   'Question mark'),
    (64,   u'@',   'At symbol'),
    (65,   u'A',   'Uppercase A'),
    (66,   u'B',   'Uppercase B'),
    (67,   u'C',   'Uppercase C'),
    (68,   u'D',   'Uppercase D'),
    (69,   u'E',   'Uppercase E'),
    (70,   u'F',   'Uppercase F'),
    (71,   u'G',   'Uppercase G'),
    (72,   u'H',   'Uppercase H'),
    (73,   u'I',   'Uppercase I'),
    (74,   u'J',   'Uppercase J'),
    (75,   u'K',   'Uppercase K'),
    (76,   u'L',   'Uppercase L'),
    (77,   u'M',   'Uppercase M'),
    (78,   u'N',   'Uppercase N'),
    (79,   u'O',   'Uppercase O'),
    (80,   u'P',   'Uppercase P'),
    (81,   u'Q',   'Uppercase Q'),
    (82,   u'R',   'Uppercase R'),
    (83,   u'S',   'Uppercase S'),
    (84,   u'T',   'Uppercase T'),
    (85,   u'U',   'Uppercase U'),
    (86,   u'V',   'Uppercase V'),
    (87,   u'W',   'Uppercase W'),
    (88,   u'X',   'Uppercase X'),
    (89,   u'Y',   'Uppercase Y'),
    (90,   u'Z',   'Uppercase Z'),
    (91,   u'[',   'Opening bracket'),
    (92,   u'\\',  'Backslash'),
    (93,   u']',   'Closing bracket'),
    (94,   u'^',   'Caret - circumflex'),
    (95,   u'_',   'Underscore'),
    (96,   u'`',   'Grave accent'),
    (97,   u'a',   'Lowercase a'),
    (98,   u'b',   'Lowercase b'),
    (99,   u'c',   'Lowercase c'),
    (100,  u'd',   'Lowercase d'),
    (101,  u'e',   'Lowercase e'),
    (102,  u'f',   'Lowercase f'),
    (103,  u'g',   'Lowercase g'),
    (104,  u'h',   'Lowercase h'),
    (105,  u'i',   'Lowercase i'),
    (106,  u'j',   'Lowercase j'),
    (107,  u'k',   'Lowercase k'),
    (108,  u'l',   'Lowercase l'),
    (109,  u'm',   'Lowercase m'),
    (110,  u'n',   'Lowercase n'),
    (111,  u'o',   'Lowercase o'),
    (112,  u'p',   'Lowercase p'),
    (113,  u'q',   'Lowercase q'),
    (114,  u'r',   'Lowercase r'),
    (115,  u's',   'Lowercase s'),
    (116,  u't',   'Lowercase t'),
    (117,  u'u',   'Lowercase u'),
    (118,  u'v',   'Lowercase v'),
    (119,  u'w',   'Lowercase w'),
    (120,  u'x',   'Lowercase x'),
    (121,  u'y',   'Lowercase y'),
    (122,  u'z',   'Lowercase z'),
    (123,  u'{',   'Opening brace'),
    (124,  u'|',   'Vertical bar'),
    (125,  u'}',   'Closing brace'),
    (126,  u'’',   'Right Single Quotation Mark'),
    (127,  u'>',   'Greater-than Sign'),

    (126,  u'→',  'Rightwards Arrow'),
    (127,  u'↓',  'Downwards Arrow'),
    (128,  u'←',  'Leftwards Arrow'),
    (129,  u'↑',  'Upwards Arrow'),

    (250, u'┏',  'Box Drawings Heavy Down And Right'),
    (251, u'┓',  'Box Drawings Heavy Down And Left'),
    (252, u'┛',  'Box Drawings Heavy Up And Left'),
    (253, u'┗',  'Box Drawings Heavy Up And Right'),
    (254, u'━',  'Box Drawings Heavy Horizontal'),
    (255, u'┃',  'Box Drawings Heavy Vertical'),
    (256, u'┳',  'Box Drawings Heavy Down And Horizontal'),
    (257, u'┫',  'Box Drawings Heavy Vertical And Left'),
    (258, u'┻',  'Box Drawings Heavy Up And Horizontal'),
    (259, u'┣',  'Box Drawings Heavy Vertical And Right'),
    (260, u'╋',  'Box Drawings Heavy Vertical And Horizontal'),
    (261, u'╭',  'Box Drawings Light Arc Down And Right'),
    (262, u'╮',  'Box Drawings Light Arc Down And Left'),
    (263, u'╯',  'Box Drawings Light Arc Up And Left'),
    (264, u'╰',  'Box Drawings Light Arc Up And Right'),

]