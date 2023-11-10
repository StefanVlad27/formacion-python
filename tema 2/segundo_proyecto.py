nombre = input("Introduce tu nombre: ")
cantidad = input("Cantidad vendida este mes: ")

cantidad = float(cantidad)

redondeo = round((cantidad)*0.13,2)

print(f"{nombre}, te corresponden {redondeo}€ de comisiones")