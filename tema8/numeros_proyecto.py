# GENERADORES
def numeros_perfumeria():
    for n in range(1,10000):
        yield f"P - {n}"

def numeros_farmacia():
    for n in range(1,10000):
        yield f"F - {n}"

def numeros_cosmetica():
    for n in range(1,10000):
        yield f"C - {n}"


p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()


# DECORADORES
def decorador(funcion):

    print("\n" + "-"*20)
    print("Su numero es: ")

    if funcion == "p":
        print(next(p))

    elif funcion == "f":
        print(next(f))

    else:
        print(next(c))

    print("Espere a ser atendido.")
    print("-"*20 + "\n")

