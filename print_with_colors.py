from compy.run import run

def main(scrn):
    scrn.printf('Hello world !!!')
    scrn.printf('Hello in green !!!', color = 3)
    scrn.printf('Hello world !!!', color = 4)

run(main)


