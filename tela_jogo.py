import pygame
import os
import classe

class Tela_jogo:
    def __init__(self, Pomo_de_ouro_classico, Torre):
        pygame.init()

        self.largura_window = 350
        self.altura_window = 420
        self.window = pygame.display.set_mode((self.largura_window, self.altura_window))

        pygame.display.set_caption("GoldenFly")

        self.imagem_fundo = pygame.image.load(os.path.join('fotos','imagem fundo remasterizada.png'))
        self.imagem_pomoouro = pygame.image.load(os.path.join('fotos','pixelado pomo de ouro.png'))
        self.imagem_casas = pygame.image.load(os.path.join('fotos','casas.png'))
        self.imagem_torre = pygame.image.load(os.path.join('fotos', 'torres_arrumadas.png'))
        
        self.pomo= Pomo_de_ouro_classico(175,210)
        self.torres= [Torre(350)]


    def atualiza_estado(self):
        pygame.time.Clock().tick(30)

        while True:
            self.pomo.movimento()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE:

