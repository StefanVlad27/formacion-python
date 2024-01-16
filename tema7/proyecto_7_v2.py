class Libro:
    def __init__(self, titulo, autor,ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro_titulo(self, titulo):
        libros_titulo = []
        for libro in self.libros:
            if libro.titulo == titulo:
                libros_titulo.append(libro)
        return libros_titulo

    def buscar_libro_autor(self, autor):
        libros_autor = []
        for libro in self.libros:
            if libro.autor == autor:
                libros_autor.append(libro)
        return libros_autor

    def mostrar_libros(self):
        for libro in self.libros:
            print("\n" + libro.titulo, libro.autor, libro.ISBN + "\n")

    def mostrar_numero_libros(self):
        print(len(self.libros))

biblioteca = Biblioteca()

def crear_libro():
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    ISBN = input("ISBN: ")
    libro = Libro(titulo, autor, ISBN)
    return libro

def inicio():

    opcion = 0

    while opcion != 'S':
        print("Elija una opcion:\n\n Agregar libros (A) \n\n Buscar libros por titulo (B)\n\n Buscar libros por autor (C)\n\n Mostrar todos los libros en la biblioteca (D)\n\n Mostrar numero de libros en la biblioteca (E)\n\nSalir (S)")
        opcion = input("Opcion: ").upper()

        if opcion == 'A':
            libro = crear_libro()
            biblioteca.agregar_libro(libro)

        elif opcion == 'B':
            nombre_libro = input("Introduce el nombre del titulo: ")
            biblioteca.buscar_libro_titulo(nombre_libro)

        elif opcion == 'C':
            nombre_autor = input("Introduce el nombre del autor: ")
            biblioteca.buscar_libro_autor(nombre_autor)

        elif opcion == 'D':
            biblioteca.mostrar_libros()

        elif opcion == 'E':
            biblioteca.mostrar_numero_libros()

        else:
            print("Opcion no valida")

    print("Gracias por usar nuestro servicio.")

inicio()

