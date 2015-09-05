#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Chars(object):
    def __init__(self, Bitmap):
        self.chars = [None] * 400

        for dirpath, dirnames, filenames in os.walk('src/chars'):
            break

        for filename in filenames:
            if '.bmp' not in filename:
                continue
            bitmap = Char(dirpath, filename, Bitmap)
            if bitmap.code >= 0 and bitmap.code < 400:
               self.chars[bitmap.code] = bitmap

    def get_bitmap(self, code):
        try: # As an int
            char = self.chars[code]
        except:
            try: # As a char
                char = self.chars[ord(code)]
            except:
                char = None

        if not char: # No problemo, I'll get you something!

            char = self.chars[63]  # Interrogation sign

        return char.bitmap

    def as_string(self, code):
        try: # As an int
            char = self.chars[code]
        except:
            try: # As a char
                char = self.chars[ord(code)]
            except:
                char = None

        if not char: # No problemo, I'll get you something!

            char = self.chars[63]  # Interrogation sign

        return char.string




class Char(object):

    def __init__(self, dirpath, filename, Bitmap):
        self.bitmap = Bitmap('{}/{}'.format(dirpath, filename))
        self.bitmap.SetDepth(1)
        self.code = int(filename.replace('.bmp', ''))
        self.string = None
        self.find_string()

    def find_string(self):
        try:
            self.string = unichar[self.code]
        except:
            self.string = u'#'


    def __repr__(self):
        return "code: {}, char:{}".format(self.code, chr(self.code))

        # if code in self.used_bitmaps.keys():
        #     return self.used_bitmaps[code]
        # try:
        #     self.used_bitmaps[code] = bmp
        # except:
        #     if 222 in self.used_bitmaps.keys():
        #         bmp = self.used_bitmaps[222]
        #     else:
        #         bmp = wx.Bitmap('chars/{:03}.bmp'.format(222))
        #         bmp.SetDepth(1)
        #         self.used_bitmaps[222] = bmp


