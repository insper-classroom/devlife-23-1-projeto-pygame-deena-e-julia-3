import os
import pygame 
import random

imagem_pomoouro = pygame.image.load(os.path.join('fotos','pixelado pomo de ouro.png'))
imagem_torre = pygame.image.load(os.path.join('fotos','torres_arrumadas.png'))
imagem_torre_nova=pygame.transform.scale(imagem_torre,(50,400))
imagem_fundo = pygame.image.load(os.path.join('fotos','imagem fundo remasterizada.png'))
# colocar o som de flappy bird
state = {
    't0': 0,    
    't':0
}

        
class Pomo:

    def __init__(self,posição_x,posição_y):
        self.posição_x = posição_x
        self.posição_y = posição_y
        self.velocidade_y = 0 
        self.angulo = 0
        self.altura = self.posição_y
        self.tempo = 0
        self.imagem = imagem_pomoouro
        self.rotacao_maxima = 25
        self.velocidade_rotacao = 20
        self.angulo = 0
        self.gravidade = 0
        self.rect = self.imagem.get_rect()
        self.rect.x = self.posição_x
        self.rect.y = self.posição_y

    def atualiza_estado(self):

        t0 = state['t0']
        t1 = pygame.time.get_ticks()
        calculo = (t1-t0)/1000
        state['t0'] = t1
        self.velocidade_y += self.gravidade * calculo
        self.posição_y += self.velocidade_y * calculo
        if self.posição_y < self.imagem.get_height():
            self.posição_y = self.imagem.get_height()
            self.velocidade_y = -self.velocidade_y
        if self.posição_y + self.imagem.get_height() > 420:
            self.posição_y = 420 - self.imagem.get_height()
            self.velocidade_y = 0
        self.rect.y=self.posição_y
    

    def desenha(self, window):
    
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        window.blit(imagem_rotacionada, (self.posição_x,self.posição_y))
       
        pygame.mask.from_surface(self.imagem)
        
    
class Torre:

    distancia_entre_torres= 140
    velocidade= 150

    def __init__(self, posicao_x):
        self.x=posicao_x
        self.altura=0
        self.parte_de_cima=0
        self.parte_de_baixo=0#
        self.torre_cima= imagem_torre_nova
        self.torre_baixo= imagem_torre_nova
        self.distancia_entre_torres=140
        self.velocidade=200
        self.rect1 = self.torre_cima.get_rect()
        self.rect1.x = self.x
        self.rect1.y = self.parte_de_cima
        self.rect2 = self.torre_baixo.get_rect()
        self.rect2.x = self.x
        self.rect2.y = self.parte_de_baixo
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randint(50 ,260)
        self.parte_de_cima= self.altura - self.torre_cima.get_height()
        self.parte_de_baixo= self.altura + self.distancia_entre_torres
        self.rect1.y = self.parte_de_cima
        self.rect2.y = self.parte_de_baixo

    def atualiza_estado(self):
        t0 = state['t']
        t1 = pygame.time.get_ticks()
        tempo=pygame.time.get_ticks()/1000
        calculo = (t1-t0)/1000
        state['t'] = t1
        self.x-= self.velocidade*calculo
        self.rect1.x = self.x
        self.rect2.x = self.x
        if tempo==10:
            self.velocidade+=1000
            tempo=pygame.time.get_ticks()

    def desenha(self,window):
        window.blit (self.torre_cima, (self.x, self.parte_de_cima))
        window.blit (self.torre_baixo, (self.x, self.parte_de_baixo ))

    def colidir(self,pomo_rect):
        return self.rect1.colliderect(pomo_rect) or self.rect2.colliderect(pomo_rect)
ponto={
    'pontuação':0
}

class Tela_Game_Over:
    def __init__(self):
        self.imagem_fundo = pygame.image.load(os.path.join('fotos','imagem fundo remasterizada.png'))
        self.fonte = pygame.font.Font('fonte/Mario-Kart-DS.ttf',20)

        self.tela_jogo = Tela_jogo()
        
        self.caixa_score_x = 80
        self.caixa_score_y  = 50
        self.caixa_score_width = 93
        self.caixa_score_height = 22

    def desenha(self, window):

        window.blit(self.imagem_fundo, (0,0))

        self.caixa_score = pygame.Rect(self.caixa_score_x, self.caixa_score_y, self.caixa_score_width, self.caixa_score_height)
        pygame.draw.rect(window, (255,255,255), self.caixa_score)

        self.texto_score = self.fonte.render('SCORE', True, (0,0,0))
        self.texto_numero_score = self.fonte.render(str(ponto['pontuação']), True, (0,0,0))

        window.blit(self.texto_score, (82, 52 ))
        window.blit(self.texto_numero_score, (158, 52))


    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
        return 3



