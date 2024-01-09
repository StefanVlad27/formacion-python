# abrir y manipular ficheros y archivos
# vamos a aprender a
#   abrir -> open()
#   leer -> read()
#   escribir -> write()
#   cerrar -> close()
#   ficheros txt


# abrir ficheros
mi_archivo = open('tema6\\prueba.txt')

print(mi_archivo) # asi no se muestra el contenido
print(mi_archivo.read()) # asi se muestra el contenido

una_linea = mi_archivo.readline()
print(una_linea) # mostrara la primera linea

una_linea = mi_archivo.readline()
print(una_linea) # mostrara la segunda ya que ha dejado un marcador donde finalizo la ultima vez y sigue a partir de ahi

una_linea = mi_archivo.readline()
print(una_linea) # mostrara la tercera ya que ha dejado un marcador en la segunda, donde finalizo la ultima vez, y sigue a partir de ahi

mi_archivo.close() # cerrar el archivo


mi_archivo = open('tema6\\prueba.txt')
todas = mi_archivo.readlines() #lee todas las lineas del fichero
todas = todas.pop()
print(todas)


# Abre el archivo texto.txt e imprime su contenido.
# Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu codigo
mi_archivo = open('texto.txt')
print(mi_archivo.read()) # asi se muestra el contenido

# Imprime la primera linea del archivo texto.txt
# No olvides abrir el archivo y cerrarlo luego de ejecutar tu codigo.
# Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu codigo
mi_archivo = open('texto.txt')

una_linea = mi_archivo.readline()
print(una_linea)
mi_archivo.close()


# Abre el archivo texto.txt e imprime unicamente la segunda linea.
mi_archivo = open('texto.txt')
una_linea = mi_archivo.readline()
una_linea = mi_archivo.readline()
print(una_linea)



# abrir ficheros y escribe una linea
archivo = open('tema6\\prueba.txt', 'r')
archivo.write('Nueva linea') # al ejecutarlo nos daria error ya que hemos abierto el fichero en modo "r", es decir, "read".

archivo = open('tema6\\prueba1.txt', 'w')
archivo.write('Nuevo fichero') # al ejecutarlo, si el fichero no existe lo crea. Si si existe, lo sobreescribe.

archivo = open('tema6\\prueba.txt', 'a')
archivo.write('Nueva linea') # escribe a partir de lo ultimo que hay en el fichero

archivo = open('tema6\\prueba.txt', 'r')
archivo.write('Nueva linea') # AL EJECUTARLO NOS DARIA ERROR YA QUE HEMOS ABIERTO EL FICHERO EN MODO "R", ES DECIR, "READ".

archivo.close()


# abrir ficheros y escribir varias palabras, lineas
archivo = open('tema6\\prueba.txt', 'w')
archivo.writelines(['Nueva ', 'linea ', 'python'])
archivo.close()


# añadir palabras de una lista a un fichero mediante saltos de linea entre cada palabra
archivo = open('tema6\\prueba.txt', 'w')
lista = ['Nueva ', 'linea ', 'python']

for palabra in lista:
    archivo.writelines(palabra + '\n')

archivo.close()



# EJERCICIOS

# Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".
# Imprime el contenido completo de "mi_archivo.txt" al finalizar.
# Pista: deberas cerrarlo en modo escritura y volverlo a abrir en modo lectura.

archivo = open('mi_archivo.txt', 'w')
archivo.write( "Nuevo texto")

archivo = open('mi_archivo.txt', 'r')
print(archivo.read())

archivo.close()


# Abre el archivo llamado "mi_archivo.txt", y añade una linea al final del mismo que diga: "Nuevo inicio de sesion".
# Imprime el contenido completo de "mi_archivo.txt" al finalizar.
# Pista: deberas cerrarlo en modo escritura y volverlo a abrir en modo lectura.

nuevo = "Nuevo inicio de sesion"

archivo = open('mi_archivo.txt', 'a')
archivo.write(nuevo)

archivo = open('mi_archivo.txt', 'r')
print(archivo.read())

archivo.close()


# Utiliza el metodo writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" .
# Inserta un tabulador entre cada elemento de la lista para separarlos.
# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
# Imprime el contenido completo de "registro.txt" al finalizar.
# Pista: recuerda que el simbolo para concatenar un tabulador en un string es \t. Tambien, deberas cerrar el archivo en
# modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.

archivo = open('registro.txt', 'a')
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

for palabra in registro_ultima_sesion:
    archivo.writelines(palabra + '\t')

archivo = open('registro.txt', 'r')

print(print(archivo.read()))

archivo.close()


# ficheros con ruta absoluta

# directorio actual
import os

ruta = os.getcwd()

print(ruta)


# directorio personalizado
import os

ruta = os.chdir('C:\\Users\\stefanvlad\\source\\repos\\formacion-python\\tema6')
archivo = open("prueba.txt")

print(archivo.read())


# crear directorios
import os

ruta = os.makedirs('C:\\Users\\stefanvlad\\source\\repos\\formacion-python\\tema6\\carpeta-prueba')


