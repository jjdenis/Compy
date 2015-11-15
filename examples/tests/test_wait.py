import compy

def main(sc):

    sc.printf('Press escape twice while I wait')
    sc.wait_key()

    sc.printf('Or press escape twice while I wait')
    sc.input()
    sc.printf('Should not leave a running process')


compy.run(main)


