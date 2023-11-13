# TIPOS DE STRINGS:
# index(): string para conocer posicion de letras.
# format[]: string para dar formato a los strings.
# upper(): pasar a mayúsculas
# lower(): pasulas
# split(): separar en partes (lista)
# join(): unir items usando separador
# find(): encontrar un substring
# replace(): reemplazar a minuscar un substring


# Método index: solo se puede aplicar a los strings

# string(str) "hola","adios",'prueba' -> cualquier carácter entre comillas "" o '' es un string .

# 1. Conocer la posición de un carácter:
    mi_texto = "hola"
    print(mi_texto.index("o"))

# 2. Conocer que caracter hay en un indice
# Índice positivo. Empieza en 0.
    mi texto = "hola"
    print(mi_texto[3])

# Índice negativo. Empieza en 0 pero sigue desde atrás.s
    mi_texto = "hola"
    print(mi_texto[-3])

# Ejercicio 1: Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"
palabra = "ordenador"
print(palabra[5])

# Ejercicio 2: Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
#
# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))

# Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.rfind("práctica"))


# MÉTODO FORMAT

# Extraer substrings
texto = "ABCDEFGH"
fragmento = texto[2:5] # Coge desde el segundo caracter hasta el quinto, sin incluirlo
print(fragmento)

# SALTAR LETRAS
texto = "ABCDEFGH"
fragmento = texto[2:5:2] # Coge desde el segundo caracter hasta el quinto, sin incluirlo pero saltando de dos en dos
print(fragmento)

# Ejercicio 1: Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
frase = "Controlar la complejidad es la esencia de la programación"

fragmento = frase[:9]
print(fragmento)

# Ejercicio 2: Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmento = frase[8::3]
print(fragmento)

# Ejercicio 3: Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento = frase[::-1]
print(fragmento)


# UPPER
texto = "prueba svlad"
resultado = texto.upper()
print(resultado)

# LOWER
texto = "prueba svlad"
resultado = texto.lower()
print(resultado)

# SPLIT
texto = "prueba svlad"
resultado = texto.split( )
print(resultado)

a = "prueba"
b = "svlad"
c = " ".join([a,b])
print(c)

# FIND
texto = "prueba svlad"
resultado = texto.find("s")
print(resultado)

# REPLACE
texto = "prueba svlad"
resultado = texto.replace("svlad","dani")
print(resultado)


# EJERCICIO 1: Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:O 1:
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())

# EJERCICIO 2:Une la siguiente lista en un string, separando cada elemento con un espacio.
# Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
lista_palabras = ["La","legibilidad","cuenta."]
unir=" ".join(["La","legibilidad","cuenta."])
print(unir)

# EJERCICIO 3: Reemplaza en la siguiente frase:  "Si la implementación es difícil de explicar, puede que sea una mala idea."
#los siguientes pares de palabras: "difícil" --> "fácil" "mala" --> "buena" y muestra en pantalla la frase con ambas palabras modificadas.

texto = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = texto.replace("difícil", "fácil").replace("mala", "buena")
print(resultado)

# PROPIEDADES DE STRINGS
# - Son inmutables: su contenido no se puede modificar.
# - Pueden concatenarse mediante el signo +. También se pueden multiplicar *
# - Multilineales: permite realizar saltos de línea.
# - Lenght(): calcular largura string.

# SUMA STRINGS
n1 = "Ste"
n2 = "fan"
print(n1+n2)

# MULTIPLICACION STRINGS
n1 = "Ste"
n2 = "fan"
print(n1*10) # Repite la palabra 10 veces

# MULTILINEALES: triple comillas
n1 = """"Que
tal
estas
"""
print("estas" in n1) # te dice si el caracter está dentro del string

# LENGHT
n1 = "SteLSFKJÑLSJCÑAL"
print(len(n1))


# EJERCICIO 1: Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. Por suerte, conoces
# que los strings son multiplicables y puedes realizar esta actividad de forma simple y elegante.
a = "Repetición"
print(a*15)

# EJERCICIO 2: Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.
a = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""
print("agua" not in a)

# EJERCICIO 3: Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.
a = "electroencefalografista"
print(len(a))

