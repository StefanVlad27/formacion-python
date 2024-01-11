class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}\nCuenta: {self.numero_cuenta}\nBalance: {self.balance}€"

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Se ha depositado {cantidad} en la cuenta {self.numero_cuenta}.")

    def retirar(self, cantidad):
        if self.balance >= cantidad:
            self.balance -= cantidad
            print(f"Se ha retirado {cantidad} de la cuenta {self.numero_cuenta}.")
        else:
            print(f"La cuenta {self.numero_cuenta} no tiene suficiente balance.")

def crear_usuario():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    numero_cuenta = input("Numero de cuenta: ")
    cliente = Cliente(nombre, apellido, numero_cuenta)
    return cliente

def inicio():
    mi_cliente = crear_usuario()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print("Elija una opcion: Depositar (D), Retirar (R), Salir (S)")
        opcion = input("Opcion: ").upper()

        if opcion == 'D':
            cantidad = float(input("Cantidad a depositar: "))
            mi_cliente.depositar(cantidad)
        elif opcion == 'R':
            cantidad = float(input("Cantidad a retirar: "))
            mi_cliente.retirar(cantidad)
        print(mi_cliente)

    print("Gracias por usar nuestro servicio.")

inicio()

