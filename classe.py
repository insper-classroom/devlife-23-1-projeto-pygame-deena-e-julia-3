import os
import pygame 
import random

imagem_pomoouro = pygame.image.load(os.path.join('fotos','pixelado pomo de ouro.png'))
imagem_torre = pygame.image.load(os.path.join('fotos','torres_arrumadas.png'))
imagem_torre_nova=pygame.transform.scale(imagem_torre,(50,400))



state = {
    't0': 0,    
    't':0
}

class Pomo_de_ouro_classico:

    def __init__(self,posição_x,posição_y):
        self.posição_x = posição_x#posição do pomo x
        self.posição_y = posição_y#altura do pomo 
        self.velocidade_y = 0#a velocidade que ele se encontra 
        self.angulo = 0# o angulo dele para sabermos o angulo que ele ira voar
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


    def movimento(self):

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
        centro_imagem = self.imagem.get_rect()  # perguntar ao miranda a estrutura desse codigo
        retangulo = imagem_rotacionada.get_rect()
        # eu uso o topleft para desenhar o retangulo, eu uso o centro para rotacionar o retangulo
        window.blit(imagem_rotacionada, (self.posição_x,self.posição_y))

        # para fazer a colisao, vamos utilizar o mask. O mask quebra a imagem do passaro, a qual eh um retangulo, em varios mini-retangulos, tipo pixels, e verificar se existe a presenca do passaro e da torre ao mesmo tempo, indicando a colisao.
        # mask is a perfect collision detection
        # Voce pega a mascara da bola e a mascara da torra e avalia. Se eles tem pixel em comum, significa que colidiu. Caso contrario, nao colidiu 
        pygame.mask.from_surface(self.imagem)
            
        # sempre que voce quiser desenhar um objeto rotacionado dentro da tela, voce faz esse processo aqui:    
        # se ele nao tiver todo virado pra cima, ele vai ficar todo virado pra cima, aka rotacao maxima
        # self.altura = e a altura do pomo desde a ultima vez que ele pulou


    # a torre nao tem aceleracao porque ela so vai se movimentar na horizontal. Nao sera como uma parabula. Qualquer obejto que voce queira que tenha movimentacao como uma parabula, ele tera a forca da gravidade interferindo na velocidade do eixo y.
   
    # para ter a torre em cima e embaixo, pasta flipar a imagem. if segundo argument for True, voce vai flipa-la na horizontal. If true o third argument, voce o flipa na vertical.
class Torre:

    distancia_entre_torres=140
    velocidade=200


    def __init__(self, posicao_x):
        self.x=posicao_x
        self.altura=0
        self.parte_de_cima=0#da torre
        self.parte_de_baixo=0#da torre
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
        self.altura=random.randint(50 ,260)
        self.parte_de_cima= self.altura - self.torre_cima.get_height()
        self.parte_de_baixo= self.altura + self.distancia_entre_torres
        self.rect1.y = self.parte_de_cima
        self.rect2.y = self.parte_de_baixo

    def estado(self):
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
    
class Torre_movimento:
    pass

class OutraTela:
    def __init__(self):
        self.cor = (255, 0, 0)
    
    def desenha(self, window):
        window.fill(self.cor)

    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

        return 1

class Tela_inicio:
    def __init__(self):

        imagem_tela_inicial = pygame.image.load(os.path.join('fotos','imagem_inicial.jpg' ))
        self.imagem_tela_inicial_nova = pygame.transform.scale(imagem_tela_inicial, (350, 420))
        fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(fonte_padrao, 30)

    def desenha(self, window):

        window.blit(self.imagem_tela_inicial_nova, (0, 0))
        self.caixa_x = 124
        self.caixa_y = 280
        self.caixa_width = 100
        self.caixa_height = 33
        caixa_texto = pygame.Rect(self.caixa_x , self.caixa_y , self.caixa_width, self.caixa_height)
        pygame.draw.rect(window, (255,255,255), caixa_texto)
        texto_jogar = self.fonte.render('Jogar', True, (0,0,0))
        window.blit(texto_jogar, (131,282))
    
    

    def colisao_coordenada_rect(self, coordenada_x, coordenada_y):
        self.pos_x = coordenada_x
        self.pos_y = coordenada_y
        if self.caixa_x <= self.pos_x and self.pos_x <= self.caixa_x + self.caixa_width and self.caixa_y <= self.pos_y and self.pos_y <= self.caixa_y + self.caixa_height:
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
    

        