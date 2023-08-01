
# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from assets import *
from game_screen.py import*

# ----- Gera tela principal
#window = pygame.display.set_mode((LARGURA, ALTURA))

def init_screen(window):

    all_buttons = pygame.sprite.Group()
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()

    play = Botao(assets, 'Play')
    all_buttons.add(play)
    # ----- Inicia estruturas de dados
    game = True

    # ----- Inicia assets
    fonte_t1 = pygame.font.SysFont("goudystout", 48)
    
    titulo1 = fonte_t1.render('BEM VINDO AO JOGO: GÊNIOS!!', True, (255, 255, 255))
    titulo2 = fonte_t1.render('GÊNIOS!!', True, (255, 255, 255))

    # ----- Gera saídas
    window.fill(PRETO)  # Preenche com a cor PRETA
    window.blit(titulo1, (52, 110))
    window.blit(titulo2, (180, 165))
    window.blit(play.image, play.rect)
    all_buttons.draw(window)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador
        
    return state

class Point:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set.mode((WIDTH,HEIGHT))
        pygame.display.set.caption(TITLE)
        self.clock = pygame.time.clock()
        self.flash_colours = [AMARELO, AZUL, VERMELHO, VERDE]
        self.colours = [AMARELO_CLARO, AZUL_CLARO, VERMELHO_CLARO, VERDE_CLARO]



        self.buttons = [Button(110, 50, DARKYELLOW),Button(330, 50, DARKBLUE),Button(110, 270, DARKRED),Button(330, 270, DARKGREEN)]


