# LISTAS: secuencia ordenada de objetos., da igual el tipo. va entre corchetes [] y separados por coma , . El orden de los elementos puede variar.
mi_lista = ['a', 'b', 'c']
print(type(mi_lista))

mi_lista2 = [142, 'hola', 2342.4565] # pueden almacenar objetos de diferentes tipos
mi_lista3 = mi_lista + mi_lista2 # las listas se pueden concatenar
mi_lista3[0] = 'stefan' # en la posicion 0 del indice , modificame el campo que haya por el texto
print(mi_lista3)

print(len(mi_lista3)) # tamaño de la lista

# MÉTODOS LISTAS

mi_lista3.append('g') # .append añade valores a la lista
print(mi_lista3)

mi_lista3.pop() # .pop elimina elementos de la lista. Sin parámetros, elimina el último registro.
print(mi_lista3)

mi_lista3.pop(3) # .pop elimina elementos de la lista. Debemos indicar el índice de la lista del elemento a eliminar.
print(mi_lista3)

eliminado = mi_lista3.pop(2) # puedes guardar el elemtento eliminado
print(eliminado)

desordenado = ['s', 'g', 'o', 'a', 'z']
desordenado.sort() # .sort ordena alfabeticamente o numericamente los valores
print(desordenado)
# MUY IMPORTANTE: .sort reordena la lista que existe, NO crea algo a partir de lo que ya hay.
# Si metemos el resultado en una variable, nos dará error. Para ver el resultado, volver a llamar
# a la variable ordenada.

desordenado.reverse() # ordena pero al revés, de la Z -> A y 9 -> 0.
print(desordenado)


# EJERCICIO 1: Crea una lista con 5 elementos, dentro de la variable mi_lista.
# Puedes incluir strings, booleanos, números, etc.
mi_lista = ['a', 'b', 'c', 12345, 392.42]

# EJERCICIO 2: Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append('motocicleta')

# EJERCICIO 3: Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable llamada eliminado.
# Utiliza métodos de listas sin alterar la línea de código ya suministrada.
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)



# DICCIONARIOS: {'clave':'valor','arte':'cine'} -> pares de palabras agrupados, la primera se denomina clave y la segunda valor. Van entre {}
diccionario = {'c1':'valor1', 'c2':'valor2'}
print(diccionario)

resultado = diccionario['c1'] # esta es la forma de realizar búsquedas de claves en un diccionario
print(resultado)

cliente = {'nombre':'stefan', 'apellido':'vlad', 'edad':22, 'peso':85.5}
consulta = cliente['apellido']
print(consulta)

dic = {'c1':55, 'c2':[10, 20, 30],'c3':{'s1':100, 's2':200}} # diccionario creado pero con INT, lista y otro diccionario dentro
print(dic['c2'][2]) # busca dentro de la clave 'c2' del diccionario, el segundo parámetro
print(dic['c3']['s2']) # busca dentro de la clave 'c3' del diccionario la clave 's2' de ese diccionario

dic = {'c1':['a','b','c'], 'c2':['d','e','f']}
print(dic['c2'][1].upper()) # Muestra resultado en mayuscula

cliente = {'nombre':'stefan', 'apellido':'vlad', 'edad':22, 'peso':85.5}
cliente['nacionalidad'] = 'rumania' # para añadir valores nuevos al diccionario
print(cliente)

cliente = {'nombre':'stefan', 'apellido':'vlad', 'edad':22, 'peso':85.5}
cliente['nombre'] = 'klk' # para modificar valores existentes del diccionario
print(cliente)

# MÉTODOS
print(cliente.keys()) # imprime solamente las claves del diccionario
print(cliente.values()) # imprime solamente los valores del diccionario
print(cliente.items()) # muestra los tupples


# Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:
#     nombre: Karen
#     apellido: Jurgens
#     edad: 35
#     ocupacion: Periodista
# Los nombres de las claves y valores deben ser iguales a la consigna.

#nombre: Karen
#apellido: Jurgens
#edad: 35
#ocupacion: Periodista
mi_dic = {'nombre':'Karen','apellido':'Jurgens','edad':35,'ocupacion':'Periodista'}

# Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])