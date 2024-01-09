# Tipos de datos:

# string(str) "hola","adios",'prueba' -> cualquier caracter entre comillas "" o '' es un string .
# integer(int) 1, 2, 4, 6 -> numeros enteros
# floating(float) 1.7, 923.14, -934 -> numeros decimales y/o negativos
# listas(lst) ["sal", 1.5, -3] -> lista de objetos, da igual el tipo. va entre corchetes [] . El orden de los elementos puede variar.
# diccionarios(dic) {'color':'rojo','arte':'cine'} -> pares de palabras agrupados, la primera se denomina clave y la segunda valor. Van entre {}
# tuples(tuple) [("sal", 1.5), ("temperatura", -3)] -> lista de objetos, da igual el tipo. va entre parentesis () pero a diferencia de la lista, el orden de los elementos NO varia
# sets(set) {'a','b','c'} -> lista de objetos UNICOS, no se pueden repetir. Van entre {}
# booleanos(bool) True, false -> solo puede tener dos valores. Se usa para comprobar si las condiciones se cumplen


#  Reglas a la hora de definir  variables
# Regla 1: nombres descriptivos faciles de entender que son
# Regla 2: si el nombre de la variable es compuesto, separarlo por guiones bajos _
# Regla 3: omitir tildes y la ñ a la hora de declararlas
# Regla 4: las variables no pueden empezar por un numero pero si contenerlo.
# Regla 5: no se admiten signos
# Regla 6: no se admiten que el nombre de la variable contenga palabras claves de python, como print input string int ...


# Integers y floats
mi_numero = 2+2 # tipo integer al ser entero
print(mi_numero + mi_numero)
print(type(mi_numero))

mi_numero = 8.6 # tipo float al ser decimal
print(mi_numero)
print(type(mi_numero))

edad = input("Escribe tu edad: ")
print(type(edad)) # los datos introducidos en un input, aun siendo un numero son de tipo str



# Conversiones entre tipos de datos: existen dos tipos
# Implicita: conversion realizada automaticamente por python.
# Explicita: conversion realizada por el usuario en el codigo

# Ejemplo conversion explicita
primer_valor = 22 # valor de tipo int
print(type(primer_valor))

segundo_valor = str(primer_valor) # se cambia a str
print(type(segundo_valor))

# Ejemplo conversion implicita
num1 = 20
num2 = 30.5

num1 = num1 + num2 # al ser el resultado con decimales num1 pasa a ser float
print(type(num1))



# Formateo de cadenas, dos tipos: funcion format y cadenas literales

# Funcion Format
x = 10
y = 5
print("La suma de {} y {} es igual a {}".format(x,y,x+y))

# Cadenas literales
color = "rojo"
matricula = 54232
print(f"El coche es {color} y su matricula es {matricula}") # si añadimos f podremos usar variables definidas sin necesidad de concatenar



# Operadores matematicos
x = 6
y = 2
z = 7

print(f"{x} mas {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} entre {y} es igual a {x/y}")
print(f"{z} dividido enteramente de {y} es igual a {z//y}") # esto significa que si el resultado es decimal, lo elimina quedandose solo con el entero
print(f"El resto de dividir {z} entre {y} es {z%y}") # calcula el resto de la division
print(f"{x} elevado a {y} es igual a {x**y}") # realiza elevaciones
print(f"La raiz cuadrada de {x} es {x**0.5}") # calcula raiz cuadrada



# Redondeo: se usa la funcion round(). se le pueden pasar 1 o 2 parametros

# Si le pasamos 2 parametros, va a sumar 1 al ultimo caracter indicado el funcion de si el siguiente decimal es mayor que 5 o menor.
x = 8.2667
y = round(x,2)
print(y) # resultado 8.27

# Si no indicas segundo parametro, redondeara hacia arriba o hacia abajo, segun cual este mas cerca
x = 2.32
y = round(x)
print(y) # resultado 2

# Si el valor es justo la mitad, redondeara hacia arriba
x = 6.72
y = round(x)
print(y) # resultado 7

# Ejercicios:
# Redondea el resultado de la division 10/3 a un numero con 2 decimales, y muestra en pantalla el valor redondeado
resultado = round(10/3,2)
print(resultado)

#Redondea el numero 10.676767 al entero mas proximo, y muestra en pantalla el resultado.
valor = 10.676767
print(round(valor))

valor = 10.676767
y = round(valor)
print(y)

# Calcula la raiz cuadrada de 5, y muestra en pantalla el resultado redondeado con 4 posiciones decimales.
print(f"{round(5**0.5,4)}")



