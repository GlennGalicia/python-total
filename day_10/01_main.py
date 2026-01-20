import pygame as pg
from random import randint
from pygame import mixer
import math
import io
import sys
import os

# Función para obtener la ruta correcta de los archivos
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Inicializar proyecto
pg.init()

# Crear pantalla
pantalla = pg.display.set_mode((800, 600))
en_juego = True

# Cargar fondo de pantalla
fondo = pg.image.load(resource_path('img/Fondo.jpg'))

# Cargar musica
mixer.music.load(resource_path('music/MusicaFondo.mp3'))
mixer.music.set_volume(0.8)
mixer.music.play(-1)

# Titulo
pg.display.set_caption("Invasión Espacial")

# Colocar icono
icono = pg.image.load(resource_path('img/ovni.png'))
pg.display.set_icon(icono)

# Variables Jugador
img_cohete = pg.image.load(resource_path('img/cohete.png'))
position_X = 368
position_Y = 500
position_X_cambio = 0
position_Y_cambio = 0

# Variables Enemigo
img_enemigo = []
enemigo_X = []
enemigo_Y = []
enemigo_X_cambio = []
enemigo_Y_cambio = []
cantidad_enemigos = 8

for i in range(cantidad_enemigos):
    img_enemigo.append(pg.image.load(resource_path('img/enemigo.png')))
    enemigo_X.append(randint(0, 736))
    enemigo_Y.append(randint(50, 200))
    enemigo_X_cambio.append(0.5)
    enemigo_Y_cambio.append(25)

# Variables Bala
balas = []
img_bala = pg.image.load(resource_path('img/bala.png'))
bala_X = 0
bala_Y = 500
bala_X_cambio = 0
bala_Y_cambio = 3
bala_visible = False


def fuente_bytes(fuente):
    with open(fuente, 'rb') as f:
        ttf_bytes = f.read()
    return io.BytesIO(ttf_bytes)


# Detalles para Puntaje
puntaje = 0
fuente_como_bytes = fuente_bytes(resource_path('FreeSansBold.ttf'))
fuente = pg.font.Font(fuente_como_bytes, 32)
texto_x = 10
texto_y = 10

# Texto final del juego
fuente_final = pg.font.Font(resource_path('FreeSansBold.ttf'), 40)


def texto_final():
    mi_fuente_final = fuente_final.render(f'Juego Terminado', True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (100, 200))


def mostar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


def cohete(x, y):
    pantalla.blit(img_cohete, (x, y))


def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


def colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Loop del juego
while en_juego:

    pantalla.blit(fondo, (0, 0))

    for event in pg.event.get():

        # Evento cerrar Juego
        if event.type == pg.QUIT:
            en_juego = False

        # Evento presionar flechas < - >
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                position_X_cambio = -1
            if event.key == pg.K_RIGHT:
                position_X_cambio = 1
            if event.key == pg.K_SPACE:
                mixer.Sound(resource_path('music/disparo.mp3')).play()
                nueva_bala = {
                    "x": position_X,
                    "y": position_Y,
                    "velocidad": -5
                }
                balas.append(nueva_bala)

                if not bala_visible:
                    bala_X = position_X
                    disparar_bala(bala_X, bala_Y)

        # Evento soltar flechas
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                position_X_cambio = 0

    # Modificar posición del juego
    position_X += position_X_cambio

    # Mantener dentro de bordes al jugador
    if position_X < 0:
        position_X = 0
    elif position_X >= 736:
        position_X = 736

    # Modificar posición del enemigo
    for e in range(cantidad_enemigos):

        # Fin del juego
        if enemigo_Y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_Y[k] = 1000
            texto_final()
            break

        enemigo_X[e] += enemigo_X_cambio[e]

        # Mantener dentro de bordes al enemigo
        if enemigo_X[e] <= 0:
            enemigo_X_cambio[e] = 1
            enemigo_Y[e] += enemigo_Y_cambio[e]
        elif enemigo_X[e] >= 736:
            enemigo_X_cambio[e] = -1
            enemigo_Y[e] += enemigo_Y_cambio[e]

        # Nueva Colision
        for bala in balas:
            colision_bala_enemigo = colision(enemigo_X[e], enemigo_Y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound(resource_path("music/Golpe.mp3"))
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_X[e] = randint(0, 736)
                enemigo_Y[e] = randint(20, 200)
                break

        enemigo(enemigo_X[e], enemigo_Y[e], e)

    # Movimiento bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)

    # Movimiento Bala
    if bala_Y <= -64:
        bala_Y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_X, bala_Y)
        bala_Y -= bala_Y_cambio

    # Mostrar puntaje
    mostar_puntaje(texto_x, texto_y)

    # Actualizar pantalla
    cohete(position_X, position_Y)

    pg.display.flip()