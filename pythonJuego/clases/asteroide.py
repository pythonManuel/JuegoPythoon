import pygame


class Asteroide(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenAsteroide = pygame.image.load("/home/sigfrido/python/imagenes/asteroide.png")
        self.rect = self.imagenAsteroide.get_rect()
        self.velocidad = 10
        self.rect.top = posY
        self.rect.left = posX
        self.listaAsteroide = []
    def recorrido(self):
        self.rect.top = self.rect.top + self.velocidad
    def dibujar(self, superficie):
        superficie.blit(self.imagenAsteroide, self.rect)