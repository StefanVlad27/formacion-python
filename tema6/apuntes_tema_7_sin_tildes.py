# programacion orientada a objetos

# clases: una clase es una plantilla o un modelo que define la estructura y el comportamiento de los objetos que se crearan a partir de ella

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


# tipos de metodos


def eliminar_acentos_en_archivo(archivo_entrada, archivo_salida):
    def eliminar_acentos(texto):
        reemplazos = {
            'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u',
            'A': 'A', 'E': 'E', 'I': 'I', 'O': 'O', 'U': 'U'
        }
        for acentuado, sin_acento in reemplazos.items():
            texto = texto.replace(acentuado, sin_acento)
        return texto

    with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    contenido_sin_acentos = eliminar_acentos(contenido)

    with open(archivo_salida, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido_sin_acentos)

# Uso de la funcion:
eliminar_acentos_en_archivo('C:\\Users\\stefanvlad\\source\\repos\\formacion-python\\tema6\\apuntes_tema6.py', 'C:\\Users\\stefanvlad\\source\\repos\\formacion-python\\tema6\\apuntes_tema_6_sin_tildes.py')
