from turtle import pos
import pygame
import sys
from pygame.locals import *
from random import randint
from collections import defaultdict

pygame.init()
ventana = pygame.display.set_mode((800,800))
pygame.display.set_caption("titulo Colisiones")
colorFondo = (1,150,70)
colorFigura = (255,255,255)
colorCuadro01 = (255, 255, 0)
colorCuadro02 = (0, 255, 255)
colorTextos = (255,255,255)
velocidad = 15
direccion = True
posX01, posY01 = randint(1,400), randint(1,300)
posX02, posY02 = randint(1,400), randint(1,300)
cadena = "texto de prueba"
tamaño = 20
fuente = pygame.font.SysFont("Consolas", tamaño)
texto = fuente.render(cadena, True, colorTextos)
lado = 40
while True:
    ventana.fill(colorFondo)
    ventana.blit(texto, (50,50))
    cuadro01 = pygame.draw.rect(
        ventana, colorCuadro01,(posX01, posY01, lado,lado))
    cuadro02 = pygame.draw.rect(
        ventana, colorCuadro02,(posX02, posY02, lado,lado))
    if cuadro01.colliderect(cuadro02):
        #print(f"colision!!! en cordenadas {posX01} : {posY01}")
        cadena = f"colision!!! en cordenadas {posX01} : {posY01}"
        texto = fuente.render(cadena, True, colorTextos) 
        posX02, posY02 = randint(1, 400), randint(1, 300)
        cuadro02.left=posX02-( lado /2)
        cuadro02.top=posY02-( lado /2)

#movimientos con el raton#
    posX01, posY01 = pygame.mouse.get_pos()
    posX01 = posX01 - (lado / 2)
    posY01 = posY01 - (lado / 2)
 
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
      
    pygame.display.update()