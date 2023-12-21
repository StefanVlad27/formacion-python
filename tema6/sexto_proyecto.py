import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "Recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador

# Menú de inicio

def inicio():
    system('cls')
    print("*" * 42)
    print("*" * 5 + " Bienvenido al admin de recetas " + "*" * 5)
    print("*" * 42)
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)}")

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opción:")
        print('''
        [1] - Leer receta
        [2] - Crear receta
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa
        ''')

        eleccion_menu = input()
    return eleccion_menu

def mostrar_categorias(ruta):
    print("Categorias: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElije una categoría: ")

    return lista[int(eleccion_correcta) -1]

def mostrar_recetas(ruta):
    print("Recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1

    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta = "x"

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElije una receta: ")

    return lista[int(eleccion_receta) -1]

menu = 0

if menu == 1:
    mis_categorias = mostrar_categorias(mi_ruta)

    mi_categoria = elegir_categoria(mis_categorias)

    mis_recetas = mostrar_recetas(mi_categoria)

    mi_receta = elegir_recetas(mis_recetas)

    # leer receta

    # volver inicio
    pass

elif menu == 2:
    mostrar_categorias = mostrar_categorias(mi_ruta)

    mi_categoria = elegir_categoria(mis_categorias)

    # crear receta nueva

    # volver inicio
    pass

elif menu == 3:
    # crear categoria

    # volver inicio
    pass

elif menu == 4:
    mostrar_categorias = mostrar_categorias(mi_ruta)

    mi_categoria = elegir_categoria(mis_categorias)

    mis_recetas = mostrar_recetas(mi_categoria)

    mi_receta = elegir_recetas(mis_recetas)

    # eliminar receta

    # volver inicio
    pass

elif menu == 5:
    mostrar_categorias = mostrar_categorias(mi_ruta)

    mi_categoria = elegir_categoria(mis_categorias)

    # eliminar categoria
    pass
elif menu == 6:
    # finalizar programa
    pass