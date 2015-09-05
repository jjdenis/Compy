Cómo ejecutar un programa
--------------------------

Para ejecutar un programa abre el terminal
en la carpeta poke
y escribe el siguiente comando:

    pythonw ejemplo.py



Cómo crear tu propio programa
--------------------------------

Ve a finder, elije el programa "ejemplo.py", y pulsa cmd-d,
luego selecciona el archivo creado 
y pulsa Enter para cambiarle el nombre. 
(por ejemplo cambia el nombre a juego.py)

Ejecuta tu programa así:

    pythonw ejemplo.py

Para parar el programa y salir, pulsa escape.

También puedes esperar 10 segundos a que se cierre.


Primer programa
-----------------

Cambia juego.py de esta manera:

def programa_principal(pantalla):

    screen.printf("Hola")
    screen.printf("Hola")
    screen.printf("Hola")
    screen.printf("Hola")
    screen.printf("Hola")
    screen.printf("Hola")
    screen.printf("Hola")
    screen.printf("Hola")

Tenemos un problema, que hay que cerrar la pantalla a mano,
vamos a solucionarlo, añade esta linea:

    screen.cierra()
