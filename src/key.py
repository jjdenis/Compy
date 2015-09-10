import sys
from time import time, sleep
SENSIBILIDAD_TECLADO = 0.05
SENSIBILIDAD_INICIO = 0.1

__author__ = 'jjdenis'


class PressedKey(object):
    """ This object ensures that even a tiny press is sent """
    def __init__(self, receive):
        self.receive_from_view = receive
        self.curr_key = None
        self.last_time_read = 0
        self.key_this_pass = None
        self.key_queue = []
        self.sensibilidad = SENSIBILIDAD_TECLADO

    def wait_for_key(self):
        self._read_from_view()
        while not self.key_this_pass:
            self._read_from_view()
        return self.key_this_pass

    def check_for_key(self):
        self._read_from_view()
        if self.key_queue:
            return self.key_queue.pop(0)
        return self.curr_key


    def _read_from_view(self):

        while time() - self.last_time_read <= self.sensibilidad:
            pass

        if self.sensibilidad == SENSIBILIDAD_INICIO:
            self.sensibilidad = SENSIBILIDAD_TECLADO

        self.key_this_pass = None

        while True:
            msg = self.receive_from_view()
            if not msg:
                break
            comando, tecla, tiempo = msg
            print comando, tecla, tiempo
            if comando == 'key_pressed':
                if not self.curr_key:
                    self.sensibilidad = SENSIBILIDAD_INICIO

                if tecla != self.curr_key:
                    self.key_queue.append(tecla)
                self.curr_key = tecla
                self.key_this_pass = tecla
            elif comando == 'key_released':
                self.curr_key = None
            elif comando == 'closing':
                sleep(1)
                sys.exit()
            else:
                pass
        self.last_time_read = time()