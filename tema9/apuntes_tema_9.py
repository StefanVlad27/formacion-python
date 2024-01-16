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



