
import compy


def main(sc):

    sc.clear_screen()
    sc.printf()
    sc.printf('DRAW A LINE', color=4)
    sc.printf()
    sc.printf()
    sc.printf()

    # To draw a line, we can draw 10 reversed spaces
    sc.printf(' '*10, reverse = True, color = 'light-yellow')


compy.run(main)


