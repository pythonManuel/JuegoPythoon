import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((800,1000))
pygame.display.set_caption("carga imagen y posiscion al Azar")
colorFondo = (1,150,70)
colorRectangulo = (255, 60, 40)
imagen = pygame.image.load("imagenes/pygame.png")
posX, posY = (10, 40)
while True:
    ventana.fill(colorFondo)
    #ventana.blit(imagen, (100,100))
    for i in range(5):
        posX, posY = randint(1, 500), randint (1, 300)
        r, g, b = randint(0, 255), randint (0, 255), randint (0, 255)
        colorRectangulo = (r,g,b)
        pygame.draw.rect(ventana, colorRectangulo, (posX, posY, 50, 80))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()