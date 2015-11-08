
import compy


def main(sc):

    sc.clear_screen()

    sc.printf()
    sc.printf('SUM TWO VALUES', color=4)
    sc.printf('==============')
    sc.printf()

    first_value = sc.input("Give me one value: ", color=8)

    second_value = sc.input("Give me another value: ")

    sum_of_values = first_value + second_value

    response = 'The sum of {} and {} is {}'.format(first_value, second_value, sum_of_values)

    sc.printf()
    sc.printf(response, color=6)


compy.run(main)


