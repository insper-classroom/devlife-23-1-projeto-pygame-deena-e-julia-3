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
    torre=Torre(420)

    assets={
        'imagem_fundo':imagem_fundo,
        'pomo_de_ouro':imagem_pomoouro,
        'brazão':imagem_casas,
        'torre': imagem_torre
    }
    return window,assets, pomo, torre

def atualiza_estado(torre, pomo):
    pygame.time.Clock().tick(30)
    game=True
    torre.estado()
    pomo.movimento()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game =False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pomo.velocidade_y = -300
        
    return game

def desenha(window,assets,pomo,torre):
    window.fill((255,255, 255))
    window.blit(assets['imagem_fundo'],(0,0))
    pomo.desenha(window)
    torre.desenha(window)
    pygame.display.update()
    return window, assets,pomo, torre

def game_loop(window,assets,pomo,torre):
    while atualiza_estado(torre, pomo):
        desenha(window,assets,pomo,torre)