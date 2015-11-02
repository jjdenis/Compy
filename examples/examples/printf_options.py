import compy


def main(sc):

    sc.printf('Hello')

    sc.printf('Hello', color='black')

    sc.printf('Hello', color=4)

    sc.printf('Hello, ', stay=True)

    sc.printf('partner!', color=0)

    sc.printf()

    sc.printf('Hello', reverse=True)

    sc.printf('Hello, or better...', color='light-green', stay=True, reverse=True)

    sc.printf('Good bye!!!')

compy.run(main)


