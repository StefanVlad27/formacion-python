# El web scraping es una técnica de extracción automatizada de información de sitios web

import bs4
import requests

resultado = requests.get("https://escueladirecta.com/")

sopa = bs4.BeautifulSoup(resultado.text, "html.parser") # esto se hace para que el texto pueda ser leído por bs4

print(sopa.select('title')) # añadimos el tipo de etiqueta que queremos seleccionar

print(sopa.select('title')[0].getText()) # añadimos el tipo de etiqueta que queremos seleccionar y el índice de la lista

parrafo_especial = sopa.select('p') #   añadimos el nombre de la clase que queremos seleccionar

parrafo_especial = sopa.select('p')[3].getText() #   añadimos el nombre de la clase que queremos seleccionar y el índice de la lista

columna_lateral = sopa.select('.content p') #   añadimos el nombre de la clase que queremos seleccionar
print(columna_lateral)

for p in columna_lateral:
    print(p.getText())



# extraer imagenes

resultado = requests.get("https://escueladirecta.com/courses")

sopa = bs4.BeautifulSoup(resultado.text, "html.parser") # esto se hace para que el texto pueda ser leído por bs4

imagenes = sopa.select('.course-box-image')[0]['src'] #   añadimos el nombre de la clase que queremos seleccionar y el índice de la lista

for i in imagenes:
    print(i)

imagen_curso_1 = requests.get(imagenes)

f = open('imagen_curso_1.jpg', 'wb') # wb es para escribir en binario
f.write(imagen_curso_1.content)
f.close()


# explorar multiples paginas

import bs4
import requests

url_base = "https://books.toscrape.com/catalogue/page-{}.html"

for n in range(1,11):
    print(url_base.format(n))


# identificar condiciones de extracción
import bs4
import requests

url_base = "https://books.toscrape.com/catalogue/page-{}.html"

resultado = requests.get(url_base.format(1)) # añadimos el formato de la url
sopa = bs4.BeautifulSoup(resultado.text, "html.parser") # esto se hace para que el texto pueda ser leído por bs4

print(sopa.select(".product_pod")) # añadimos el nombre de la clase que queremos seleccionar


# extraer información de una página
import bs4
import requests

url_base = "https://books.toscrape.com/catalogue/page-2.html"

resultado = requests.get(url_base.format(1)) # añadimos el formato de la url
sopa = bs4.BeautifulSoup(resultado.text, "html.parser") # esto se hace para que el texto pueda ser leído por bs4

libros = sopa.select(".product_pod")

ejemplo = libros[0].select('.star-rating.Three') # añadimos el nombre de la clase que queremos seleccionar despues del punto .
print(ejemplo)


# combinacion de items
import bs4
import requests

url_base = "https://books.toscrape.com/catalogue/page-{}.html"

# lista de titulos con 4 o 5 estrellas
titulos_4_5_estrellas = []

# iterar paginas
for pagina in range(1,51):

    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "html.parser")

     # seleccionar datos de los libros
    libros = sopa.select(".product_pod")

     # iterar libros
    for libro in libros:
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            titulo = libro.select('a')[1]['title']
            titulos_4_5_estrellas.append(titulo)

# imprimir lista de titulos
for t in titulos_4_5_estrellas:
    print(t)