import pygame
import random
import math
from pygame import mixer

# inicializar pygame
pygame.init()

# crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# título icono y fondo
pygame.display.set_caption("Invasion de los cacharros")
icono = pygame.image.load("imgs/icono.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("imgs/fondo.png")

# nave espacial
img_jugador = pygame.image.load("imgs/cohete.png")
jugador_x = 368 # 800 / 2 - 64 -> 800 es el ancho de la pantalla y 64 el ancho de la imagen
jugador_y = 500 # 600 - 64 -> 600 es el alto de la pantalla y 64 el alto de la imagen
jugador_velocidad = 1

jugador_x_cambio = 0
jugador_y_cambio = 0

# enemigo dani1
img_dani1 = pygame.image.load("imgs/enemigos/dani1.png")
dani1_x = random.randint(0, 800 - 64)
dani1_y = random.randint(50, 200)
dani1_x_cambio = 0.2
dani1_y_cambio = 50

# enemigo dani1
img_dani2 = pygame.image.load("imgs/enemigos/dani2.png")
dani2_x = random.randint(0, 800 - 64)
dani2_y = random.randint(50, 200)
dani2_x_cambio = 0.2
dani2_y_cambio = 50

# enemigo jaime1
img_jaime1 = pygame.image.load("imgs/enemigos/jaime1.png")
jaime1_x = random.randint(0, 800 - 64)
jaime1_y = random.randint(50, 200)
jaime1_x_cambio = 0.2
jaime1_y_cambio = 50

# enemigo jose1
img_jose1 = pygame.image.load("imgs/enemigos/jose1.png")
jose1_x = random.randint(0, 800 - 64)
jose1_y = random.randint(50, 200)
jose1_x_cambio = 0.2
jose1_y_cambio = 50

# enemigo juanjo1
img_juanjo1 = pygame.image.load("imgs/enemigos/juanjo1.png")
juanjo1_x = random.randint(0, 800 - 64)
juanjo1_y = random.randint(50, 200)
juanjo1_x_cambio = 0.2
juanjo1_y_cambio = 50

# enemigo samu
img_samu = pygame.image.load("imgs/enemigos/samu.png")
samu_x = random.randint(0, 800 - 64)
samu_y = random.randint(50, 200)
samu_x_cambio = 0.2
samu_y_cambio = 50

# enemigo samu2
img_samu2 = pygame.image.load("imgs/enemigos/samu2.png")
samu2_x = random.randint(0, 800 - 64)
samu2_y = random.randint(50, 200)
samu2_x_cambio = 0.2
samu2_y_cambio = 50

# enemigo stefan1
img_stefan = pygame.image.load("imgs/enemigos/stefan1.png")
stefan1_x = random.randint(0, 800 - 64)
stefan1_y = random.randint(50, 200)
stefan1_x_cambio = 0.2
stefan1_y_cambio = 50

# enemigo oscar
img_oscar = pygame.image.load("imgs/enemigos/oscar.png")
oscar_x = random.randint(0, 800 - 64)
oscar_y = random.randint(50, 200)
oscar_x_cambio = 0.2
oscar_y_cambio = 50

# bala
img_bala = pygame.image.load("imgs/enemigos/bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False


# puntuacion
puntuacion = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10

# funcion mostrar puntuacion
def mostrar_puntuacion(x, y):
    puntuacion_texto = fuente.render("Puntuacion: " + str(puntuacion), True, (255, 255, 255))
    pantalla.blit(puntuacion_texto, (x, y))

# funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# funcion enemigo dani1
def enemigo_dani1(x, y):
    pantalla.blit(img_dani1, (x, y))

# funcion enemigo dani2
def enemigo_dani2(x, y):
    pantalla.blit(img_dani2, (x, y))

# funcion enemigo jaime1
def enemigo_jaime1(x, y):
    pantalla.blit(img_jaime1, (x, y))

# funcion enemigo jose1
def enemigo_jose1(x, y):
    pantalla.blit(img_jose1, (x, y))

# funcion enemigo juanjo1
def enemigo_juanjo1(x, y):
    pantalla.blit(img_juanjo1, (x, y))

# funcion enemigo samu
def enemigo_samu(x, y):
    pantalla.blit(img_samu, (x, y))

# funcion enemigo samu2
def enemigo_samu2(x, y):
    pantalla.blit(img_samu2, (x, y))

# funcion enemigo stefan1
def enemigo_stefan1(x, y):
    pantalla.blit(img_stefan, (x, y))

# funcion enemigo oscar
def enemigo_oscar(x, y):
    pantalla.blit(img_oscar, (x, y))

# funcion disparar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x, y + 10))

# funcion colision
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False

# funcion restablecer enemigo si es necesario
def restablecer_enemigo_si_es_necesario(enemigo_x, enemigo_y, enemigo_x_cambio, enemigo_y_cambio):
    if enemigo_y > 350:
        enemigo_x = random.randint(0, 800 - 64)
        enemigo_y = random.randint(50, 200)
        enemigo_y_cambio = 50  # Restablecer a la velocidad de descenso original si es necesario
    return enemigo_x, enemigo_y, enemigo_x_cambio, enemigo_y_cambio


# bucle principal
se_ejecuta = True
while se_ejecuta:

    # imagen de fondo
    pantalla.blit(fondo, (0, 0))

    # eventos
    for evento in pygame.event.get():

        # Evento cerrar ventana
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Eventos presionar teclas
        if evento.type == pygame.KEYDOWN:

            # Mover eje X
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio -= jugador_velocidad
            # Mover eje Y
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio += jugador_velocidad
            # Disparar
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparos.mp3")
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)


        # eventos soltar teclas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio += jugador_velocidad

            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio -= jugador_velocidad

    # movimiento de la nave
    jugador_x += jugador_x_cambio

    # mantener dentro de los bordes la nave
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # movimiento del enemigo dani1
    dani1_x += dani1_x_cambio

    # mantener dentro de los bordes al enemigo dani1
    if dani1_x <= 0:
        dani1_x_cambio = 0.2
        dani1_y += dani1_y_cambio
    elif dani1_x >= 736:
        dani1_x_cambio = -0.2
        dani1_y += dani1_y_cambio

    # movimiento del enemigo dani2
    dani2_x += dani2_x_cambio

    # mantener dentro de los bordes al enemigo dani2
    if dani2_x <= 0:
        dani2_x_cambio = 0.2
        dani2_y += dani2_y_cambio
    elif dani2_x >= 736:
        dani2_x_cambio = -0.2
        dani2_y += dani2_y_cambio

    # movimiento del enemigo jaime1
    jaime1_x += jaime1_x_cambio

    # mantener dentro de los bordes al enemigo jaime1
    if jaime1_x <= 0:
        jaime1_x_cambio = 0.2
        jaime1_y += jaime1_y_cambio
    elif jaime1_x >= 736:
        jaime1_x_cambio = -0.2
        jaime1_y += jaime1_y_cambio

    # movimiento del enemigo jose1
    jose1_x += jose1_x_cambio

    # mantener dentro de los bordes al enemigo jose1
    if jose1_x <= 0:
        jose1_x_cambio = 0.2
        jose1_y += jose1_y_cambio
    elif jose1_x >= 736:
        jose1_x_cambio = -0.2
        jose1_y += jose1_y_cambio

    # movimiento del enemigo juanjo1
    juanjo1_x += juanjo1_x_cambio

    # mantener dentro de los bordes al enemigo juanjo1
    if juanjo1_x <= 0:
        juanjo1_x_cambio = 0.2
        juanjo1_y += juanjo1_y_cambio
    elif juanjo1_x >= 736:
        juanjo1_x_cambio = -0.2
        juanjo1_y += juanjo1_y_cambio

    # movimiento del enemigo samu
    samu_x += samu_x_cambio

    # mantener dentro de los bordes al enemigo samu
    if samu_x <= 0:
        samu_x_cambio = 0.2
        samu_y += samu_y_cambio
    elif samu_x >= 736:
        samu_x_cambio = -0.2
        samu_y += samu_y_cambio

    # movimiento del enemigo samu2
    samu2_x += samu2_x_cambio

    # mantener dentro de los bordes al enemigo samu2
    if samu2_x <= 0:
        samu2_x_cambio = 0.2
        samu2_y += samu2_y_cambio
    elif samu2_x >= 736:
        samu2_x_cambio = -0.2
        samu2_y += samu2_y_cambio

    # movimiento del enemigo stefan1
    stefan1_x += stefan1_x_cambio

    # mantener dentro de los bordes al enemigo stefan1
    if stefan1_x <= 0:
        stefan1_x_cambio = 0.2
        stefan1_y += stefan1_y_cambio
    elif stefan1_x >= 736:
        stefan1_x_cambio = -0.2
        stefan1_y += stefan1_y_cambio

    # movimiento del enemigo oscar
    oscar_x += oscar_x_cambio

    # mantener dentro de los bordes al enemigo oscar
    if oscar_x <= 0:
        oscar_x_cambio = 0.2
        oscar_y += oscar_y_cambio
    elif oscar_x >= 736:
        oscar_x_cambio = -0.2
        oscar_y += oscar_y_cambio

    # movimiento de la bala
    if bala_y <= 0:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # colisiones enemigos
    colision_dani1 = hay_colision(dani1_x, dani1_y, bala_x, bala_y)
    colision_dani2 = hay_colision(dani2_x, dani2_y, bala_x, bala_y)
    colision_jaime1 = hay_colision(jaime1_x, jaime1_y, bala_x, bala_y)
    colision_jose1 = hay_colision(jose1_x, jose1_y, bala_x, bala_y)
    colision_juanjo1 = hay_colision(juanjo1_x, juanjo1_y, bala_x, bala_y)
    colision_samu = hay_colision(samu_x, samu_y, bala_x, bala_y)
    colision_samu2 = hay_colision(samu2_x, samu2_y, bala_x, bala_y)
    colision_stefan1 = hay_colision(stefan1_x, stefan1_y, bala_x, bala_y)
    colision_oscar = hay_colision(oscar_x, oscar_y, bala_x, bala_y)


    if colision_dani1:
        sonido_colision = mixer.Sound("acertar.mp3")
        sonido_colision.play()
        bala_y = 500
        bala_visible = False
        puntuacion += 1
        dani1_x = random.randint(0, 800 - 64)
        dani1_y = random.randint(50, 200)

    if colision_dani2:
        sonido_colision = mixer.Sound("acertar.mp3")
        sonido_colision.play()
        bala_y = 500
        bala_visible = False
        puntuacion += 1
        dani2_x = random.randint(0, 800 - 64)
        dani2_y = random.randint(50, 200)

    if colision_jaime1:
        sonido_colision = mixer.Sound("acertar.mp3")
        sonido_colision.play()
        bala_y = 500
        bala_visible = False
        puntuacion += 1
        jaime1_x = random.randint(0, 800 - 64)
        jaime1_y = random.randint(50, 200)

    if colision_jose1:
        sonido_colision = mixer.Sound("acertar.mp3")
        sonido_colision.play()
        bala_y = 500
        bala_visible = False
        puntuacion += 1
        jose1_x = random.randint(0, 800 - 64)
        jose1_y = random.randint(50, 200)

    if colision_juanjo1:
        sonido_colision = mixer.Sound("acertar.mp3")
        sonido_colision.play()
        bala_y = 500
        bala_visible = False
        puntuacion += 1
        juanjo1_x = random.randint(0, 800 - 64)
        juanjo1_y = random.randint(50, 200)

    if colision_samu:
        sonido_colision = mixer.Sound("acertar.mp3")
        sonido_colision.play()
        bala_y = 500
        bala_visible = False
        puntuacion += 1
        samu_x = random.randint(0, 800 - 64)
        samu_y = random.randint(50, 200)

    if colision_samu2:
        sonido_colision = mixer.Sound("acertar.mp3")
        sonido_colision.play()
        bala_y = 500
        bala_visible = False
        puntuacion += 1
        print(puntuacion)
        samu2_x = random.randint(0, 800 - 64)
        samu2_y = random.randint(50, 200)

    if colision_stefan1:
        sonido_colision = mixer.Sound("acertar.mp3")
        sonido_colision.play()
        bala_y = 500
        bala_visible = False
        puntuacion += 1
        stefan1_x = random.randint(0, 800 - 64)
        stefan1_y = random.randint(50, 200)

    if colision_oscar:
        sonido_colision = mixer.Sound("acertar.mp3")
        sonido_colision.play()
        bala_y = 500
        bala_visible = False
        puntuacion += 1
        oscar_x = random.randint(0, 800 - 64)
        oscar_y = random.randint(50, 200)

    # restablecer enemigo si es necesario
    dani1_x, dani1_y, dani1_x_cambio, dani1_y_cambio = restablecer_enemigo_si_es_necesario(dani1_x, dani1_y, dani1_x_cambio, dani1_y_cambio)
    dani2_x, dani2_y, dani2_x_cambio, dani2_y_cambio = restablecer_enemigo_si_es_necesario(dani2_x, dani2_y, dani2_x_cambio, dani2_y_cambio)
    jaime1_x, jaime1_y, jaime1_x_cambio, jaime1_y_cambio = restablecer_enemigo_si_es_necesario(jaime1_x, jaime1_y, jaime1_x_cambio, jaime1_y_cambio)
    jose1_x, jose1_y, jose1_x_cambio, jose1_y_cambio = restablecer_enemigo_si_es_necesario(jose1_x, jose1_y, jose1_x_cambio, jose1_y_cambio)
    juanjo1_x, juanjo1_y, juanjo1_x_cambio, juanjo1_y_cambio = restablecer_enemigo_si_es_necesario(juanjo1_x, juanjo1_y, juanjo1_x_cambio, juanjo1_y_cambio)
    samu_x, samu_y, samu_x_cambio, samu_y_cambio = restablecer_enemigo_si_es_necesario(samu_x, samu_y, samu_x_cambio, samu_y_cambio)
    samu2_x, samu2_y, samu2_x_cambio, samu2_y_cambio = restablecer_enemigo_si_es_necesario(samu2_x, samu2_y, samu2_x_cambio, samu2_y_cambio)
    stefan1_x, stefan1_y, stefan1_x_cambio, stefan1_y_cambio = restablecer_enemigo_si_es_necesario(stefan1_x, stefan1_y, stefan1_x_cambio, stefan1_y_cambio)
    oscar_x, oscar_y, oscar_x_cambio, oscar_y_cambio = restablecer_enemigo_si_es_necesario(oscar_x, oscar_y, oscar_x_cambio, oscar_y_cambio)

    jugador(jugador_x, jugador_y)

    enemigo_dani1(dani1_x, dani1_y)
    enemigo_jaime1(jaime1_x, jaime1_y)
    enemigo_jose1(jose1_x, jose1_y)
    enemigo_juanjo1(juanjo1_x, juanjo1_y)
    enemigo_samu2(samu2_x, samu2_y)
    enemigo_stefan1(stefan1_x, stefan1_y)
    enemigo_oscar(oscar_x, oscar_y)

    # mostrar puntuacion
    mostrar_puntuacion(texto_x, texto_y)

    # actualizar pantalla
    pygame.display.update()