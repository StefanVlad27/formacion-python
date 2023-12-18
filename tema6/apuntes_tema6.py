# abrir y manipular ficheros y archivos
# vamos a aprender a
#   abrir -> open()
#   leer -> read()
#   escribir -> write()
#   cerrar -> close()
#   ficheros txt


# abrir ficheros
mi_archivo = open('tema6\\prueba.txt')

print(mi_archivo) # así no se muestra el contenido
print(mi_archivo.read()) # así se muestra el contenido

una_linea = mi_archivo.readline()
print(una_linea) # mostrará la primera linea

una_linea = mi_archivo.readline()
print(una_linea) # mostrará la segunda ya que ha dejado un marcador donde finalizó la última vez y sigue a partir de ahí

una_linea = mi_archivo.readline()
print(una_linea) # mostrará la tercera ya que ha dejado un marcador en la segunda, donde finalizó la última vez, y sigue a partir de ahí

mi_archivo.close() # cerrar el archivo


mi_archivo = open('tema6\\prueba.txt')
todas = mi_archivo.readlines() #lee todas las lineas del fichero
todas = todas.pop()
print(todas)


# Abre el archivo texto.txt e imprime su contenido.
# Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
mi_archivo = open('texto.txt')
print(mi_archivo.read()) # así se muestra el contenido

# Imprime la primera línea del archivo texto.txt
# No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.
# Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
mi_archivo = open('texto.txt')

una_linea = mi_archivo.readline()
print(una_linea)
mi_archivo.close()


# Abre el archivo texto.txt e imprime únicamente la segunda línea.
mi_archivo = open('texto.txt')
una_linea = mi_archivo.readline()
una_linea = mi_archivo.readline()
print(una_linea)



# abrir ficheros y escribe una linea
archivo = open('tema6\\prueba.txt', 'r')
archivo.write('Nueva linea') # al ejecutarlo nos daría error ya que hemos abierto el fichero en modo "r", es decir, "read".

archivo = open('tema6\\prueba1.txt', 'w')
archivo.write('Nuevo fichero') # al ejecutarlo, si el fichero no existe lo crea. Si sí existe, lo sobreescribe.

archivo = open('tema6\\prueba.txt', 'a')
archivo.write('Nueva linea') # escribe a partir de lo ultimo que hay en el fichero

archivo = open('tema6\\prueba.txt', 'r')
archivo.write('Nueva linea') # AL EJECUTARLO NOS DARÍA ERROR YA QUE HEMOS ABIERTO EL FICHERO EN MODO "R", ES DECIR, "READ".

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
# Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.

archivo = open('mi_archivo.txt', 'w')
archivo.write( "Nuevo texto")

archivo = open('mi_archivo.txt', 'r')
print(archivo.read())

archivo.close()


# Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
# Imprime el contenido completo de "mi_archivo.txt" al finalizar.
# Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.

nuevo = "Nuevo inicio de sesión"

archivo = open('mi_archivo.txt', 'a')
archivo.write(nuevo)

archivo = open('mi_archivo.txt', 'r')
print(archivo.read())

archivo.close()


# Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" .
# Inserta un tabulador entre cada elemento de la lista para separarlos.
# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
# Imprime el contenido completo de "registro.txt" al finalizar.
# Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en
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