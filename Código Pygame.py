import pygame
import assets
import random

# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((650, 650))
pygame.display.set_caption('BEM VINDO AO JOGO DA MEMÓRIA!')

# ----- Inicia estruturas de dados
jogando = True
estado = 'tela inicial'
dicionario = assets.load_assets()


# Lista cores 
cores_disponiveis = [(255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 255)]

cor_sorteada = random.choices(cores_disponiveis, k=4)

# ===== Loop principal =====
while jogando:
    window.fill((0, 0, 0))  # Preenche com a cor preta

    if estado == 'tela inicial':
        window.blit(dicionario['tela inicial'], (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
            if event.type == pygame.KEYDOWN:
                if event.key == 13:
                    estado = 'tela_preta'

    elif estado == 'tela_preta':
        window.fill((0, 0, 0))  # Preenche com a cor preta
        pygame.draw.rect(window, (255,0,0), (100,100,200,200))
        pygame.draw.rect(window, (0,255,0), (350,100,200,200))
        pygame.draw.rect(window, (255,255,0), (100,350,200,200))
        pygame.draw.rect(window, (0,0,255), (350,350,200,200))
        
        cores_possiveis = [(255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 255)]


    

    # ----- Gera saídas

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