class Tela_jogo:
    def __init__(self):
        self.pomo = Pomo(120,210)
        self.torres = [Torre(350)]
        self.imagem_fundo = pygame.image.load(os.path.join('fotos','imagem fundo remasterizada.png'))
        fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(fonte_padrao, 16)
        
    def desenha(self, window):
        window.blit(self.imagem_fundo,(0,0))
        self.pomo.desenha(window)
        self.texto = self.fonte.render(str(ponto['pontuação']), True,(255,255,255))

        for torre in self.torres:
            torre.desenha(window)
            torre.atualiza_estado()
            if torre.x < -50:
                ponto['pontuação']+=1
        for torre in self.torres:
            if (torre.x <= -50):
                self.torres.append(Torre(350))
                self.torres.remove(torre)
                
        window.blit(self.texto, (167,30))


    def atualiza_estado(self):
        self.pomo.atualiza_estado()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.pomo.velocidade_y = -280
                    self.pomo.gravidade = 550
        for torre in self.torres:
            if torre.colidir(self.pomo.rect):
                return 3
        return 2


class Tela_Instrucao:
    def __init__(self):
        self.imagem_fundo = pygame.image.load(os.path.join('fotos','imagem fundo remasterizada.png'))
        self.pomo = Pomo(120,100)
        self.fonte = pygame.font.Font('fonte/Mario-Kart-DS.ttf',20)
        self.caixa_x_1 = 59
        self.caixa_y_1 = 98
        self.caixa_width_1 = 220
        self.caixa_height_1 = 42
       

    def desenha(self, window):
        window.blit(self.imagem_fundo, (0,0))
        self.pomo.desenha(window)
        window.blit(self.pomo.imagem, (120, 210))

        self.texto_instrucoes1 = self.fonte.render('TO START THE GAME', True, (0,0,0))
        self.texto_instrucoes2 = self.fonte.render('PRESS SPACE TWICE', True, (0,0,0))
        caixa_texto_1 = pygame.Rect(self.caixa_x_1, self.caixa_y_1, self.caixa_width_1, self.caixa_height_1)
        pygame.draw.rect(window, (255,255,255), caixa_texto_1)
        window.blit(self.texto_instrucoes1, (65,100))
        window.blit(self.texto_instrucoes2, (65, 120))

    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return 2
        return 1

class Tela_inicio:
    def __init__(self):

        imagem_tela_inicial = pygame.image.load(os.path.join('fotos','casas.png' ))
        self.imagem_tela_inicial_nova = pygame.transform.scale(imagem_tela_inicial, (200, 220))
        self.fonte = pygame.font.Font('fonte/Mario-Kart-DS.ttf',25)
        self.titulo= pygame.font.Font('fonte/Mario-Kart-DS.ttf',40)
        self.fundo= pygame.image.load(os.path.join('fotos','imagem fundo remasterizada.png'))
        self.pomo_imagem= pygame.image.load(os.path.join('fotos', 'pixelado pomo de ouro.png'))
        self.caixa_x_jogo = 124
        self.caixa_y_jogo = 322
        self.caixa_width_jogo = 100
        self.caixa_height_jogo = 33
        self.caixa_x_titulo = 50
        self.caixa_y_titulo = 38
        self.caixa_width_titulo = 250
        self.caixa_height_titulo = 40

    def desenha(self, window):
        window.blit(self.fundo,(0,0))
        window.blit(self.imagem_tela_inicial_nova, (75, 95))
        caixa_texto = pygame.Rect(self.caixa_x_jogo , self.caixa_y_jogo , self.caixa_width_jogo, self.caixa_height_jogo)
        pygame.draw.rect(window, (255,255,255), caixa_texto)
        texto_jogar = self.fonte.render('PLAY', True, (0,0,0))
        texto_nome= self.titulo.render('GOLDENFLY', True, (0,0,0))
        caixa_titulo = pygame.Rect(self.caixa_x_titulo, self.caixa_y_titulo, self.caixa_width_titulo, self.caixa_height_titulo )
        pygame.draw.rect(window,(255,255,255), caixa_titulo )
        window.blit(texto_nome,(52,40))
        window.blit(texto_jogar, (139,326))
    
    def colisao_coordenada_rect(self, coordenada_x, coordenada_y):
        self.pos_x = coordenada_x
        self.pos_y = coordenada_y
        if self.caixa_x_jogo <= self.pos_x and self.pos_x <= self.caixa_x_jogo + self.caixa_width_jogo and self.caixa_y_jogo <= self.pos_y and self.pos_y <= self.caixa_y_jogo + self.caixa_height_jogo:
            return True
        return False
    
    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_pos()
                if self.colisao_coordenada_rect(event.pos[0], event.pos[1]):
                    return 1
        return 0
    

        