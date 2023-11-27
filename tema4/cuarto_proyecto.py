# MI CÓDIGO
from random import randint

aleatorio = randint(1,100)
nombre = input("Introduce tu nombre: ")

numero = int(input(f"De acuerdo {nombre}, he pensado un número entre el 1 y el 100, intenta adivinarlo."))

intentos = 8


while intentos > 0:
    if numero > aleatorio:
        intentos -= 1
        numero = int(input(f"Error. El número {numero} es mayor que el número generado. Introduce un valor nuevo.  Te quedan {intentos} intentos."))
    elif numero < aleatorio:
        intentos -= 1
        numero = int(input(f"Error. El número {numero} es menor que el número generado. Introduce un valor nuevo. Te quedan {intentos} intentos."))
    else:
        print(f"Enhorabuena. El número {numero} es el correcto. Te quedaban {intentos} intentos.")
        break
else:
    print("Te has quedado sin vidas.")


# SOLUCIÓN:
from random import randint

estimado = 0
intentos = 0
numero_secreto = randint(1,100)

nombre = input("Introduce tu nombre: ")

print(f"De acuerdo {nombre}, he pensado un número entre el 1 y el 100, intenta adivinarlo.")

while intentos < 8:
    estimado = int(input("Introduce un número: "))
    intentos += 1

    if estimado not in range(1,101):
        print("Introduce un número entre 1 y 100.")

    elif estimado < numero_secreto:
        print("El número es más alto")

    elif estimado > numero_secreto:
        print("El número es más bajo")

    else:
        print(f"Enhorabuena. El número {numero_secreto} es el correcto. Te ha tomado {intentos} intentos.")
        break

if estimado != numero_secreto:
    print("Te has quedado sin vidas.")
