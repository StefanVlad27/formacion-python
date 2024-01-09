# print : imprimir en pantalla
print("Buenas") # se puede usar tanto comillas simples como dobles
print("Hola \"Stefan\"") # La \ dentro de un string indica que el proximo caracter es especial
print("Primera linea\nSegunda linea") # n es un caracter especial que indica salto de linea
print("\tLinea tabulada") # t es un caracter especial que realiza una tabulacion de 4 caracteres

# input : recibe datos introducidos por teclado
input("Introduce tu nombre: ")
input("Introduce tu apellido: ")
print(input("Introduce tu edad: "))
print("Tu nombre es " + input("Introduce tu nombre:") + " y tienes " + input("Introduce tu edad: ") + " años")
print(input("Escribe tu nombre:") + "\n" + input("Escribe tu apellido:"))