# conocer la ruta del fichero
import os

ruta = os.makedirs('C:\\Users\\stefanvlad\\source\\repos\\formacion-python\\tema6\\prueba3.txt')

elemento = os.path.dirname(ruta)

elemento = os.path.split(ruta) # te mostrara el nombre de la ruta y despues el nombre del fichero


# eliminar directorios

import os

os.rmdir('C:\\Users\\stefanvlad\\source\\repos\\formacion-python\\tema6\\carpeta-prueba')

# leer ficheros en ruta absoluta

import os

otro_archivo = open('C:\\Users\\stefanvlad\\source\\repos\\formacion-python\\tema6\\prueba1.txt')
print(otro_archivo.read())


# modulo path - sirve para cualquier SO
from pathlib import Path

carpeta = Path("C:/Users/stefanvlad/source/repos/formacion-python/tema6") / "prueba1.txt"

mi_archivo = open(carpeta)
print(mi_archivo.read())




# modulo pathlib

# leer un fichero
from pathlib import Path

carpeta = Path("C:/Users/stefanvlad/source/repos/formacion-python/tema6/prueba1.txt")
print(carpeta.read_text())

# ver nombre fichero
from pathlib import Path

carpeta = Path("C:/Users/stefanvlad/source/repos/formacion-python/tema6/prueba1.txt")
print(carpeta.name)

# ver extension del fichero
from pathlib import Path

carpeta = Path("C:/Users/stefanvlad/source/repos/formacion-python/tema6/prueba1.txt")
print(carpeta.suffix)

# ver nombre fichero sin la extension
from pathlib import Path

carpeta = Path("C:/Users/stefanvlad/source/repos/formacion-python/tema6/prueba1.txt")
print(carpeta.stem)


# ver nombre fichero sin la extension
from pathlib import Path

carpeta = Path("C:/Users/stefanvlad/source/repos/formacion-python/tema6/prueba1.txt")


# comprobar si existe un fichero

from pathlib import Path

carpeta = Path("C:/Users/stefanvlad/source/repos/formacion-python/tema6/prueba1.txt")

if not carpeta.exists():
    print("Este fichero no existe")
else:
    print("Este fichero existe")


# para transformar a una ruta de windows

from pathlib import Path, PureWindowsPath
carpeta = Path("C:/Users/stefanvlad/source/repos/formacion-python/tema6/prueba1.txt")
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)


# crear rutas a partir de palabras
from pathlib import Path

base = Path.home() # devuelve la ruta absoluta del directorio principal del usuario actual
guia = Path("Barcelona", "Sagrada_familia")

print(base) # C:\Users\stefanvlad
print(guia) # Barcelona\Sagrada familia

guia = Path(base, "Barcelona", "Sagrada_familia.txt")
guia2 = guia.with_name("La_predera.txt") # cambia el fichero
print(guia) # C:\Users\stefanvlad\Barcelona\Sagrada_familia.txt
print(guia2) # C:\Users\stefanvlad\Barcelona\La_predera.txt

print(guia.parent) # C:\Users\stefanvlad\Barcelona . devuelve el directorio padre del fichero.
print(guia.parent.parent) # C:\Users\stefanvlad



# EJERCICIOS
# Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.
# Recuerda importar Path del modulo pathlib, y utilizar el metodo home()
from pathlib import Path

ruta_base = Path.home()

# Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
# Almacena el directorio obtenido en la variable ruta. No olvides importar Path.
from pathlib import Path

guia = Path("Curso Python","Dia 6","practicas_path.py")
ruta = guia.relative_to(Path())

print(ruta)

# Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
# Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario.
from pathlib import Path

ruta = Path (Path.home(),"Curso Python","Dia 6","practicas_path.py")


# limpiar la consola
from os import system

nombre = input('Dime tu nombre: ')
edad = input('Dime tu edad: ')

system('cls') # system sirve para ejecutar comandos cual cmd se tratase

print(f"Tu nombre es {nombre} y tienes {edad} años.")


# archivos y funciones
# EJERCICIOS
# Crea una funcion llamada abrir_leer() que abra (open) un archivo indicado como parametro, y devuelva su contenido (read).
from pathlib import Path

def abrir_leer(fichero):
    read = open.read_text()
    return read


open = Path('ejemplo.txt')
abrir_leer(open)


# Crea una funcion llamada sobrescribir() que abra (open) un archivo indicado como parametro, y sobrescriba cualquier
# contenido anterior por el texto "contenido eliminado"
def sobrescribir(fichero):
    archivo = open(fichero, 'w')
    archivo.write("contenido eliminado")

sobrescribir('prueba.txt')

# Crea una funcion llamada registro_error() que abra (open) un archivo indicado como parametro, y lo actualice añadiendo una
# linea al final que indique "se ha registrado un error de ejecucion". Finalmente, debe cerrar el archivo abierto.

def registro_error(fichero):
    archivo = open(fichero, 'a')
    archivo.write("se ha registrado un error de ejecucion")
    archivo.close()

registro_error('prueba.txt')