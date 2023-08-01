import pygame
import os
import math
#import numpy
from settings import *

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (40, 40, 40)
AMARELO = (155, 155, 0)
AMARELO_CLARO = (255, 255, 0)
AZUL = (0, 0, 155)
AZUL_CLARO = (0, 0, 255)
VERDE = (0, 155, 0)
VERDE_CLARO = (0, 255, 0)
VERMELHO = (155, 0, 0)
VERMELHO_CLARO = (255, 0, 0)
COR_DO_FUNDO = PRETO


pygame.mixer.init()

class Botão:
    def __init__(self, x, y, cor):
        self.x, self.y = x, y
        self.cor = cor

    def draw(self, screen):
        pygame.draw.rect(screen, self.cor, (self.x, self.y, TAMANHODOBOTAO, TAMANHODOBOTAO))

    def clicked(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + TAMANHODOBOTAO and self.y <= mouse_y <= self.y + TAMANHODOBOTAO

WIDTH = 650
HEIGHT = 650
FPS = 60
TAMANHODOBOTAO = 200
ANIMATION_SPEED = 20

def load_assets():
    
    assets = {}
    
    # tela inicial
    assets['tela inicial'] = pygame.image.load('assets/imgs/tela_inicial.png').convert()
    assets['tela inicial'] = pygame.transform.scale(assets['tela inicial'], (WIDTH, HEIGHT))

    return assets
    

