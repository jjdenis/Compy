
import compy


def main(sc):

    sc.clear_screen()
    sc.printf()
    sc.printf('DRAW A SQUARE CENTERED', color=4)
    sc.printf()
    sc.printf()
    sc.printf()
    sc.printf()
    sc.printf()

    num_rows = 0
    while True:
        sc.printf(' '*15, stay=True)
        sc.printf(' '*10, reverse = True, color = 'light-yellow')
        num_rows = num_rows + 1
        if num_rows == 10:
            break


compy.run(main)


