
import compy


def main(sc):

    sc.clear_screen()

    index = 0
    while True:
        sc.printf('         ', reverse = True)
        index = index + 1
        if index == 10:
            break


compy.run(main)


