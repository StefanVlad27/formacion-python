# modulo Collections: es un modulo que contiene estructuras de datos especializadas

# Counter: es una subclase de diccionario para contar objetos de una lista

from collections import Counter

# contar numeros de una lista
numeros = [8,6,7,2,5,2,4,1,0,7,9,8,6,5,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0]
print(Counter(numeros)) # Counter({2: 4, 1: 4, 0: 4, 8: 3, 7: 3, 6: 3, 5: 3, 4: 3, 9: 2, 3: 2})

# contar letras de una palabra
palabra = "ardido"
print(Counter(palabra)) # Counter({'d': 2, 'a': 1, 'r': 1, 'i': 1, 'o': 1})

# contar palabras de una frase
frase = "Hola mundo, hola mundo, hola mundo"
print(Counter(frase.split())) # Counter({'hola': 3, 'mundo,': 2, 'mundo': 1})



serie = Counter([1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4])
print(serie.most_common()) # most_common(): devuelve una lista de tuplas con los elementos mas comunes y su numero de apariciones

serie = Counter([1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4])
print(serie.most_common(1)) # muestra el elemento que mas se repite

# guarda en una lista los elementos de la serie
serie = Counter([1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4])
lista = list(serie)
print(lista)


# defaultdict: es una subclase de diccionario que en caso de no encontrar una clave, devuelve un valor por defecto que puedes definir
from collections import defaultdict

mi_dic= {"a": "azul", "b": "rojo", "c": "verde"}
print(mi_dic["a"]) # azul

# si intentamos acceder a una clave que no existe, nos devuelve un KeyError
print(mi_dic["d"]) # KeyError: 'd'

# con defaultdict podemos evitar el KeyError
mi_dic = defaultdict(lambda: "nada")

mi_dic["a"] = "azul"
print(mi_dic["b"]) # nada


# namedtuple: permite crear tuplas con nombres para un acceso mas legible a los elementos en lugar de usar indices numericos
from collections import namedtuple

mi_tupla = (500, 200, 100)
print(mi_tupla[0]) # 500

Persona = namedtuple("Persona", ["nombre", "apellido", "edad"])
ariel = Persona("Ariel", "Carreras", 30)
print(ariel.nombre) # Ariel
print(ariel.apellido) # Carreras
print(ariel.edad) # 30



# ejercicios:

# Aplica un Counter (contador) sobre la lista de numeros entregada a continuacion, y almacenalo en una variable llamada contador
from collections import Counter

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
contador = Counter(lista)


# Crea un diccionario llamado mi_diccionario, para el cual, cuando no se halle una palabra clave buscada, se cargue con el string "Valor no hallado".
# Carga el diccionario, al menos, con el siguiente par de datos:
#     palabra clave = edad
#     valor = 44
# Utiliza el método defaultdict del módulo Collections.
from collections import defaultdict

mi_diccionario = defaultdict(lambda: "Valor no hallado")
mi_diccionario["edad"] = 44

# Una cola doblemente terminada o deque (del inglés double ended queue) es una estructura de datos lineal que permite insertar
# y eliminar elementos por ambos extremos.
# Investiga más al respecto en cualquier sitio de documentación, y a continuación implementa una deque a partir del módulo collections.
# Los elementos iniciales de la lista se brindan a continuación.
# ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
# La lista debe tener la capacidad de incorporar elementos por la izquierda, y recibir el nombre lista_ciudades.

from collections import deque

ciudades = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
lista_ciudades = deque(ciudades)


# modulo os y shutil: nos permiten trabajar con archivos y directorios del sistema operativo
# os: nos permite trabajar con archivos y directorios
# shutil: nos permite trabajar con archivos y directorios de forma mas avanzada

import os
import shutil


print(os.getcwd()) # devuelve el directorio actual

# crear un fichero, escribir dentro del mismo y cerrarlo
archivo= open("tema9/archivo.txt", "w")
archivo.write("Hola mundo")
archivo.close()

print(os.listdir()) # devuelve una lista con los archivos y directorios del directorio actual


# mover archivos
shutil.move("tema9/archivo.txt", "tema9/archivos/archivo.txt")

