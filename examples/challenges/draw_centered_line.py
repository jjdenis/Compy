
import compy


def main(sc):

    sc.clear_screen()
    sc.printf()
    sc.printf('DRAW A CENTERED LINE', color=4)

    sc.printf()
    sc.printf()
    sc.printf()
    sc.printf()
    sc.printf()

    # To draw a centered line, we will first draw an invisible row of spaces
    # and stay in the same line
    line = ' ' * 10
    sc.printf(line, stay=True)
    sc.printf(line, reverse = True, color = 'light-yellow')

compy.run(main)


