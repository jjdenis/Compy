
def my_program():
    clear_screen()
    msg = 'Here we show how to print text and numbers.'
    printf(msg)

    printf()

    printf('You first create a string that contains the numbers')
    printf('To do that, you need to use braces, a point, and the word "format" ')
    printf('Lets print a number inside a text string:')
    msg = 'I am {} years old'.format(46)
    printf(msg, color='yellow')

    printf()

    printf('You can also use variables and print text inside text:', color='light-blue')
    age = 46
    name = 'Juanjo'
    msg = 'Hello, mi name is {}, I am {} years old'.format(name, age)
    printf(msg, color = 'yellow')

    printf()

    printf('You can also format the number, the options are many, this one is useful:', color='light-blue')
    age_universe = 15000000000
    msg = 'No format: The universe is {} years old'.format(age_universe)
    printf(msg, color='yellow')
    msg = 'Formatted: The universe is {:g} years old'.format(age_universe)
    printf(msg)
    msg = 'Another format: The universe is {:,} years old'.format(age_universe)
    printf(msg)


###########################################################################
###########################################################################
# The next lines are needed to run compy, don't mind them,
# but keep them, don't get rid of these lines
###########################################################################
###########################################################################
import compy
import time

# define commands of compy, so IDE's will recognize them
def clear_screen(): pass
def set_bg_color(color): pass
def set_fm_color(color): pass
def printf(to_print='', color=None, stay=False, reverse=False): pass
def xyprintf(x, y, *args): pass
def poke(x, y, code, color = None, reverse=False): pass
def peek(self, x, y): pass
def input(message = '', color=None): return None
def wait_key(): pass
def check_key(): pass

def redefine_commands_and_run(screen):

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

if __name__ == '__main__':
    compy.run(redefine_commands_and_run)

###########################################################################
###########################################################################

