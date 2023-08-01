import pygame
import os
import math
#import numpy
from settings import *




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


HEIGHT = 650
FPS = 60

QUADRADO_VERMELHO_IMG = 'vermelho_img'
QUADRADO_AZUL_IMG = 'azul_img'
QUADRADO_AMARELO_IMG = 'amarelo_img'
QUADRADO_VERDE_IMG = 'verde_img'

WIDTH = 650
HEIGHT = 650



def load_assets():
    
    assets = {}
    
    # tela inicial
    assets['tela inicial'] = pygame.image.load('assets/imgs/tela_inicial.png').convert()
    assets['tela inicial'] = pygame.transform.scale(assets['tela inicial'], (WIDTH, HEIGHT))
    assets[QUADRADO_VERMELHO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'quadrado vermelho.jpg')).convert_alpha()
    assets[QUADRADO_VERMELHO_IMG] = pygame.transform.scale(assets[QUADRADO_VERMELHO_IMG], (199, 199))
    assets[QUADRADO_AZUL_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'quadrado azul.jpg')).convert_alpha()
    assets[QUADRADO_AZUL_IMG] = pygame.transform.scale(assets[QUADRADO_AZUL_IMG], (199, 199))
    assets[QUADRADO_AMARELO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'quadrado amarelo.jpg')).convert_alpha()
    assets[QUADRADO_AMARELO_IMG] = pygame.transform.scale(assets[QUADRADO_AMARELO_IMG], (199, 199))
    assets[QUADRADO_VERDE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'quadrado verde.jpg')).convert_alpha()
    assets[QUADRADO_VERDE_IMG] = pygame.transform.scale(assets[QUADRADO_VERDE_IMG], (199, 199))
    return assets



    

