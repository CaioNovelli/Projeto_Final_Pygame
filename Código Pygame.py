import pygame
import assets

# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((650, 650))
pygame.display.set_caption('BEM VINDO AO JOGO DA MEMÓRIA!')

# ----- Inicia estruturas de dados
jogando = True
dicionario = assets.load_assets()


# ===== Loop principal =====
while jogando:

    window.fill((0, 0, 0))  # Preenche com a cor preta
    window.blit(dicionario['tela inicial'], (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_KP_ENTER:
                jogando = True

    # ----- Gera saídas
    
    

    

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador


# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
