import pygame
def inicializa():
    pygame.init()
    window=pygame.display.set_mode((320, 240))
    pygame.display.set_caption("Goldenfly")
    return window

def recebe_eventos():
    game=True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
    return game

def desenha(janela):
    janela.fill((255, 0, 0))
    pygame.display.update()
    return janela

def game_loop(window):
    while True:
        if recebe_eventos()==False:
            break
        else:
            desenha(window)