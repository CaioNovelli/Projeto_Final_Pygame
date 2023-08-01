import os
from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# Dados gerais do jogo.
WIDTH = 480 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define tamanhos


# Define algumas variáveis com as cores básicas


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

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2
