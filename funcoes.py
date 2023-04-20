from classe import*
import pygame
import os 
def inicializa():
    pygame.init()
    window=pygame.display.set_mode((350, 420))
    pygame.display.set_caption("Goldenfly")
    imagem_fundo=pygame.image.load(os.path.join('fotos','imagem fundo remasterizada.png'))
    imagem_pomoouro=pygame.image.load(os.path.join('fotos','pixilart-drawing.png'))
    imagem_casas=pygame.image.load(os.path.join('fotos','casas.png'))
    assets={
        'imagem_fundo':imagem_fundo,
        'pomo_de_ouro':imagem_pomoouro,
        'brazão':imagem_casas,
    }
    return window,assets

def recebe_eventos():
    game=True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
    return game

def desenha(janela,assets):
    janela.fill((255,255, 255))
    janela.blit(assets['imagem_fundo'],(0,0))
    pygame.display.update()
    return janela

def game_loop(window,assets):
    while True:
        if recebe_eventos()==False:
            break
        else:
            desenha(window,assets)