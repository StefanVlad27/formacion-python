import os
import re
import datetime
import math
import time
from pathlib import Path

inicio = time.time()

ruta = os.path.abspath("./proyecto/Mi_Gran_Directorio")
mi_patron = r"N\D{3}-\d{5}"
hoy = datetime.datetime.today()
nros_encontrados = []
archivos_encontrados = []

def buscar_numero(archivo, patron):

    este_archivo = open(archivo, "r")
    texto = este_archivo.read()

    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''


def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta, a), mi_patron)
            if resultado != '':
                nros_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())


def mostrar_todo():
    indice = 0

    print("-" * 50)
    print(f"Fecha: {hoy.day}/{hoy.month}/{hoy.year}")
    print("\n")
    print("ARCHIVO\t\t\t\tNRO. SERIE")
    print("-------\t\t\t\t\t----------")

    for a in archivos_encontrados:
        print(f"{a}\t\t\t\t{nros_encontrados[indice]}")
        indice += 1
    print('\n')
    print(f"Numeros encontrados: {len(nros_encontrados)}")
    fin = time.time()
    duracion = fin - inicio
    print(f"Duracion: {math.ceil(duracion)} segundos")
    print("-" * 50)


crear_listas()
mostrar_todo()