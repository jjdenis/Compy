
def my_program():

    clear_screen()

    printf()

    printf('This program shows how "def" works')

    first, second = ask_for_two_numbers()

    sum_of_numbers = sum_two_numbers(first, second)

    print_response(first, second, sum_of_numbers)

    printf('Bye!!', color='light-red')


# This function doesn't receive values, but returns two values
def ask_for_two_numbers():
    n1 = input('Give me a number ', color='light-green')
    n2 = input('Give me another number ', color='light-green')
    return n1, n2


# This function receives two values and returns one
def sum_two_numbers(n1, n2):
    sum = n1 + n2
    return sum


# This function receives three values, but doesn't return any
def print_response(n1, n2, sum):
    response = 'The sum of {} and {} is {}'.format(n1, n2, sum)
    printf(response)


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

