
import compy


def main(scr):

    scr.clear_screen()

    scr.printf()
    scr.printf('    SUM OF TWO VALUES', color= 4)
    scr.printf('    =================')
    scr.printf()

    first_value = scr.input("Give me one value: ", color=8)

    second_value = scr.input("Give me another value: ")

    sum_of_values = first_value + second_value

    response = 'The sum of {} and {} is {}'.format(first_value, second_value, sum_of_values)

    scr.printf()
    scr.printf(response, color=6)


compy.run(main)


