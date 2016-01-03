
def my_program():

    printf('Example of printf using a color number',color=17)

    printf('And now using a color name', color='light-yellow')

    printf()

    printf('To leave a blank line, do not include anything inside the parenthesis', color='light-green')

    printf()

    printf('If no color is specified, printf will select color used last')

    printf()

    printf('After a printf ends, the next printf will continue in the next line',color='light-blue')

    printf('Except when you specify otherwise...', stay=True)

    printf('This time it stayed in the same line!!!',color='white')

    printf()

    printf('You can also print in reverse!!!', reverse=True, color='pink')

    printf('Reversed spaces make fine lines!!!')

    printf()

    printf('       ', reverse=True)


###########################################################################
###########################################################################
# The next lines are needed to run compy, don't mind them,
# but keep them, don't get rid of these lines
###########################################################################
###########################################################################

def clear_screen(): pass

def set_bg_color(color): pass

def set_fm_color(color): pass

def printf(to_print='', color=None, stay=False, reverse=False): pass

def xyprintf(x, y, *args): pass

def poke(x, y, code, color = None, reverse=False): pass

def peek(self, x, y): pass

def input(message = '', color=None): pass

def wait_key(): pass

def check_key(): pass

def redefine_commands(screen):

    global clear_screen, set_bg_color, set_fm_color, printf, xyprintf
    global poke, peek, input, wait_key, check_key

    clear_screen = screen.clear_screen
    set_bg_color = screen.set_bg_color
    set_fm_color = screen.set_fm_color
    printf = screen.printf
    xyprintf = screen.xyprintf
    poke = screen.poke
    peek = screen.peek
    input = screen.input
    wait_key = screen.wait_key
    check_key = screen.check_key

    my_program()

import compy

compy.run(redefine_commands)

###########################################################################
###########################################################################


