from classe import*
import pygame
import os 
def inicializa():
    pygame.init()

    window = pygame.display.set_mode((350, 420))
    pygame.display.set_caption("GoldenFly")

    # imagem_fundo = pygame.image.load(os.path.join('fotos','imagem fundo remasterizada.png'))
    # imagem_pomoouro = pygame.image.load(os.path.join('fotos','pixelado pomo de ouro.png'))
    # imagem_casas = pygame.image.load(os.path.join('fotos','casas.png'))
    # imagem_torre = pygame.image.load(os.path.join('fotos', 'torres_arrumadas.png'))
    # imagem_tela_inicial = pygame.image.load(os.path.join('fotos','imagem_inicial.jpg' ))
    # imagem_tela_inicial_nova = pygame.transform.scale(imagem_tela_inicial, (350, 420))

    pomo= Pomo_de_ouro_classico(175,210)
    torres= [Torre(350)]


    assets={
        # 'imagem_fundo':imagem_fundo,
        # 'pomo_de_ouro':imagem_pomoouro,
        # 'brazão':imagem_casas,
        # 'torre': imagem_torre,
        # 'tela_inicial': imagem_tela_inicial_nova
    }
    return window,assets, pomo, torres

def atualiza_estado(torres, pomo):
    pygame.time.Clock().tick(30)
    game=True
    pomo.movimento()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game =False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pomo.velocidade_y = -300
        
    return game

def desenha(window,assets,pomo,torres):
    window.fill((255,255, 255))
    window.blit(assets['imagem_fundo'],(0,0))
    pomo.desenha(window)
    for torre in torres:
        torre.desenha(window)
        torre.estado()

    for torre in torres:
        if (torre.x <= -50):
            torres.append(Torre(350))
            torres.remove(torre)
        

    pygame.display.update()
    return window, assets,pomo, torres

def game_loop(window,assets,pomo,torre):
    telas = [Tela_inicio(), OutraTela()]
    tela = telas[0]
    game = True
    while game:
        indice_proxima_tela = tela.atualiza_estado()
        if indice_proxima_tela == -1:
            game = False
        else:
            tela = telas[indice_proxima_tela]
            tela.desenha(window)
            pygame.display.update()
            pygame.time.Clock().tick(30)
    # while atualiza_estado(torre, pomo):
    #     desenha(window,assets,pomo,torre)