texto = input("Introduce una cadena de texto: ")
letras = []

texto = texto.lower()

letras.append(input("Introduce una letra: ").lower())
letras.append(input("Introduce otra letra: ").lower())
letras.append(input("Introduce otra letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras} veces.")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces.")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces.")

print("\n")
print("CANTIDAD DE PALABRAS"")
palabras = texto.split()
print(palabras)

print("\n")
print("LETRAS DE INICIO Y FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La primera letra es '{letra_inicio}'y la última '{letra_final}'")

print("\n")
print("TEXTO AL REVES")
palabras.reverse()
texto_alreves = ' '.join(palabras)
print(f"El texto al revés es: '{texto_alreves}'")

print("\n")
print("BUSCAR PALABRA PYTHON")
buscar = 'python' in texto
dic = {True:"sí", False:"no"}
print(f"La palabra 'Python' {dic[buscar]} se encuentra")

