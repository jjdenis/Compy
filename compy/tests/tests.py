#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from wait_time import sleep
import random

A = 65
B = 66
Q = 81
DCHA = 316
IZDA = 314
ABAJO = 317
ARRIBA = 315
ENTER = 13

def programa_principal():

    demo_primera()
    demo_colores()
    demo_bg_color()
    demo_fm_color()
    demo_input()
    demo_printf()
    demo_print_sin_texto()
    demo_print_misma_linea()
    demo_print_colores()
    demo_unicode()
    demo_unicode_move()
    demo_cod_tecla()
    demo_mapa_caracteres()
    demo_poke_movimiento()

    #scr.stop()



def demo_primera():
    scr.clear_screen()
    scr.printf("¡¡That is how you print in the screen!!!")
    scr.wait_key()

def demo_colores():
    scr.colors()



def demo_bg_color():
    scr.clear_screen()
    scr.printf('', color=5)
    scr.xyprint(0, 24, "¡¡Así se cambia el color de fondo!!!")
    scr.xyprint(5, 1, "Pulsa tres veces cualquier tecla para ver colores")

    color = 0
    i = 0
    while True:
        scr.xyprint(0, 22, 'Color numero: ', color)
        scr.set_bg_color(color)
        k=scr.wait_key()
        color = random.randint(0, 19)
        if k == 13:
            i= i+1
            if i == 3:
                break
    scr.set_bg_color(0)


def demo_fm_color():
    scr.clear_screen()
    scr.xyprint(0,24,"¡¡Así se cambia el color del marco!!!")
    scr.xyprint(5,1,"Pulsa cualquier tecla para cambiar")
    scr.xyprint(15,0,"Pulsa q para continuar")

    color = 0
    i=0
    while True:
        scr.xyprint(0, 22, 'Color =', color)
        scr.set_fm_color(color)
        color = random.randint(0, 100)
        k=scr.wait_key()
        if k == 13:
            i= i+1
            if i == 3:
                break



def demo_input():
    scr.clear_screen()
    a = scr.input('Dime tu nombre')
    if not a:
        a = 'sin nombre'
    scr.printf("Hola " + a)
    scr.wait_key()

def demo_printf():
    scr.clear_screen()
    scr.printf("Hola Juanjo!!")
    scr.printf("Hola Juanjo!!")
    scr.printf("Hola Juanjo!!")
    scr.printf("Hola Juanjo!!")
    scr.printf("Hola Juanjo!!")
    scr.printf("Hola Juanjo!!")
    scr.wait_key()

def demo_print_sin_texto():
    scr.clear_screen()
    scr.printf("Hola Juanjo!!")
    scr.printf("Hola Juanjo!!")
    scr.printf("Hola Juanjo!!")
    scr.printf("")
    scr.printf("Hola Juanjo!!")
    scr.printf("Hola Juanjo!!")
    scr.printf()
    scr.printf("Hola Juanjo!!")
    scr.wait_key()


def demo_print_misma_linea():
    scr.clear_screen()
    scr.printf("Hola Juanjo!!", stay=True)
    scr.printf("Hola Juanjo!!")
    scr.printf("Hola Juanjo!!")
    scr.printf("")
    scr.printf("Hola Juanjo!!")
    scr.printf("Hola Juanjo!!", stay=True)
    scr.printf("Hola Juanjo!!")
    scr.wait_key()


def demo_print_colores():
    scr.clear_screen()
    for i in range(0, 100):
        scr.printf(u'Hola', i, stay=True)


def demo_unicode():
    scr.clear_screen()

    while True:
        a = scr.check_key()
        if a:
            break
        scr.clear_screen()
        scr.printf(u'╭o╮')
        sleep(0.3)
        scr.clear_screen()
        scr.printf(u'╰o╯')
        sleep(0.3)


def demo_unicode_move():
    scr.clear_screen()
    i = 0
    while i < 20:
        a = scr.check_key()
        if a:
            break
        espacio=' '*i
        i=i+1
        scr.clear_screen()
        scr.printf(espacio + u'╭o╮')
        sleep(0.3)
        scr.clear_screen()
        espacio=' '*i
        i=i+1
        scr.printf(espacio + u'╰o╯')
        sleep(0.3)


def demo_cod_tecla():
    scr.clear_screen()
    scr.printf('Pulsa una tecla')
    i=0
    while True:
        a = scr.wait_key()
        scr.clear_screen()
        scr.printf('El código de tecla pulsado es ' + str(a))
        scr.printf('Pulsa una tecla')
        if a==13:
            i=i+1
            if i==3:
                break

def demo_mapa_caracteres():
    scr.mapa()


def demo_poke_movimiento():
    scr.clear_screen()

    x = 0
    y = 0
    scr.poke(x, y, B, 'light_green')
    scr.poke(10, 20, A, 'light_green')
    scr.poke(5, 5, A, 'light_green')
    while True:
        a = scr.check_key()
        if not a:
            continue
        scr.poke(x, y, None, 'red')
        if a == DCHA:
            x += 1
        elif a == IZDA:
            x -= 1
        elif a == ARRIBA:
            y += 1
        elif a == ABAJO:
            y += -1
        elif a == Q: # q
            break
        else:
            pass

        if scr.peek(x, y+1) == A:
            scr.poke(x, y, B, 'red')
        else:
            scr.poke(x, y, B, 'light_red')

def demo12():
    pass



##################
##################

from compy.run import run
def pg(screen):
    global scr
    scr=screen
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