# copiar archivos
shutil.copy("tema9/archivos/archivo.txt", "tema9/archivos/archivo_copia.txt")

# renombrar archivos
shutil.move("tema9/archivos/archivo_copia.txt", "tema9/archivos/archivo_renombrado.txt")

# eliminar archivos
os.unlink("tema9/archivos/archivo_renombrado.txt")

# eliminar carpetas VACIAS solamente
os.rmdir("tema9/archivos")

# eliminar directorios y archivos
shutil.rmtree("tema9/archivos")

# crear directorios
os.mkdir("tema9/archivos")

# crear directorios y subdirectorios
os.makedirs("tema9/archivos/subarchivos")

os.read()

# os.walk - explorar y mostrar la estructura de directorios de una carpeta específica en Python
for carpeta, subcarpeta, archivo in os.walk("tema9"):

    print(f"Estas en la carpeta {carpeta}")

    print(f"Las subcarpetas son:")
    for sub in subcarpeta:
        print(f"\t{sub}")

    print(f"Los archivos son:")
    for arch in archivo:
        print(f"\t{arch}")

    print("")


# para buscar elementos que cumplan con un criterio:
for carpeta, subcarpeta, archivo in os.walk("tema9"):

    print(f"Estas en la carpeta {carpeta}")

    print(f"Las subcarpetas son:")
    for sub in subcarpeta:
        print(f"\t{sub}")

    print(f"Los archivos son:")
    for arch in archivo:
        if arch.endswith(".txt"): # solo mostrara los ficheros acabados en .txt
            print(f"\t{arch}")

    print("")

# enviar archivos a la papelera de reciclaje
import send2trash

send2trash.send2trash("tema9/archivos/subarchivos")



# modulo datetime: nos permite trabajar con fechas y horas
import datetime

mi_hora = datetime.time(17, 35) # hora, minutos
print(mi_hora) # 17:35:00
print(mi_hora.hour) # 17
print(mi_hora.minute) # 35

# fecha actual
mi_fecha = datetime.date.today()
print(mi_fecha)

# defnir fecha
mi_dia  = datetime.date(2020, 12, 31) # año, mes, dia
print(mi_dia) # 2020-12-31

# podemos combinar fechas y horas
mi_fecha = datetime(2020, 12, 31, 17, 35) # año, mes, dia, hora, minutos
print(mi_fecha) # 2020-12-31 17:35:00

# podemos sumar dias a una fecha
mi_fecha = mi_fecha.replace(year=2021)


from datetime import date

# calcular la diferencia en días entre dos fechas

nacimiento = date(1989, 12, 31)
defuncion = date(2021, 12, 31)
diferencia = defuncion - nacimiento

print(diferencia) # 11622 days, 0:00:00

print(diferencia.days) # 11622


# calcular la diferencia en horas entre dos fechas
despierta = datetime(2021, 1, 1, 7, 0)
duerme = datetime(2021, 1, 1, 23, 0)

vigilia = duerme - despierta
print(vigilia) # 16:00:00



# ejercicios:
# Crea un objeto fecha llamado mi_fecha que almacene el día 3 de febrero de 1999
from datetime import date

mi_fecha = date(1999, 2, 3)


# Crea un objeto en la variable hoy que siempre almacene la fecha actual cuando sea invocada.
from datetime import date

hoy = date.today()


# En una variable llamada minutos, almacena únicamente los minutos de la hora actual.
# Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable minutos debe almacenar el valor 43
from datetime import datetime

minutos = datetime.now().minute



# modulos para medir tu tiempo de ejecucion

# modulo timeit: nos permite medir el tiempo de ejecucion de un codigo
# modulo time: nos permite medir el tiempo de ejecucion de un codigo

import time
def prueba_for(numero):
    lista = []
    for i in range(1, numero+1):
        lista.append(i)
    return lista

def prueba_while(numero):
    lista = []
    i = 0
    while i < numero:
        i += 1
        lista.append(i)
    return lista


# ejemplo con time
inicio = time.time()
prueba_for(1000000)
final = time.time()
print(final - inicio)

inicio = time.time()
prueba_while(1000000)
final = time.time()
print(final - inicio)


# ejemplo con timeit

import timeit

declaracion = """
prueba_for(100)
"""

