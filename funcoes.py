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
    imagem_tela_inicial = pygame.image.load(os.path.join('fotos','imagem_inicial.jpg' ))
    imagem_tela_inicial_nova = pygame.transform.scale(imagem_tela_inicial, (350, 420))

    pomo= Pomo_de_ouro_classico(175,210)
    torres= [Torre(350)]


    assets={
        'imagem_fundo':imagem_fundo,
        'pomo_de_ouro':imagem_pomoouro,
        'brazão':imagem_casas,
        'torre': imagem_torre,
        'tela_inicial': imagem_tela_inicial_nova
        }
    imagem_fundo = pygame.image.load(os.path.join('fotos','imagem fundo remasterizada.png'))
    imagem_pomoouro = pygame.image.load(os.path.join('fotos','pixelado pomo de ouro.png'))
    imagem_casas = pygame.image.load(os.path.join('fotos','casas.png'))
    imagem_torre = pygame.image.load(os.path.join('fotos', 'torres_arrumadas.png'))
    pomo=Pomo_de_ouro_classico(100,210)
    torres=[Torre(350)]
    musica_fundo = pygame.mixer.music.load('musica/musica harry potter.mp3')#para tocar a musica de fundo 
    pygame.mixer.music.play()
    fonte_padrao = pygame.font.get_default_font()
    fonte = pygame.font.Font(fonte_padrao, 16)

    assets={
        'imagem_fundo':imagem_fundo,
        'pomo_de_ouro':imagem_pomoouro,
        'brazão':imagem_casas,
        'torre': imagem_torre,
        'ponto': 0,
        'fonte_ponto': fonte,
        'maior_pontuação':0
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
    for torre in torres:
        if torre.colidir(pomo.rect):
            game= False
        
    return game

def desenha(window,assets,pomo,torres):
    window.fill((255,255, 255))
    window.blit(assets['imagem_fundo'],(0,0))
    pomo.desenha(window)
    texto = assets['fonte_ponto'].render(str(assets['ponto']), True,(255,255,255))
    
    for torre in torres:
        torre.desenha(window)
        torre.estado()
        if torre.x < -50:
            assets['ponto']+=1
            if assets['ponto']> assets['maior_pontuação']:
                assets['maior_pontuação']= assets['ponto']
    for torre in torres:
        if (torre.x <= -50):
            torres.append(Tela_jogo.Torre(350))
            torres.remove(torre)
    window.blit(texto, (167,30))
        
    

    pygame.display.update()
    return window, assets,pomo, torres

def game_loop(window,assets,pomo,torre):
    telas = [Tela_inicio(), Tela_Instrucao(Tela_jogo.Pomo_de_ouro_classico()), Tela_jogo(), Tela_Game_Over()]
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