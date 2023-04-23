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
    
    assets={
        'imagem_fundo':imagem_fundo,
        'pomo_de_ouro':imagem_pomoouro,
        'brazão':imagem_casas,
        'torre': imagem_torre
    }
    return window,assets

def atualiza_estado():
    game=True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game =False
    return game

def desenha(window,assets):
    window.fill((255,255, 255))
    window.blit(assets['imagem_fundo'],(0,0))
    pygame.display.update()
    return window, assets

def game_loop(window,assets):
    while atualiza_estado():
        desenha(window,assets)
    