mi_setup = """
def prueba_for(numero):
    lista = []
    for i in range(1, numero+1):
        lista.append(i)
    return lista
"""

duracion = timeit.timeit(declaracion, mi_setup, number=1000000)
print(duracion)

declaracion2 = """
prueba_while(100)
"""

mi_setup2 = """
def prueba_while(numero):
    lista = []
    i = 0
    while i < numero:
        i += 1
        lista.append(i)
    return lista
"""

duracion2 = timeit.timeit(declaracion2, mi_setup2, number=1000000)
print(duracion2)



# modulo math: nos permite trabajar con funciones matematicas

import math

resultado = math.floor(3.14) # redondea hacia abajo
print(resultado) # 3

resultado = math.ceil(3.14) # redondea hacia arriba
print(resultado) # 4

resultado = math.pi # devuelve el valor de pi
print(resultado) # 3.141592653589793

resultado = math.sqrt(25) # devuelve la raiz cuadrada
print(resultado) # 5.0

# ejercicios:
# Obtén el logaritmo base 10 del número 25, y almacena el resultado en la variable resultado.
# Puedes utilizar el método math.log10()
import math

resultado = math.log10(25)


# Obten la raíz cuadrada de pi con la constante math.pi y el método math.sqrt() . Almacena el resultado obtenido en la variable resultado.
import math

resultado = math.sqrt(math.pi)


# Encuentra el factorial de 7 y almacena el resultado en la variable resultado.
# El método a utilizar es factorial()
import math

resultado = math.factorial(7)



# modulo re: nos permite trabajar con expresiones regulares
# expresiones regulares: nos permiten buscar patrones dentro de un texto
# https://regex101.com/

# caracteres especiales:
# /d -> digito numerico -> v\d.\d\d -> v1.09
# /w -> caracter alfanumerico -> \w\w-\w -> ab-c
# /s -> espacio en blanco -> numero\s\d\d -> numero 12
# /D -> no digito numerico -> \D\D\D -> abc
# /W -> no caracter alfanumerico -> \W\W\W -> -_-
# /S -> no espacio en blanco -> \S\S\S -> abc

# caracteres cuantificadores:
# + -> 1 o mas veces -> \d+ -> 123
# {n} -> exactamente n veces -> \d{3} -> 123 -> N\d{3}-\d{5}
# {n,m} -> de n a m veces -> \d{2,4} -> 1234
# {n,} -> n o mas veces -> \d{2,} -> 1234567890
# * -> 0 o mas veces -> \d* -> 1234567890
# ? -> 0 o 1 vez -> \d? -> 1


# sin expresiones regulares:
texto = "Si necesitas ayuda llama al 555-1234-5678 las 24 horas del dia"

palabra = "ayuda" in texto:
print(palabra) # True

# con expresiones regulares:
import re

texto = "Si necesitas ayuda llama al 555-1234-5678 las 24 horas del dia en el servicio de ayuda"
patron = "ayuda"


busqueda = re.search(patron, texto)
print(busqueda) # <re.Match object; span=(13, 18), match='ayuda'>
print(busqueda.start()) # 13 -> indice del primer caracter de la coincidencia

busqueda = re.findall(patron, texto)
print(busqueda) # ['ayuda', 'ayuda'] -> devuelve una lista con todas las coincidencias
print(len(busqueda)) # 2 -> devuelve la cantidad de coincidencias

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span()) # (13, 18) (54, 59) -> indices de ambos caracteres de la coincidencia


# sin cuantificar:
texto = "llama al 555-1234-5678 ya mismo"
patron = r"\d\d\d-\d\d\d\d-\d\d\d\d" # \d -> digito numerico

resultado = re.search(patron, texto)

print(resultado) # <re.Match object; span=(8, 22), match='555-1234-5678'> -> devuelve la primera coincidencia
print(resultado.group()) # 555-1234-5678 -> devuelve la primera coincidencia


# cuantificadores:
texto = "llama al 555-1234-5678 ya mismo"
patron = r"\d{3}-\d{4}-\d{4}" # \d -> digito numerico

resultado = re.search(patron, texto)
print(resultado) # <re.Match object; span=(8, 22), match='555-1234-5678'> -> devuelve la primera coincidencia