unichar = {


    0:  u'♥',  # Black Heart Suit
    1:  u'♣',  # Black Club Suit
    2:  u'♦',  # Black Diamond Suit
    3:  u'♠',  # Black Spade Suit
    4:  u'●',  # Black Circle
    5:  u'○',  # White Circle
    6:  u'•',  # Bullet

    8:  u'✓',  # Check Mark
    9:  u'π',  # Greek Small Letter Pi
    10: u'£',  # Pound Sign

    12: u'◤',  # Black Upper Left Triangle
    13: u'◥',  # Black Upper Right Triangle

    14: u'┏',  # Box Drawings Heavy Down And Right
   
    15: u'┓',  # Box Drawings Heavy Down And Left

    16: u'┛',  # Box Drawings Heavy Up And Left

    17: u'┗',  # Box Drawings Heavy Up And Right

    18: u'━',  # Box Drawings Heavy Horizontal

    19: u'┃',  # Box Drawings Heavy Vertical

    20: u'┳',  # Box Drawings Heavy Down And Horizontal

    21: u'┫',  # Box Drawings Heavy Vertical And Left

    22: u'┻',  # Box Drawings Heavy Up And Horizontal

    23: u'┣',  # Box Drawings Heavy Vertical And Right

    24: u'╋',  # Box Drawings Heavy Vertical And Horizontal

    25: u'╭',  # Box Drawings Light Arc Down And Right

    26: u'╮',  # Box Drawings Light Arc Down And Left

    27: u'╯',  # Box Drawings Light Arc Up And Left

    28: u'╰',  # Box Drawings Light Arc Up And Right

    29: u'╱',  # Box Drawings Light Diagonal Upper Right To Lower Left

    30: u'╲',  # Box Drawings Light Diagonal Upper Left To Lower Right

    31: u'╳',  # Box Drawings Light Diagonal Cross

    32:   u' ',   # Space
    33:   u'!',   # Exclamation mark
    34:   u'"',   # Double quotes (or speech marks)
    35:   u'#',   # Number
    36:   u'$',   # Dollar
    37:   u'%',   # Procenttecken
    38:   u'&',   # Ampersand
    39:   u"'",   # Single quote
    40:   u'(',   # Open parenthesis (or open bracket)
    41:   u')',   # Close parenthesis (or close bracket)
    42:   u'*',   # Asterisk
    43:   u'+',   # Plus
    44:   u',',   # Comma
    45:   u'-',   # Hyphen
    46:   u'.',   # Period, dot or full stop
    47:   u'/',   # Slash or divide
    48:   u'0',   # Zero
    49:   u'1',   # One
    50:   u'2',   # Two
    51:   u'3',   # Three
    52:   u'4',   # Four
    53:   u'5',   # Five
    54:   u'6',   # Six
    55:   u'7',   # Seven
    56:   u'8',   # Eight
    57:   u'9',   # Nine
    58:   u':',   # Colon
    59:   u';',   # Semicolon
    60:   u'<',   # Less than (or open angled bracket)
    61:   u'=',   # Equals
    62:   u'>',   # Greater than (or close angled bracket)
    63:   u'?',   # Question mark
    64:   u'@',   # At symbol
    65:   u'A',   # Uppercase A
    66:   u'B',   # Uppercase B
    67:   u'C',   # Uppercase C
    68:   u'D',   # Uppercase D
    69:   u'E',   # Uppercase E
    70:   u'F',   # Uppercase F
    71:   u'G',   # Uppercase G
    72:   u'H',   # Uppercase H
    73:   u'I',   # Uppercase I
    74:   u'J',   # Uppercase J
    75:   u'K',   # Uppercase K
    76:   u'L',   # Uppercase L
    77:   u'M',   # Uppercase M
    78:   u'N',   # Uppercase N
    79:   u'O',   # Uppercase O
    80:   u'P',   # Uppercase P
    81:   u'Q',   # Uppercase Q
    82:   u'R',   # Uppercase R
    83:   u'S',   # Uppercase S
    84:   u'T',   # Uppercase T
    85:   u'U',   # Uppercase U
    86:   u'V',   # Uppercase V
    87:   u'W',   # Uppercase W
    88:   u'X',   # Uppercase X
    89:   u'Y',   # Uppercase Y
    90:   u'Z',   # Uppercase Z
    91:   u'[',   # Opening bracket
    92:   u'\\',  # Backslash
    93:   u']',   # Closing bracket
    94:   u'^',   # Caret - circumflex
    95:   u'_',   # Underscore
    96:   u'`',   # Grave accent
    97:   u'a',   # Lowercase a
    98:   u'b',   # Lowercase b
    99:   u'c',   # Lowercase c
    100:  u'd',   # Lowercase d
    101:  u'e',   # Lowercase e
    102:  u'f',   # Lowercase f
    103:  u'g',   # Lowercase g
    104:  u'h',   # Lowercase h
    105:  u'i',   # Lowercase i
    106:  u'j',   # Lowercase j
    107:  u'k',   # Lowercase k
    108:  u'l',   # Lowercase l
    109:  u'm',   # Lowercase m
    110:  u'n',   # Lowercase n
    111:  u'o',   # Lowercase o
    112:  u'p',   # Lowercase p
    113:  u'q',   # Lowercase q
    114:  u'r',   # Lowercase r
    115:  u's',   # Lowercase s
    116:  u't',   # Lowercase t
    117:  u'u',   # Lowercase u
    118:  u'v',   # Lowercase v
    119:  u'w',   # Lowercase w
    120:  u'x',   # Lowercase x
    121:  u'y',   # Lowercase y
    122:  u'z',   # Lowercase z
    123:  u'{',   # Opening brace
    124:  u'|',   # Vertical bar
    125:  u'}',   # Closing brace
    126:  u'~',   # Equivalency sign - tilde
    127:  u' ',   # Delete

    128:  u'←',  # Leftwards Arrow
    129:  u'↑',  # Upwards Arrow
    130:  u'→',  # Rightwards Arrow
    131:  u'↓',  # Downwards Arrow



}



    # : u'·',  # Middle Dot



    # : u'▀',  # Upper Half Block
    # : u'▁',  # Lower One Eighth Block
    # : u'▂',  # Lower One Quarter Block
    # : u'▃',  # Lower Three Eighths Block
    # : u'▄',  # Lower Half Block
    # : u'▅',  # Lower Five Eighths Block
    # : u'▆',  # Lower Three Quarters Block
    # : u'▇',  # Lower Seven Eighths Block
    # : u'█',  # Full Block
    # : u'▊',  # Left Three Quarters Block
    # : u'▋',  # Left Five Eighths Block
    # : u'▌',  # Left Half Block
    # : u'▍',  # Left Three Eighths Block
    # : u'▎',  # Left One Quarter Block
    # : u'▐',  # Right Half Block
    # : u'▒',  # Medium Shade
    # : u'▖',  # Quadrant Lower Left
    # : u'▗',  # Quadrant Lower Right
    # : u'▘',  # Quadrant Upper Left
    # : u'▙',  # Quadrant Upper Left And Lower Left And Lower Right
    # : u'▚',  # Quadrant Upper Left And Lower Right
    # : u'▛',  # Quadrant Upper Left And Upper Right And Lower Left
    # : u'▜',  # Quadrant Upper Left And Upper Right And Lower Right
    # : u'▝',  # Quadrant Upper Right
    # : u'▞',  # Quadrant Upper Right And Lower Left
    # : u'▟',  # Quadrant Upper Right And Lower Left And Lower Right






    # 0:    u'█',   # Full Block
    # 1:    u'▌',   # Half Block
    # 2:    u'▄',   # Lower Half Block
    # 3:    u'▔',   # Upper one-eight
    # 3:    u'▔',   # Upper one-eight
    # 4:    u'▁',   # Lower one-eight
    # 3:    u'▔',   # Upper one-eight
    # 3:    u'▎',   # Left one-quarter
    # 177:  u'▒',   # Medium Shade
    # 3:    u'▊',   # Left three-quarters
    # 3:    u'▔',   # Upper one-eight
    # 3:    u'▔',   # Upper one-eight

    # 176: u'░',   # Light Shade
    # 178: u'▓',   # Dark Shade
    # 179: u'│',   # Box Drawings Light Vertical
    # 180: u'┤',   # Box Drawings Light Vertical And Left
    # 181: u'Á',   # Latin Capital Letter A With Acute
    # 182: u'Â',   # Latin Capital Letter A With Circumflex
    # 183: u'À',   # Latin Capital Letter A With Grave
    # 184: u'©',   # Copyright Sign
    # 185: u'╣',   # Box Drawings Double Vertical And Left
    # 186: u'║',   # Box Drawings Double Vertical
    # 187: u'╗',   # Box Drawings Double Down And Left
    # 188: u'╝',   # Box Drawings Double Up And Left
    # 189: u'¢',   # Cent Sign
    # 190: u'¥',   # Yen Sign
    # 191: u'┐',   # Box Drawings Light Down And Left
    # 192: u'└',   # Box Drawings Light Up And Right
    # 193: u'┴',   # Box Drawings Light Up And Horizontal
    # 194: u'┬',   # Box Drawings Light Down And Horizontal
    # 195: u'├',   # Box Drawings Light Vertical And Right
    # 196: u'─',   # Box Drawings Light Horizontal
    # 197: u'┼',   # Box Drawings Light Vertical And Horizontal
    # 198: u'ã',   # Latin Small Letter A With Tilde
    # 199: u'Ã',   # Latin Capital Letter A With Tilde
    # 200: u'╚',   # Box Drawings Double Up And Right
    # 201: u'╔',   # Box Drawings Double Down And Right
    # 202: u'╩',   # Box Drawings Double Up And Horizontal
    # 203: u'╦',   # Box Drawings Double Down And Horizontal
    # 204: u'╠',   # Box Drawings Double Vertical And Right
    # 205: u'═',   # Box Drawings Double Horizontal
    # 206: u'╬',   # Box Drawings Double Vertical And Horizontal
    # 207: u'¤',   # Currency Sign
    # 208: u'ð',   # Latin Small Letter Eth
    # 209: u'Ð',   # Latin Capital Letter Eth
    # 210: u'Ê',   # Latin Capital Letter E With Circumflex
    # 211: u'Ë',   # Latin Capital Letter E With Diaeresis
    # 212: u'È',   # Latin Capital Letter E With Grave
    # 213: u'ı',   # Latin Small Letter Dotless I
    # 214: u'Í',   # Latin Capital Letter I With Acute
    # 215: u'Î',   # Latin Capital Letter I With Circumflex
    # 216: u'Ï',   # Latin Capital Letter I With Diaeresis
    # 217: u'┘',   # Box Drawings Light Up And Left
    # 218: u'┌',   # Box Drawings Light Down And Right
    # 219: u'█',   # Full Block
    # 221: u'¦',   # Broken Bar
    # 222: u'Ì',   # Latin Capital Letter I With Grave
    # 223: u'▀',   # Upper Half Block
    # 224: u'Ó',   # Latin Capital Letter O With Acute
    # 225: u'ß',   # Latin Small Letter Sharp S
    # 226: u'Ô',   # Latin Capital Letter O With Circumflex
    # 227: u'Ò',   # Latin Capital Letter O With Grave
    # 228: u'õ',   # Latin Small Letter O With Tilde
    # 229: u'Õ',   # Latin Capital Letter O With Tilde
    # 230: u'µ',   # Micro Sign
    # 231: u'þ',   # Latin Small Letter Thorn
    # 232: u'Þ',   # Latin Capital Letter Thorn
    # 233: u'Ú',   # Latin Capital Letter U With Acute
    # 234: u'Û',   # Latin Capital Letter U With Circumflex
    # 235: u'Ù',   # Latin Capital Letter U With Grave
    # 236: u'ý',   # Latin Small Letter Y With Acute
    # 237: u'Ý',   # Latin Capital Letter Y With Acute
    # 238: u'¯',   # Macron
    # 239: u'´',   # Acute Accent
    # 240: u' ',   # Soft Hyphen
    # 241: u'±',   # Plus-minus Sign
    # 242: u'‗',   # Double Low Line
    # 243: u'¾',   # Vulgar Fraction Three Quarters
    # 244: u'¶',   # Pilcrow Sign
    # 245: u'§',   # Section Sign
    # 246: u'÷',   # Division Sign
    # 247: u'¸',   # Cedilla
    # 248: u'°',   # Degree Sign
    # 249: u'¨',   # Diaeresis
    # 250: u'·',   # Middle Dot
    # 251: u'¹',   # Superscript One
    # 252: u'³',   # Superscript Three
    # 253: u'²',   # Superscript Two
    # 254: u'■',   # Black Square
    # 255: u' ',   # No-break Space




    # : u' ',  # Space
    # : u'!',  # Exclamation Mark
    # : u'"',  # Quotation Mark
    # : u'#',  # Number Sign
    # : u'$',  # Dollar Sign
    # : u'%',  # Percent Sign
    # : u'&',  # Ampersand
    # : u''',  # Apostrophe
    # : u'(',  # Left Parenthesis
    # : u')',  # Right Parenthesis
    # : u'*',  # Asterisk
    # : u'+',  # Plus Sign
    # : u',',  # Comma
    # : u'-',  # Hyphen-minus
    # : u'.',  # Full Stop
    # : u'/',  # Solidus
    # : u'0',  # Digit Zero
    # : u'1',  # Digit One
    # : u'2',  # Digit Two
    # : u'3',  # Digit Three
    # : u'4',  # Digit Four
    # : u'5',  # Digit Five
    # : u'6',  # Digit Six
    # : u'7',  # Digit Seven
    # : u'8',  # Digit Eight
    # : u'9',  # Digit Nine
    # : u':',  # Colon
    # : u';',  # Semicolon
    # : u'<',  # Less-than Sign
    # : u'=',  # Equals Sign
    # : u'>',  # Greater-than Sign
    # : u'?',  # Question Mark
    # : u'@',  # Commercial At
    # : u'A',  # Latin Capital Letter A
    # : u'B',  # Latin Capital Letter B
    # : u'C',  # Latin Capital Letter C
    # : u'D',  # Latin Capital Letter D
    # : u'E',  # Latin Capital Letter E
    # : u'F',  # Latin Capital Letter F
    # : u'G',  # Latin Capital Letter G
    # : u'H',  # Latin Capital Letter H
    # : u'I',  # Latin Capital Letter I
    # : u'J',  # Latin Capital Letter J
    # : u'K',  # Latin Capital Letter K
    # : u'L',  # Latin Capital Letter L
    # : u'M',  # Latin Capital Letter M
    # : u'N',  # Latin Capital Letter N
    # : u'O',  # Latin Capital Letter O
    # : u'P',  # Latin Capital Letter P
    # : u'Q',  # Latin Capital Letter Q
    # : u'R',  # Latin Capital Letter R
    # : u'S',  # Latin Capital Letter S
    # : u'T',  # Latin Capital Letter T
    # : u'U',  # Latin Capital Letter U
    # : u'V',  # Latin Capital Letter V
    # : u'W',  # Latin Capital Letter W
    # : u'X',  # Latin Capital Letter X
    # : u'Y',  # Latin Capital Letter Y
    # : u'Z',  # Latin Capital Letter Z
    # : u'[',  # Left Square Bracket
    # : u'\',  # Reverse Solidus
    # : u']',  # Right Square Bracket
    # : u'^',  # Circumflex Accent
    # : u'_',  # Low Line
    # : u'`',  # Grave Accent
    # : u'a',  # Latin Small Letter A
    # : u'b',  # Latin Small Letter B
    # : u'c',  # Latin Small Letter C
    # : u'd',  # Latin Small Letter D
    # : u'e',  # Latin Small Letter E
    # : u'f',  # Latin Small Letter F
    # : u'g',  # Latin Small Letter G
    # : u'h',  # Latin Small Letter H
    # : u'i',  # Latin Small Letter I
    # : u'j',  # Latin Small Letter J
    # : u'k',  # Latin Small Letter K
    # : u'l',  # Latin Small Letter L
    # : u'm',  # Latin Small Letter M
    # : u'n',  # Latin Small Letter N
    # : u'o',  # Latin Small Letter O
    # : u'p',  # Latin Small Letter P
    # : u'q',  # Latin Small Letter Q
    # : u'r',  # Latin Small Letter R
    # : u's',  # Latin Small Letter S
    # : u't',  # Latin Small Letter T
    # : u'u',  # Latin Small Letter U
    # : u'v',  # Latin Small Letter V
    # : u'w',  # Latin Small Letter W
    # : u'x',  # Latin Small Letter X
    # : u'y',  # Latin Small Letter Y
    # : u'z',  # Latin Small Letter Z
    # : u'{',  # Left Curly Bracket
    # : u'|',  # Vertical Line
    # : u'}',  # Right Curly Bracket
    # : u'~',  # Tilde
    # : u' ',  # No-break Space
    # : u' ',  # Em Space
    # : u' ',  # Three-per-em Space
    # : u' ',  # Four-per-em Space
    # : u' ',  # Six-per-em Space
    # : u' ',  # Figure Space
    # : u' ',  # Punctuation Space
    # : u' ',  # Thin Space
    # : u' ',  # Hair Space
    # : u'�',  # Em Dash
    # : u'’',  # Right Single Quotation Mark
    # : u'“',  # Left Double Quotation Mark
    # : u'”',  # Right Double Quotation Mark

    # 3: u'─',  # Box Drawings Light Horizontal
    # 5: u'│',  # Box Drawings Light Vertical
    # 7: u'┌',  # Box Drawings Light Down And Right
    # 9: u'┐',  # Box Drawings Light Down And Left
    # 11:u'└',  # Box Drawings Light Up And Right
    # 13: u'┘',  # Box Drawings Light Up And Left
    # 15: u'├',  # Box Drawings Light Vertical And Right
    # 17: u'┤',  # Box Drawings Light Vertical And Left
    # 19: u'┬',  # Box Drawings Light Down And Horizontal
    # 21: u'┴',  # Box Drawings Light Up And Horizontal
    # 23: u'┼',  # Box Drawings Light Vertical And Horizontal
