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

    # Método 1
    def piar(self):
        print("pio, mi color es {}".format(self.color))

    # Método 2
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros.")

# instancia
piolin = Pajaro('negro', 'Tucan')

# Llamada al método piar en la instancia piolin
piolin.piar() # pio, mi color es negro

# Llamada al método volar en la instancia piolin
piolin.volar(50) # El pajaro ha volado 50 metros.







class Pajaro:
    pass

mi_pajaro = Pajaro() # asi se define un objeto. en este caso se ha definido el objeto mi_pajaro a raiz de la clase
otro_pajaro = Pajaro() # otro objeto


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

