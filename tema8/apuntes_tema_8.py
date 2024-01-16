# manejo de errores

# ejemplo:
try:     # codigo que queremos probar
    numero = int(input("Introduce un numero: "))
    print("El numero es: ", numero)
except: # codigo que se ejecuta si hay un error
    print("El valor introducido no es un numero")
else: # codigo que se ejecuta si no hay error
    print("El numero es correcto")
finally: # codigo que se ejecuta siempre
    print("Fin del programa")



def pedir_numero():
    while True:
        try:
            numero = int(input("Introduce un numero: "))

        except:
            print("El valor introducido no es un numero")

        else:
            print('El numero es' , numero)
            break

    print("Fin del programa")

pedir_numero()




# ejercicios:

# Hemos visto en la lección de qué manera se implementa el manejo de errores habitualmente en Python. En el caso de este
# ejercicio, sin embargo, necesitaré que lo hagamos de una forma ligeramente distinta para que pueda ser evaluado: deberás
# implementarlo DENTRO de la función. En forma de comentario, verás un ejemplo de resolución. Ten presente, sin embargo,
# que la forma preferida es la que hemos visto en clase.
# Implementa para la siguiente función suma(), un manejador de errores simple que ante cualquier error, imprima en pantalla
# el mensaje: "Error inesperado". En caso contrario, deberá limitarse a mostrar el resultado de la suma entre los dos números.

def suma(num1, num2):
    try:
        print(num1 + num2)
    except:
        print("Error inesperado")


# Hemos visto en la lección de qué manera se implementa el manejo de errores habitualmente en Python. En el caso de este ejercicio,
# sin embargo, necesitaré que lo hagamos de una forma ligeramente distinta para que pueda ser evaluado: deberás implementarlo
# DENTRO de la función. En forma de comentario, verás un ejemplo de resolución. Ten presente, sin embargo, que la forma preferida es la que hemos visto en clase.
# Implementa para la siguiente función cociente(), un manejador de errores:
# Ante un error de tipo (TypeError), debe imprimir en pantalla el mensaje: "Los argumentos a ingresar deben ser números"
# Si se generara una división por cero (error del tipo ZeroDivisionError), el mensaje mostrado debe ser: "El segundo argumento no debe ser cero"
# En caso que no se produzca un error, deberá limitarse a imprimir el resultado del cociente (división) entre los dos números entregados como argumento.

def cociente(num1, num2):
    try:
        print(num1 / num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")

# Implementa un manejador de errores dentro de la siguiente función, abrir_archivo():
# En caso de que el archivo que se intenta abrir no pueda ser hallado (FileNotFoundError), mostrar en pantalla el mensaje: "El archivo no fue encontrado"
# En caso de que otro tipo de error ocurra, mostrar el mensaje: "Error desconocido"
# Si no se produce ningún error, imprimir en pantalla: "Abriendo exitosamente"
# En todos los casos, al finalizar, imprimir: "Finalizando ejecución"



def abrir_archivo(fichero):
    try:
        archivo = open(fichero)

    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")

abrir_archivo('archivo.txt')

# pylint: es un analizador de código estático que busca errores en el código
# pip install pylint
# py -m pylint \\ruta\\al\\fichero.py -r y

numero1 = 5
print(Numero1)


# decoradores: son funciones que modifican el comportamiento de otras funciones.
# Un decorador en Python es una función que toma otra función como argumento y agrega
# funcionalidad adicional a esa función sin modificar su código interno.

def mayusculas(texto):
    return texto.upper()

def minusculas(texto):
    return texto.lower()

mi_funcion = mayusculas # asignamos la funcion a una variable
print(mi_funcion("hola mundo"))

mi_funcion = minusculas
print(mi_funcion("HOLA MUNDO"))



def una_funcion(funcion):
    return funcion

una_funcion(mayusculas("hola mundo")) # llamamos a la funcion mayusculas dentro de la funcion una_funcion


# ejemplo de decorador:
def cambiar_letras(tipo):

    def mayusculas(texto):
        return texto.upper()

    def minusculas(texto):
        return texto.lower()

    if tipo == "mayusculas":
        return mayusculas
    elif tipo == "minusculas":
        return minusculas

operacion = cambiar_letras("mayusculas")
print(operacion("hola mundo"))


# funcion que se va a encargar de decorar cualquier funcion que le pasemos como argumento:

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")

    return otra_funcion


def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())


minusculas("hola mundo") # hola mundo
mayusculas("hola mundo") # HOLA MUNDO

# decoramos las funciones:
mayusculas = decorar_saludo(mayusculas)
minusculas = decorar_saludo(minusculas)

mayusculas("hola mundo") # Hola HOLA MUNDO Adios
minusculas("hola mundo") # Hola hola mundo Adios



# generadores: son funciones que nos van a permitir obtener valores a medida que los necesitemos.

def mi_funcion():
    return 4

def mi_generador():
    yield 4


print(mi_funcion()) # 4
print(mi_generador()) # <generator object mi_generador at 0x0000021B7F4E0C80>

g = mi_generador()
print(next(g)) # 4



# ejemplo:
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")
ciudades_devueltas2 = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")



print(next(ciudades_devueltas)) # Madrid
print(next(ciudades_devueltas)) # Barcelona
print(next(ciudades_devueltas)) # Bilbao
print(next(ciudades_devueltas)) # Valencia
print(next(ciudades_devueltas)) # Error: StopIteration: no hay mas elementos a devolver.



# ejemplo 2:

def mi_generador():
    x = 1
    yield x

    x += 1
    yield x


print(next(mi_generador())) # 1
print(next(mi_generador())) # 2: muestra el 2 porque la funcion se queda en el yield 2
print(next(mi_generador())) # 3: muestra el 3 porque la funcion se queda en el yield 3




# ejercicios:

# Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números,
# iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next.

def mi_generador():
    x = 0
    while True:
        yield x
        x += 1

generador = mi_generador()
print(next(generador))


# Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7,
# iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).

def mi_generador():
    x = 7
    while True:
        yield x
        x += 7

generador = mi_generador()

# Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea llamado:
#     "Te quedan 3 vidas"
#     "Te quedan 2 vidas"
#     "Te queda 1 vida"
#     "Game Over"
# Almacena el generador en la variable perder_vida
def mi_generador():
        yield "Te quedan 3 vidas"
        yield "Te quedan 2 vidas"
        yield "Te queda 1 vida"
        yield "Game Over"

perder_vida = mi_generador()

