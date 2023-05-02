from classe import *
import pygame
import os 
def inicializa():
    pygame.init()

    window = pygame.display.set_mode((350, 420))
    pygame.display.set_caption("GoldenFly")

    imagem_casas = pygame.image.load(os.path.join('fotos','casas.png'))
    imagem_tela_inicial = pygame.image.load(os.path.join('fotos','imagem_inicial.jpg' ))
    imagem_tela_inicial_nova = pygame.transform.scale(imagem_tela_inicial, (350, 420))

    pomo = Pomo(175,100)
    torres = [Torre(350)]
    
    musica_fundo = pygame.mixer.music.load('musica/musica harry potter.mp3')#para tocar a musica de fundo 
    pygame.mixer.music.play()
    fonte_padrao = pygame.font.get_default_font()
    fonte = pygame.font.Font(fonte_padrao, 16)

    assets={
        'brazão':imagem_casas,
        'tela_inicial': imagem_tela_inicial_nova,
        'fonte_ponto': fonte
    }
    return window,assets, pomo, torres

def atualiza_estado(torres, pomo):
    game=True
    pomo.atualiza_estado()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game =False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pomo.velocidade_y = -300
    for torre in torres:
        if torre.colidir(pomo.rect):
            game= False
        
    return game

def desenha(window,assets,pomo,torres):
    window.fill((255,255, 255))
    window.blit(assets['imagem_fundo'],(0,0))
    pomo.desenha(window)
    texto = assets['fonte_ponto'].render(str(assets['ponto']), True,(255,255,255))
    window.blit(texto, (167,30))

    pygame.display.update()
    return window, assets,pomo, torres

def game_loop(window,assets,pomo,torre):
    telas = [Tela_inicio(), Tela_Instrucao(), Tela_jogo(), Tela_Game_Over()]
    tela = telas[0]
    game = True
    while game:
        indice_proxima_tela = tela.atualiza_estado()

        if indice_proxima_tela == -1:
            game = False
        else:
            window.fill((0,0,0))
            tela = telas[indice_proxima_tela]
            tela.desenha(window)
            pygame.display.update()
            pygame.time.Clock().tick(30)