texto = "llama al 555-1234-5678 ya mismo"
patron = re.compile(r"(\d{3})-(\d{4})-(\d{4})") # \d -> digito numerico

resultado = re.search(patron, texto)
print(resultado.group()) # 555-1234-5678 -> devuelve todo
print(resultado.group(2)) # 555 -> devuelve la primera coincidencia


# utiliza una expresión regular para verificar si cumple con un patrón específico que incluye un carácter que no sea
# un dígito al principio y 7 caracteres de palabra
import re

clave = input("Introduce tu clave: ")

patron = r"\D{1}\w{7}"

chequear = re.search(patron, clave)

print(chequear)


# utiliza una expresión regular para buscar y encontrar la primera coincidencia
import re

texto = "No atendemos los lunes a las 10:00"
buscar = re.search(r'lunes|martes', texto)

print(buscar) # <re.Match object; span=(16, 21), match='lunes'> -> devuelve la primera coincidencia

# . -> cualquier caracter antes del texto "demos". el punto indica tantos caracteres como sea
import re

texto = "No atendemos los lunes a las 10:00"
buscar = re.search(r'..demos', texto)

print(buscar.group()) # endemos -> devuelve la primera coincidencia


# ^ -> indica que el texto debe comenzar con el caracter que le sigue
import re

texto = "No atendemos los lunes a las 10:00"
buscar = re.search(r'^\D', texto) # \D -> no digito numerico

print(buscar.group()) # N -> devuelve la primera coincidencia




# ejercicios:
# Crea una función llamada verificar_email para comprobar si una dirección de email es correcta, que verifique si el email
# dado como argumento contiene "@" (entre el nombre de usuario y el dominio) y finaliza en ".com" (aunque aceptando también
# casos que cuentan con un dominio adicional, tal como ".com.br" para el caso de un usuario de Brasil).
# Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok", pero si detecta que la frase
# no contiene los elementos indicados, debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el mensaje.
import re

def verificar_email(email):
    patron = r"\w+@\w+\.\w+"
    if re.search(patron, email):
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


# Crea una función llamada verificar_saludo para verificar si una frase entregada como argumento inicia con la palabra "Hola".
# Si se encuentra el patrón, la función debe finalizar mostrando el mensaje "Ok", pero si detecta que la frase no contiene "Hola",
# debe informarle al usuario "No has saludado" imprimiendo el mensaje en pantalla.
import re

def verificar_saludo(frase):
    patron = r"^Hola"
    if re.search(patron, frase):
        print("Ok")
    else:
        print("No has saludado")


# El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos y cuatro numéricos a
# continuación (ejemplo: XX1234). Crea una función, llamada verificar_cp para comprobar si el código postal pasado como
# argumento sigue este patrón. Si el patrón es correcto, mostrar al usuario el mensaje "Ok", de lo contrario:
# "El código postal ingresado no es correcto".
import re

def verificar_cp(cp):
    patron = r"^\w{2}\d{4}"
    if re.search(patron, cp):
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")



# comprimir y descomprimir archivos con el modulo zipfile y shutil

# comprimir archivos
import zipfile

mi_zip = zipfile.ZipFile("tema9/archivo.zip", "w") # w -> write

mi_zip.write("tema9/fichero-1.txt")
mi_zip.write("tema9/fichero-2.txt")

mi_zip.close()


# descomprimir archivos
import zipfile

zip_abierto = zipfile.ZipFile("tema9/archivo.zip", "r") # r -> read

zip_abierto.extract("tema9/fichero-1.txt", "tema9/archivos")
zip_abierto.extractall("tema9/archivos")



# comprimir con shutil
import shutil

carpeta_origen = "tema9/"

archivo_destino = "tema9/todo_comprimido"

shutil.make_archive(archivo_destino, "zip", carpeta_origen) # comprime todo el contenido de la carpeta_origen en un archivo zip


# descomprimir con shutil
import shutil

archivo_a_descomprimir = "tema9/todo_comprimido.zip"

carpeta_destino = "tema9/extraccion"

shutil.unpack_archive(archivo_a_descomprimir, carpeta_destino) # descomprime el archivo en la carpeta_destino


