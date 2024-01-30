#! /usr/bin/env python
import os
import random
import sys
import math
import csv
import pygame
from pygame.locals import *
from button import Button
from configuracion import *
from funcionesVACIAS import *
from extras import *

def ingresar_nombre(puntos,eleccion):
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.display.set_caption("Peguele al precio")
    screen = pygame.display.set_mode((ANCHO, ALTO))
    clock=pygame.time.Clock()
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA_MED)
    texto=""
    input_active = True
    texto_nombre=defaultFontGrande.render("Ingresa tu nombre:", 1, COLOR_TEXTO)
    screen.blit(texto_nombre, (ANCHO // 2 - texto_nombre.get_width() // 2, 20))
    while True:
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                input_active = True
                texto = ""
            elif evento.type == pygame.KEYDOWN and input_active:
                if evento.key == pygame.K_RETURN:
                    if(eleccion=="f"):
                        with open('puntosfacil.txt', 'a') as f:
                            f.write(texto+","+str(puntos))
                            f.write('\n')
                    elif(eleccion=="m"):
                        with open('puntosmedio.txt', 'a') as f:
                            f.write(texto+","+str(puntos))
                            f.write('\n')
                    elif(eleccion=="d"):
                        with open('puntosdificil.txt', 'a') as f:
                            f.write(texto+","+str(puntos))
                            f.write('\n')
                    pygame.quit()
                    pantalla_final(texto,puntos,eleccion)
                elif evento.key == pygame.K_BACKSPACE:
                    texto =  texto[:-1]
                else:
                    texto += evento.unicode
            screen.fill(0)
            text_surf = defaultFont.render(texto, True, (255, 0, 0))
            screen.blit(texto_nombre, (ANCHO // 2 - texto_nombre.get_width() // 2, 20))
            screen.blit(text_surf, text_surf.get_rect(center = screen.get_rect().center))
            pygame.display.flip()


def pantalla_final(texto,puntos,eleccion):
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.display.set_caption("Peguele al precio")
    screen = pygame.display.set_mode((ANCHO, ALTO))
    defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA_MED)
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA)
    texto_puntos=defaultFontGrande.render("Hiciste "+str(puntos)+" puntos", 1, COLOR_LETRAS)
    screen.blit(texto_puntos, (ANCHO // 2 - texto_puntos.get_width() // 2, 20))
    ranking=""
    y_pos=120
    cont=0
    pygame.draw.line(screen, (200, 200, 200),
                     (0, 100), (ANCHO, 100), 5)
    if(eleccion=="f"):
        texto_ranking = defaultFont.render("Mejores puntuaciones (facil)", 1, COLOR_TEXTO)
        with open("puntosfacil.txt") as file:
            csv_reader = csv.reader(file)
            sorted_list = sorted(csv_reader, key=lambda row: int(row[1]), reverse=True)
    elif(eleccion=="m"):
        texto_ranking = defaultFont.render("Mejores puntuaciones (medio)", 1, COLOR_TEXTO)
        with open("puntosmedio.txt") as file:
            csv_reader = csv.reader(file)
            sorted_list = sorted(csv_reader, key=lambda row: int(row[1]), reverse=True)
    elif(eleccion=="d"):
        texto_ranking = defaultFont.render("Mejores puntuaciones (dificil)", 1, COLOR_TEXTO)
        with open("puntosdificil.txt") as file:
            csv_reader = csv.reader(file)
            sorted_list = sorted(csv_reader, key=lambda row: int(row[1]), reverse=True)
    screen.blit(texto_ranking, (ANCHO // 2 - texto_ranking.get_width() // 2, 120))
    for nom, pun in sorted_list:
        cont=cont+1
        ranking=("{0} - {1}".format(nom, pun))
        listapuntos=defaultFont.render(ranking, 1, COLOR_TEXTO)
        print(ranking)
        y_pos=y_pos+ESPACIO
        screen.blit(listapuntos,(ANCHO // 2 - texto_ranking.get_width() // 2, y_pos))
        if(cont==5):
            break
    texto_menu=defaultFont.render("1 - Menu",1,COLOR_TEXTO)
    screen.blit(texto_menu, (10, 550))
    texto_salir=defaultFont.render("esc - Salir",1,COLOR_TEXTO)
    screen.blit(texto_salir, (600, 550))
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                elif evento.key == pygame.K_1:
                    pygame.quit()
                    main()
        pygame.display.flip()


def pantalla_inicio():
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.display.set_caption("Peguele al precio")
    screen = pygame.display.set_mode((ANCHO, ALTO))
    fondo = pygame.image.load("fondo.png")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    screen.blit(fondo, (0, 0))
    defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA)
    texto_titulo = defaultFontGrande.render("Péguele al precio", 1, COLOR_FONDO)
    screen.blit(texto_titulo, (ANCHO // 2 - texto_titulo.get_width() // 2, ALTO // 4))
    texto_facil = defaultFont.render("Presiona 1 para Fácil", 1, COLOR_FONDO)
    screen.blit(texto_facil, (ANCHO // 2 - texto_facil.get_width() // 2, ALTO // 2))
    texto_medio = defaultFont.render("Presiona 2 para Medio", 1, COLOR_FONDO)
    screen.blit(texto_medio, (ANCHO // 2 - texto_medio.get_width() // 2, ALTO // 2 + 50))
    texto_dificil = defaultFont.render("Presiona 3 para Difícil", 1, COLOR_FONDO)
    screen.blit(texto_dificil, (ANCHO // 2 - texto_dificil.get_width() // 2, ALTO // 2 + 100))
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return "s"
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                elif evento.key == pygame.K_1:
                    pygame.quit()
                    return "f"
                elif evento.key == pygame.K_2:
                    pygame.quit()
                    return "m"
                elif evento.key == pygame.K_3:
                    pygame.quit()
                    return "d"


        pygame.display.flip()


def main():

    acciones=[0,0]
    eleccion=""
    cantidad=0
    cont=0
    if(eleccion!="f" or eleccion!="m" or eleccion!="d"):
        eleccion=pantalla_inicio()
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.display.set_caption("Peguele al precio")
    screen = pygame.display.set_mode((ANCHO, ALTO))
    fondo2 = pygame.image.load("fondo2.png")
    fondo2 = pygame.transform.scale(fondo2, (ANCHO, ALTO))
    screen.blit(fondo2, (0, 0))
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), 20)
    pygame.mixer.init()
    acierto=pygame.mixer.Sound('acierto.mp3')
    fallo=pygame.mixer.Sound('fallo.mp3')
    tiempo=pygame.mixer.Sound('tiempo.mp3')
    fallo.set_volume(0.3)
    musicadefondo = pygame.mixer.Sound('musica2.mp3')
    musicadefondo.play(-1)
    musicadefondo.set_volume(0.06)
    # tiempo total del juego
    cont=0
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    tmax=TIEMPO_MAX
    fps = FPS_inicial

    puntos = 0  # puntos o dinero acumulado por el jugador
    producto_candidato = ""

    #Lee el archivo y devuelve una lista con los productos,
    lista_productos = lectura()  # lista de productos
    if(eleccion=="f"):
        cantidad=4
        margen=1000
    elif(eleccion=="m"):
        cantidad=6
        margen=800
    elif(eleccion=="d"):
        cantidad=7
        margen=500
    elif(eleccion=="s"):
        pygame.quit()
        return
    # Elegir un producto, [producto, calidad, precio]
    productolista = dameProducto(lista_productos, margen)
    producto=productolista[0]

    # Elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio.
    # De manera aleatoria se debera tomar el valor economico o el valor premium.
    # Agregar  '(economico)' o '(premium)' y el precio
    productos_en_pantalla = dameProductosAleatorios(productolista, lista_productos, margen,cantidad)
    print(productos_en_pantalla)

    # dibuja la pantalla la primera vez
    dibujar(screen, productos_en_pantalla, producto,
            producto_candidato, puntos, segundos)

    while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        # Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            # QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return ()

            # Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                producto_candidato += letra  # va concatenando las letras que escribe
                if e.key == K_BACKSPACE:
                    # borra la ultima
                    producto_candidato = producto_candidato[0:len(producto_candidato)-1]
                if e.key == K_RETURN:  # presionó enter
                    indice = int(producto_candidato)
                    # chequeamos si el prducto no es el producto principal. Si no lo es procesamos el producto
                    if indice < len(productos_en_pantalla):
                        acciones = procesar(producto, productos_en_pantalla[indice], margen,eleccion)
                        if(acciones[0]>0):
                            acierto.play()
                        else:
                            fallo.play()
                        puntos+=acciones[0]
                        tmax=tmax+(acciones[1])
                        producto_candidato = ""
                        # Elegir un producto
                        productolista = dameProducto(lista_productos, margen)
                        producto=productolista[0]
                        # elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio
                        productos_en_pantalla = dameProductosAleatorios(productolista, lista_productos, margen,cantidad)
                    else:
                        producto_candidato = ""



        segundos = tmax - pygame.time.get_ticks()/1000
        if(segundos<=15 and cont==0):
            tiempo.play()
            cont=cont+1

        #print(segundos)
        # Limpiar pantalla anterior
        screen.blit(fondo2, (0, 0))

        # Dibujar de nuevo todo
        dibujar(screen, productos_en_pantalla, producto,
                producto_candidato, puntos, segundos)

        pygame.display.flip()

    pygame.quit()
    ingresar_nombre(puntos,eleccion)
    while 1:
        # Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return


# Programa Principal ejecuta Main
if __name__ == "__main__":
    main()

