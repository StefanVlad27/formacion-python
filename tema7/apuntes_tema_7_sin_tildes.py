# programacion orientada a objetos

# clases: una clase es una plantilla o un modelo que define la estructura y el comportamiento de los objetos que se crearan a partir de ella
# atributos: dentro de la clase, defines los atributos que serán variables que pertenecerán a los objetos creados a partir de la clase. Estos atributos son características de los objetos.
# metodos: Métodos (Methods): También dentro de la clase, defines los métodos que son funciones que describen el comportamiento o las acciones que los objetos de esa clase pueden realizar.
# instancia: Fuera de la clase, creas una instancia u objeto concreto utilizando la clase como base. Cada instancia representa un objeto individual y contiene los atributos y métodos definidos en la clase.

# Definición de la clase:
class Pajaro:

    # Atributo 1
    def __init__(self, color, especie):
        self.color = color  # Atributo: color
        self.especie = especie  # Atributo: especie

    # Método
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros.")

    # Método + atributo
    def piar(self, voz):
        print("pio "+ voz + " mi color es {}".format(self.color))


# instancia
piolin = Pajaro('negro', 'Tucan')

# Llamada al método piar en la instancia piolin
piolin.piar("aguda") # pio, mi color es negro

# Llamada al método volar en la instancia piolin
piolin.volar(50) # El pajaro ha volado 50 metros.







class Pajaro:
    pass

mi_pajaro = Pajaro() # asi se define una instancia. en este caso se ha definido la instancia mi_pajaro a raiz de la clase
otro_pajaro = Pajaro() # otra instancia


# EJERCICIOS

# Crea una clase llamada Personaje y a continuacion, crea un objeto a partir de ella, por ejemplo: harry_potter
class Personaje:
    pass

harry_potter = Personaje()

# Crea una clase llamada Dinosaurio, y tres instancias a partir de ella: velociraptor, tiranosaurio_rex y braquiosaurio .
class Dinosaurio:
    pass

velociraptor = Dinosaurio()
tiranosaurio_rex = Dinosaurio()
braquiosaurio  = Dinosaurio()

# Crea una clase llamada PlataformaStreaming y crea los siguientes objetos a partir de ella: netflix, hbo_max, amazon_prime_video
class PlataformaStreaming:
    pass

netflix = PlataformaStreaming()
hbo_max = PlataformaStreaming()
amazon_prime_video = PlataformaStreaming()


# atributos: hay diferentes tipos:
# atributos de clase: pertenecen directamente a la clase y se les aplica a todos los objetos que se creen con esa clase
# atributos de instancia: pertenecen a la instancia del objeto creado a partir de la clase

# atributos de instancia:

class Pajaro:

    def __init__(self, color): # asi se define el metodo constructor que va a asignar un atributo a la clase
        self.color = color

mi_pajaro = Pajaro('negro')

print(mi_pajaro) # Devuelve la clase del objeto: <__main__.Pajaro object at 0x0000018CD35D7F90>
print(mi_pajaro.color) # Devuelve el valor: "negro"


class Pajaro:

    def __init__(self, color,especie): # para definir varios atributos
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('negro', 'Tucan')

print(mi_pajaro.color, mi_pajaro.especie)



# Crea una clase llamada Casa, y asignale atributos: color, cantidad_pisos.
# Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.
class Casa:

    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa('blanco',4)


# Crea una clase llamada Cubo, y asignale el atributo de clase:
#     caras = 6
# y el atributo de instancia:
#     color
# Crea una instancia cubo_rojo, de dicho color.

class Cubo:
    caras = 6

    def __init__(self, color):
        self.color = color


cubo_rojo = Cubo("rojo")



# Crea una clase llamada Personaje, y asignale el siguiente atributo de clase:
#     real = False
# Crea una instancia llamada harry_potter con los siguientes atributos de instancia:
#     especie = "Humano"
#     magico = True
#     edad = 17

class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad


harry_potter = Personaje("Humano", True, 17)


# como crear metodos de clases.

class Pajaro:

    def __init__(self, color,especie): # para definir varios atributos
        self.color = color
        self.especie = especie

    def piar(self): # creamos el primer metodo
        print("pio, mi color es {}".format(self.color))

    def volar(self,metros): # el segundo metodo. tendremos que darle el valor de metros.
        print(f"El pajaro ha volado {metros} metros.")

piolin = Pajaro('negro', 'Tucan') # aqui definimos los atributos

piolin.piar() # pio, mi color es negro
piolin.volar(50) # tenemos que definir los metros. "El pajaro ha volado 50 metros."



# EJERCICIOS:

# Crea una clase Perro. Dicho perro debe poder ladrar.
# Crea el metodo ladrar() y ejecutalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla "Guau!".

