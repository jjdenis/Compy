
__author__ = 'jjdenis'

Q = 81
ARRIBA = 315

class MapaDeCaracteres(object):
    def __init__(self, screen):
        global scr
        scr=screen
        self.resetea_pantalla()
        init_cod=0
        while True:
            self.pinta_100(init_cod)
            tecla = scr.wait_key()
            if tecla == Q:
                break
            if tecla == ARRIBA and init_cod > 0:
                init_cod=init_cod-100
            elif tecla == ARRIBA and init_cod == 0:
                pass
            elif init_cod == 200:
                pass
            else:
                init_cod = init_cod + 100

            # if final_de_linea:
            #     self.pinta_separador_filas()


    def pinta_100(self, init_code):
        self.resetea_pantalla()
        for fila in range(0,10):
            char_cod = 10 * fila + init_code
            self.pinta_separador_filas()
            self.nombre_fila(char_cod)
            for columna in range(0,10):
                char_cod = 10 * fila + columna + init_code
                self.pinta_caracter(char_cod)
        self.pinta_separador_filas()


    def resetea_pantalla(self):
        scr.clear_screen()
        scr.printf('\n')

    def pinta_separador_filas(self):
        scr.printf()
        scr.printf('       ', next_line=False)
        for k in range(5, 26):
            scr.printf(31, color=8, next_line=False, iscode=True)

    def nombre_fila(self, char_cod):
        scr.printf('{:>03}-{:>03}'.format(char_cod, char_cod + 9))
        scr.printf(31, color=8, next_line=False, iscode=True)

    def pinta_caracter(self, char_cod):
        scr.printf(char_cod, color=4, next_line=False, iscode=True)
        scr.printf(31, color=8, next_line=False, iscode=True)