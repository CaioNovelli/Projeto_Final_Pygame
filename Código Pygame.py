import pygame
import assets
import random
import time

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
lista_cores_sorteadas = []
dicio_infos={
    'vermelha':{
        'cor':(255, 0, 0),
        'pos':(100,100,200,200)
    },
    'verde':{
        'cor':(0, 255, 0),
        'pos':(350,100,200,200)
    }, 
    'azul':{
        'cor':(0, 0, 255),
        'pos':(350,350,200,200)
    },
    'amarelo':{
        'cor':(255, 255, 0),
        'pos':(100,350,200,200)

    }
}
contador_acertos = 0

lista_sorteio=[]
cor_atual=0

# ===== Loop principal =====
while jogando:

    
    window.fill((0, 0, 0))  # Preenche com a cor preta
    if estado =='sorteando':
        sorteada = random.choice(list(dicio_infos.keys()))
        print(f'vai sortear entre {list(dicio_infos.keys())}')
        lista_sorteio.append(sorteada)
        exibe_normal = True
        cor_atual=0
        estado = 'tela_preta'

    elif estado == 'tela inicial':
        window.blit(dicionario['tela inicial'], (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == 13:
                    estado = 'sorteando'
                    t_inicial= time.time()
                    
    elif estado == 'tela_preta':
        window.fill((0, 0, 0))  # Preenche com a cor preta
        for cor,info in dicio_infos.items():
            pygame.draw.rect(window,info['cor'], info['pos'])

        if cor_atual < len(lista_sorteio):
            cor = lista_sorteio[cor_atual]
            info = dicio_infos[cor]

            if exibe_normal:
                pygame.draw.rect(window,info['cor'], info['pos'])  
            else:
                pygame.draw.rect(window,(255,255,255), info['pos'])


            t_final = time.time()
            tempo_decorrido = (t_final-t_inicial)
            if tempo_decorrido >0.35:
                t_inicial = t_final
                if exibe_normal:
                    exibe_normal =False
                else:
                    cor_atual+=1
                    exibe_normal = True


        else:
            estado = 'aguardando_clique'
            num_cliques=0
            print (lista_sorteio)

    elif estado == 'aguardando_clique':
        window.fill((0, 0, 0))  # Preenche com a cor preta
        
        for cor,info in dicio_infos.items():
            pygame.draw.rect(window,info['cor'], info['pos'])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

            # Cor apertada pelo usuario
                
                if 100 <= pos[0] <= 300 and 100 <= pos[1] <= 300:
                    cor_selecionada = 'vermelha'
                    num_cliques+=1
                    print('vermelho') # cor vermelha esta funcionando
                elif 350 <= pos[0] <= 550 and 100 <= pos[1] <= 300:
                    cor_selecionada = 'verde'
                    num_cliques+=1 
                    print('verde')# cor verde esta funcionando
                elif 100 <= pos[0] <= 300 and 350 <= pos[1] <= 550:
                    cor_selecionada = 'amarelo'
                    num_cliques+=1
                    print('amarelo')# cor amarela esta funcionando
                elif 350 <= pos[0] <= 550 and 350 <= pos[1] <= 550:
                    cor_selecionada = 'azul'
                    num_cliques+=1
                    print('azul')# cor azul esta funcionando
                else:
                    continue

            

                if cor_selecionada != lista_sorteio[num_cliques-1]:
                    print('perdeu!')
                    estado = 'perdeu'
                    t_inicial_perdeu = time.time()

                if num_cliques == len(lista_sorteio):
                    estado = 'sorteando'

    
    elif estado == 'perdeu':
        window.blit(dicionario['tela final'],(0,0))
        pygame.display.flip()  # Atualiza a tela
        
        t_final_perdeu = time.time()
        tempo_decorrido_perdeu = (t_final_perdeu - t_inicial_perdeu)

        if tempo_decorrido_perdeu > 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jogando = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == 13:
                        lista_sorteio.clear()
                        estado = 'tela inicial'
                    

    pygame.display.flip()# Atualiza a tela

    # ----- Atualiza estado do jogo
    pygame.display.update() # Mostra o novo frame para o jogador
                 

# ----- Atualiza estado do jogo
pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
