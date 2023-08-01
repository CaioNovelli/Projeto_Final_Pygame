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
    # ----- Trata eventos
    for evento in pygame.event.get():
        # ----- Verifica consequências
        if evento.type == pygame.QUIT:
            jogando = False

    # ----- Gera saídas
    
    window.fill((0, 0, 0))  # Preenche com a cor preta
    window.blit(dicionario['tela inicial'], (0,0))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador


# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
