import os
import pygame 
import random
# import funcoes 

imagem_pomoouro = pygame.image.load(os.path.join('fotos','pixelado pomo de ouro.png'))
imagem_torre = pygame.image.load(os.path.join('fotos','torres_arrumadas.png'))
imagem_torre_nova=pygame.transform.scale(imagem_torre,(50,400))
imagem_fundo = pygame.image.load(os.path.join('fotos','imagem fundo remasterizada.png'))

state = {
    't0': 0,    
    't':0
}

        
class Pomo():

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
        self.gravidade = 500
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
        if self.posição_y < self.imagem.get_height() / 2:
            self.posição_y = self.imagem.get_height() / 2
            self.velocidade_y = -self.velocidade_y
        if self.posição_y + self.imagem.get_height() / 2 > 420:
            self.posição_y = 420 - self.imagem.get_height() / 2
            self.velocidade_y = 0
        self.rect.y=self.posição_y
    

    def desenha(self, window):
    
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        centro_imagem = self.imagem.get_rect()  
        retangulo = imagem_rotacionada.get_rect()
        window.blit(imagem_rotacionada, (self.posição_x,self.posição_y))

       
        pygame.mask.from_surface(self.imagem)
        
    
class Torre:

    distancia_entre_torres= 140
    velocidade= 200

    def __init__(self, posicao_x):
        self.x=posicao_x
        self.altura=0
        self.parte_de_cima=0
        self.parte_de_baixo=0#
        self.torre_cima= imagem_torre_nova
        self.torre_baixo= imagem_torre_nova
        self.distancia_entre_torres=140
        self.velocidade=300
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

    def colidir(self):
        return self.rect1.colliderect(self.rect2) or self.rect2.colliderect(self.rect1)
    
class Tela_Game_Over:
    pass

class Tela_jogo:

    def __init__(self):
        self.pomo = Pomo(175,210)
        self.torre = Torre(350)
        self.imagem_fundo = pygame.image.load(os.path.join('fotos','imagem fundo remasterizada.png'))
        fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(fonte_padrao, 16)
        self.ponto = 0
        self.maior_pontuação = 0
        
    def desenha(self, window):
        # funcoes.desenha(window,self.imagem_fundo,self.pomo,self.torres)
        window.blit(self.imagem_fundo,(0,0))
        self.pomo.desenha(window)
        self.torre.desenha(window)
        self.texto = self.fonte.render(self.ponto, True,(255,255,255))

        for torre in self.torre:
            torre.desenha(window)
            torre.atualiza_estado()
        if torre.x < -50:
            self.ponto+=1
            if self.ponto> self.maior_pontuação:
                self.maior_pontuação= self.ponto
        for torre in self.torre:
            if (torre.x <= -50):
                self.torre.append(Tela_jogo.Torre(350))
                self.torre.remove(torre)
        window.blit(self.texto, (167,30))

    def atualiza_estado(self):
        self.pomo.atualiza_estado()
        self.torre.atualiza_estado()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
                if self.torre.colidir():
                    return 3
        return 2


class Tela_Instrucao:
    def __init__(self):
        self.imagem_fundo = pygame.image.load(os.path.join('fotos','imagem fundo remasterizada.png'))
        self.pomo = Pomo(175,210)
        self.fonte = pygame.font.Font('fonte/Mario-Kart-DS.ttf',20)
        self.caixa_x_1 = 39
        self.caixa_y_1 = 100
        self.caixa_width_1 = 260
        self.caixa_height_1 = 38
        # self.caixa_x_2 = 
        # self.caixa_y_2 =
        # self.caixa_width_2 =
        # self.caixa_height_2 =

    def desenha(self, window):
        window.blit(self.imagem_fundo, (0,0))
        self.pomo.desenha(window)
        self.texto_instrucoes1 = self.fonte.render('PARA INICIAR O JOGO', True, (0,0,0))
        self.texto_instrucoes2 = self.fonte.render('CLIQUE NA TECLA ENTER', True, (0,0,0))
        caixa_texto_1 = pygame.Rect(self.caixa_x_1, self.caixa_y_1, self.caixa_width_1, self.caixa_height_1)
        pygame.draw.rect(window, (255,255,255), caixa_texto_1)
        window.blit(self.texto_instrucoes1, (40,100))
        window.blit(self.texto_instrucoes2, (40, 120))

    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
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
        texto_jogar = self.fonte.render('JOGAR', True, (0,0,0))
        texto_nome= self.titulo.render('GOLDENFLY', True, (0,0,0))
        caixa_titulo = pygame.Rect(self.caixa_x_titulo, self.caixa_y_titulo, self.caixa_width_titulo, self.caixa_height_titulo )
        pygame.draw.rect(window,(255,255,255), caixa_titulo )
        window.blit(texto_nome,(52,40))
        window.blit(texto_jogar, (130,326))
    
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
    

        