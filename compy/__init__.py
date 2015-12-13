__author__ = 'jjdenis'

from run import run

txt="""
# I need the next lines to run compy, don't mind them,
#  but keep them, don't get rid of them
def get_all_commands(screen):
    global printf, clear_screen
    printf = screen.printf
    clear_screen = screen.clear_screen
    main()

compy.run(get_all_commands)
"""