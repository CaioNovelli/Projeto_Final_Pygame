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
estado = 'tela inicial'
dicionario = assets.load_assets()

imagem1 = pygame.image.load('vermelho_img')
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
        window.blit(imagem1, (0, 0))


    

    # ----- Gera saídas

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
