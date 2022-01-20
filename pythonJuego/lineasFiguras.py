import pygame
import sys
from pygame.locals import *
from pygame import Color, Rect, Surface

pygame.init()
ventana = pygame.display.set_mode((700,500))
pygame.display.set_caption("titulo de la ventana")
colorFondo = (1,150,70)
colorlineas = (255,128,0)
colorCirculo = (255, 255,0)
colorFiguras = (255,0,155)

while True:
    ventana.fill(colorFondo)
    pygame.draw.line(ventana,colorlineas, (60,90), (200,100), 40)
    pygame.draw.line(ventana, colorFondo, (80,190), (100,150), 20)
    pygame.draw.circle(ventana, colorFiguras, (400, 100), 100,30)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()