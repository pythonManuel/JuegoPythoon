import pygame, sys
from pygame.locals import *
from clases import asteroide, jugador
from random import randint
from time import  time 
#variable
ANCHO = 480
ALTO = 700
listaAsteroide = []
jugando = True

def cargarAsteroide(x,y):
    meteoro = asteroide.Asteroide(x,y)
    listaAsteroide.append(meteoro)

#funcion principal

def meteorito():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    #imagen de fondo
    fondo = pygame.image.load("/home/sigfrido/python/imagenes/fondo.png")
   

    pygame.display.set_caption("Meteoritos")

    nave = jugador.Nave()
    contador = 0
    while True:
        ventana.blit(fondo,(0,0))
        nave.dibujar(ventana)
        #tiempo
        tiempo = time()
        if tiempo - contador > 1:
            contador = tiempo
            posX = randint(2, 478)
            cargarAsteroide(posX, 0)

            #comprobar lista asteroide
        if len(listaAsteroide) > 0:
            for x in listaAsteroide:
                x.dibujar(ventana)
                x.recorrido()
                if x.rect.top > 700:
                    listaAsteroide.remove(x)
        if len(nave.listaDisparo)>0:
            for x in nave.listaDisparo:
                x.dibujar(ventana)
                x.recorrido()
                if x.rect.top<-10:
                    nave.listaDisparo.remove(x)
        nave.mover()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    nave.rect.left-=nave.velocidad
                elif evento.key == K_RIGHT:
                    nave.rect.right+=nave.velocidad
                elif evento.key == K_SPACE:
                    x,y= nave.rect.center
                    nave.disparar(x,y)

        pygame.display.update()

meteorito()
