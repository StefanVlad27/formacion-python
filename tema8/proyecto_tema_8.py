import numeros_proyecto

def pregunta():

    print("Bienvenido a la tienda")

    while True:
        print("[P] - Perfumería \n[F] - Farmacia \n[C] - Cosmética")
        print("[S] - Salir")

        try:
            mi_rubro = input("Opción: ").upper()
            ["P", "F", "C", "S"].index(mi_rubro)

        except ValueError:
            print("Opción incorrecta")
            continue

        else:
            break

    numeros_proyecto.decorador(mi_rubro)

def inicio():

    while True:
        pregunta()

        try:
            otro_turno = input("Quieres otro turno? [S/N]: ").upper()
            ["S", "N"].index(otro_turno)

        except ValueError:
            print("No es una opcion valida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()