class Perro:

    def ladrar(self):
        print("Guau!")

Perro().ladrar()

# Crea una clase llamada Mago, y crea un metodo llamado lanzar_hechizo() (debera imprimir "¡Abracadabra!").
# Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo

class Mago:

    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin = Mago()

merlin.lanzar_hechizo()

# Crea una instancia de la clase Alarma, que tenga un metodo llamado postergar(cantidad_minutos). El metodo debe imprimir en pantalla el mensaje
# "La alarma ha sido pospuesta {cantidad_minutos} minutos"

class Alarma:

    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

mi_alarma = Alarma()

mi_alarma.postergar(20)


# tipos de metodos:

# metodos de instancia: afectan a cada instancia dentro de la clase.
# acceden y modifican atributos del objeto
# accede a otros metodos
# modifica el estado de la clase
# class pajaro:
#   def mi_metodo(self):
#       print("algo")

class Pajaro:

    def __init__(self, color,especie): # para definir varios atributos
        self.color = color
        self.especie = especie

    def piar(self): # creamos el primer metodo
        print("pio, mi color es {}".format(self.color))

    def volar(self,metros): # el segundo metodo. tendremos que darle el valor de metros.
        print(f"El pajaro ha volado {metros} metros.")
        self.piar() # podemos llamar a otro metodo

    def pintar_negro(self):
        self.color = 'negro'
        print(f"El pajaro ahora es {self.color}") # podemos modificar el valor de color.


piolin = Pajaro('negro', 'Tucan') # aqui definimos los atributos

piolin.piar() # pio, mi color es negro
piolin.volar(50) # tenemos que definir los metros. "El pajaro ha volado 50 metros."




# metodos de clase @classmethod: no necesitan crear una instancia para poder ejecutarse
# @classmethod
# def mi_metodo(cls):
# #         print("algo")

class Pajaro:

    alas = True

    def __init__(self, color,especie): # para definir varios atributos
        self.color = color
        self.especie = especie

    def piar(self): # creamos el primer metodo
        print("pio, mi color es {}".format(self.color))

    def volar(self,metros): # el segundo metodo. tendremos que darle el valor de metros.
        print(f"El pajaro ha volado {metros} metros.")
        self.piar() # podemos llamar a otro metodo

    def pintar_negro(self):
        self.color = 'negro'
        print(f"El pajaro ahora es {self.color}") # podemos modificar el valor de color.

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Ha puesto {cantidad} huevos")

Pajaro.poner_huevos(2) # permite llamar al atributo sin definir una instancia de la clase




# metodos estaticos @staticmethod
# es independiente a todos los demas argumentos y es inamovible

class Pajaro:

    alas = True

    def __init__(self, color,especie): # para definir varios atributos
        self.color = color
        self.especie = especie

    def piar(self): # creamos el primer metodo
        print("pio, mi color es {}".format(self.color))

    def volar(self,metros): # el segundo metodo. tendremos que darle el valor de metros.
        print(f"El pajaro ha volado {metros} metros.")
        self.piar() # podemos llamar a otro metodo

    def pintar_negro(self):
        self.color = 'negro'
        print(f"El pajaro ahora es {self.color}") # podemos modificar el valor de color.

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Ha puesto {cantidad} huevos")

    @staticmethod
    def mirar():
        print("El pajaro mira.")

Pajaro.poner_huevos(2) # permite llamar al atributo sin definir una instancia de la clase


# EJERCICIOS

# Crea un método estático respirar() para la clase Mascota. Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"
class Mascota:

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


Mascota().respirar()


# Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en
# True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.
class Jugador:
    vivo = False

    def revivir(self):
        vivo = True


Jugador().revivir()



# Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en True
# cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.

class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True



# Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de Personaje,
# que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.
class Personaje:

    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1
        print(self.cantidad_flechas)


stefan = Personaje(30)
stefan.lanzar_flecha()





# herencia : hereda las funcionalidades y atributos de la clase que le indiquemos.

# class Padre: una clase con sus atributos
#     ...
#     ...
#     ...


# class Hijo(Padre): la clase hereda  los atributos que tenía la clase Padre
#     ... metodos heredados
#     ... metodos modificados
#     ... metodos nuevos

class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

piolin = Pajaro(2, "amarillo")

print(piolin.color) # podemos acceder a la clase nacer a través de la herencia




# EJERCICIOS


# Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: nombre, edad. Crea otra clase, Alumno,
# que herede de la primera estos atributos.
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass


# Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: edad, nombre, cantidad_patas.
# Crea otra clase, Perro, que herede de la primera sus atributos.
class Mascota:
    def __init__(self,edad,nombre,cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass


# Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() (puedes dejar el código de los métodos en blanco con pass).
# Crea una clase llamada Automovil que herede estos métodos de Vehiculo.
class Vehiculo:
    def acelerar(self):
        pass
    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass



# herencia extendida:

# modificar herencia
class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal ha hablado")

class Pajaro(Animal):
    def nacer(self):
        print("muerte")

piolin = Pajaro(2, "amarillo")

piolin.nacer() # la primera herencia es sobreescribida por la clase Pajaro


# añadir atributo a una clase que tiene herencia
class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
        print(edad)
        print(color)

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal ha hablado")

class Pajaro(Animal):
    def nacer(self):
        print("muerte")

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color) # esta linea se agrega para no volver a escribir self.edad = edad... es equivalente
        self.altura_vuelo = altura_vuelo
        print(altura_vuelo)

piolin = Pajaro(22, "negro", 4234)


# herencias multiples

class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("jsjasjdajaja")

    def hablar(self):
        print("Klk")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()


# ejercicios

# Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocación, y hoy tienen el mismo trabajo en
# la Fiscalía, crea la herencia múltiple que le permita a esta clase heredar correctamente de Padre y Madre.
class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")

class Hija(Madre, Padre):
    pass



# Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, tal que "construyas" un
# animal que tiene los siguientes métodos y atributos:
#
# - poner_huevos()
# - tiene_pico = True
# - vertebrado = True
# - venenoso = True
# - nadar()
# - caminar()
# - amamantar()
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    pass


# Un hijo ha heredado de su padre todas sus características, sin embargo, tienen diferentes hobbies. Logra que la clase Hijo herede
# de Padre todos sus métodos y atributos, sobreescribiendo el método hobby() para que se devuelva[1]: "Juego videojuegos en mi tiempo libre"
class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"

class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"



# polimorfismo: objetos de clases distintas pueden tener métodos con el mismo nombre pero implementaciones diferentes
class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Soy la vaca " + self.nombre + "\nmuuu")

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Soy la oveja " + self.nombre + "\nbeeee")

vaca1 = Vaca('Lola')
oveja1 = Oveja('Paca')
vaca1.hablar()
oveja1.hablar()

def animal_habla(animal):
    animal.hablar()


animal_habla(vaca1)


# ejercicios:

# La función incorporada en Python len() tiene un comportamiento polimórfico, ya que calcula el largo de un objeto en función
# de su tipo (strings, listas, tuples, entre otros), devolviendo la cantidad de items o caracteres que lo componen.
# Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla (print()) para cada uno de
# ellos su longitud con la función len().

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

nuevo = [palabra,lista,tupla]

for n in nuevo:
    print(len(n))


# Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos.
# Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, llamando al método atacar()
# de cada uno de los personajes. Deberás crear instancias de cada una de las clases anteriores para construir un iterable
# (una lista llamada personajes) que pueda recorrese en dicho orden.

class Mago():
    def atacar(self, ):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

mago = Mago()
arquero = Arquero()
samurai = Samurai()

personajes = [arquero, mago, samurai]

for personaje in personajes:
    personaje.atacar()


# Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa específicos.
# Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia de las clases de tus personajes),
# y ejecutar su método defender() independientemente de qué tipo de personaje se trate.

class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

mago = Mago()
arquero = Arquero()
samurai = Samurai()

personajes = [arquero, mago, samurai]

def personaje_defender(personajes):
    personajes.defender()




# metodos especiales: sirve para definir metodos predeterminados en base a las clases que se creen y las llamadas a sus instancias
class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self): # de esta manera indicamos la respuesta a un print de la clase.
        return f"CD: {self.titulo} Autor: {self.autor}"

    def __len__(self): # aqui le indicamos que es lo que tiene que hacer cuando en una llamada posterior se llame al metodo len
        return self.canciones

    def __del__(self):
        print("Se ha eliminado el objeto")

mi_cd = CD("Nirvana", "Nevermind", 12)

print(mi_cd) # de esta manera, va a aparecer lo que hemos definido en el metodo __str__
print(len(mi_cd)) # de esta manera, va a aparecer lo que hemos definido en el metodo __len__

del mi_cd # de esta manera, eliminamos la instancia de la clase CD


# Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima el objeto, devuelva '"{titulo}", de {autor}'
# (atención: el título debe estar encerrado entre comillas dobles).
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'


# Dada la clase Libro, implementa el método especial __len__ para que cada vez que se ejecute la función len() sobre el mismo,
# devuelva el número de páginas como número entero.

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return int(self.cantidad_paginas)


# Dada la clase Libro, implementa el método especial __del__ para que el usuario sea informado con el mensaje "Libro eliminado",
# mostrándolo en pantalla cada vez que el libro se elimine.
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")
        