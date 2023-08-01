#pacotes

import pygame
import random
import os
from os import path

pygame.init()
pygame.mixer.init()


LARGURA = 480
ALTURA = 600
FPS = 60

TELA = pygame.display.set_mode((LARGURA, ALTURA))



def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'inicio.png')).convert()
    background_rect = background.get_rect()
