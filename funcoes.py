from classe import*
import pygame
import os 
def inicializa():
    pygame.init()

    window = pygame.display.set_mode((350, 420))
    pygame.display.set_caption("GoldenFly")

    imagem_fundo = pygame.image.load(os.path.join('fotos','imagem fundo remasterizada.png'))
    imagem_pomoouro = pygame.image.load(os.path.join('fotos','pixelado pomo de ouro.png'))
    imagem_casas = pygame.image.load(os.path.join('fotos','casas.png'))
    imagem_torre = pygame.image.load(os.path.join('fotos', 'torres_arrumadas.png'))
    pomo=Pomo_de_ouro_classico(175,210)
    torres=[Torre(350)]


    assets={
        'imagem_fundo':imagem_fundo,
        'pomo_de_ouro':imagem_pomoouro,
        'brazão':imagem_casas,
        'torre': imagem_torre
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
    while atualiza_estado(torre, pomo):
        desenha(window,assets,pomo,torre)