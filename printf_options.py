import compy


def main(sc):

    sc.printf('Hello')

    sc.printf('Hello', color='black')

    sc.printf('Hello', color=4)

    sc.printf('Hello, ', next_line=False)

    sc.printf('partner!', color=0)

    sc.printf()

    sc.printf('Hello', reverse = True)

    sc.printf('Hello, or better...', color='light-green', reverse=True, next_line=False)

    sc.printf('Good bye!!!')

compy.run(main)


