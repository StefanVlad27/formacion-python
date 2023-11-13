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

# EJERCICIO 2:Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
lista_palabras = ["La","legibilidad","cuenta."]
unir=" ".join(["La","legibilidad","cuenta."])
print(unir)

# EJERCICIO 3: Reemplaza en la siguiente frase:  "Si la implementación es difícil de explicar, puede que sea una mala idea." los siguientes pares de palabras: "difícil" --> "fácil" "mala" --> "buena" y muestra en pantalla la frase con ambas palabras modificadas.

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


# EJERCICIO 1: Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. Por suerte, conoces que los strings son multiplicables y puedes realizar esta actividad de forma simple y elegante.
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

# LISTAS:
