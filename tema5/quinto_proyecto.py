from random import choice

palabras = ["manzana", "platano", "zanahoria", "perro", "elefante", "pez", "guitarra", "casa", "helado", "selva", "canguro", "portatil", "luna", "ninja", "pulpo", "pinguino", "colcha", "arcoiris", "futbol", "tigre", "paraguas", "violin", "cascada", "xilofono", "yate", "cebra"]
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas

def pedir_letra():
    letra_elegida = ""
    es_valida = False
    abecedario = 'abcdefghijklmnopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ").lower()

        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("Elige una letra correcta.")

    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):

    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)

        else:
            lista_oculta.append("_")

    print(" ".join(lista_oculta))

def comprobar_letra(letra_elegida, palabra_oculta, vidas, coincidencias):

    fin = False

    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias

def perder():
    print("Has perdido. No hay más vidas.")
    print(f"La palabra oculta era {palabra}.")

    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Has ganado.")

    return True



palabra,letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print("\n" + '*' * 20 + "\n")
    mostrar_nuevo_tablero(palabra)
    print("\n")
    print("Letras incorrectas:" + '-'.join(letras_incorrectas))
    print(f"Vidas: {intentos}")
    print("\n" + '*' * 20 + "\n")

    letra = pedir_letra()
    intentos, terminado, aciertos = comprobar_letra(letra, palabra, intentos,aciertos)

    juego_terminado = terminado

