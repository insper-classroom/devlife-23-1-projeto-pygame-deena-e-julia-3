import os
import pygame 
import random

imagem_pomoouro = pygame.image.load(os.path.join('fotos','pixelado pomo de ouro.png'))
imagem_torre = pygame.image.load(os.path.join('fotos','torres_arrumadas.png'))
imagem_torre_nova=pygame.transform.scale(imagem_torre,(50,300))



state = {
    't0': 0,    
    't':0
}
#para conseguirmos fazer essa classe usamos como base o video https://www.youtube.com/watch?v=gomDSZaay3E e https://www.youtube.com/watch?v=WSPstecsF90.
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

    def movimento(self):

        t0 = state['t0']
        t1 = pygame.time.get_ticks()
        calculo = (t1-t0)/1000
        state['t0'] = t1
        # o angulo e respectivo a posicao que a poma vai cair
        # self.tempo += 1
        # deslocamento = self.tempo * self.velocidade + 2 * (self.tempo**2)/2#formula para descobrir o estado do pomo ultizando o s=so+v.t+a.t**2/2
        self.velocidade_y += self.gravidade * calculo
        self.posição_y += self.velocidade_y * calculo
        # self.velocidade += self.gravidade 
        # self.posição_y += self.velocidade
        # # if estado < 20:
        #limitando o tamanho do deslocamento pra 20 pixel de altura 
        #o passaro não muda de posição x ja que o movimento do passaro deve ser de cima para baixo logo quando isso acontesse a unica unidade modificada é o y. Assim, temos que pegar o ponto y e somar com o deslocamento (estado) dele.
        if self.posição_y < self.imagem.get_height() / 2:
            self.posição_y = self.imagem.get_height() / 2
            self.velocidade_y = -self.velocidade_y
        if self.posição_y + self.imagem.get_height() / 2 > 420:
            self.posição_y = 420 - self.imagem.get_height() / 2
            self.velocidade_y = 0
        
        


    def desenha(self, window):
        
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        centro_imagem = self.imagem.get_rect()  # perguntar ao miranda a estrutura desse codigo
        retangulo = imagem_rotacionada.get_rect()
        # eu uso o topleft para desenhar o retangulo, eu uso o centro para rotacionar o retangulo
        window.blit(imagem_rotacionada, (self.posição_x - self.imagem.get_width()/2,self.posição_y  - self.imagem.get_height() / 2))

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
    def __init__(self, posicao_x):
        self.x=posicao_x
        self.altura=0
        self.parte_de_cima=0#da torre
        self.parte_de_baixo=0#da torre
        self.torre_cima= imagem_torre_nova
        self.torre_baixo= imagem_torre_nova
        self.distancia_entre_torres=140
        self.velocidade=300
        self.definir_altura()

    def definir_altura(self):
        self.altura=random.randint(50, 370)
        self.parte_de_baixo= self.altura - self.torre_cima.get_height()
        self.parte_de_cima= self.altura + self.distancia_entre_torres

    def estado(self):
        t0 = state['t']
        t1 = pygame.time.get_ticks()
        calculo = (t1-t0)/1000
        state['t'] = t1
        self.x-= self.velocidade*calculo

    def desenha(self,window):
        window.blit (self.torre_cima, (self.x, self.parte_de_cima))
        window.blit (self.torre_baixo, (self.x, self.parte_de_baixo ))

    def colidir(self,pomo):
        # pomo_mask= pomo.get_mask()
        pomo_mask = pygame.mask.from_surface(self.imagem)
        torre_cima_mask=pygame.mask.from_surface(self.torre_cima)
        torre_baixo_mask= pygame.mask.from_surface(self.torre_baixo)

        colisao1 = pygame.sprite.collidemask(pomo_mask, torre_baixo_mask)     
        colisao2 = pygame.sprite.collidemask(pomo_mask, torre_cima_mask)

        # if colisao1 != None:
        #     # vai para a tela game over
        # if colisao2 != None:
        #     # vai para a tela game over 

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

        caixa_texto = pygame.Rect(124, 280, 100, 33)
        pygame.draw.rect(window, (255,255,255), caixa_texto)
        texto_jogar = self.fonte.render('Jogar', True, (0,0,0))
        window.blit(texto_jogar, (130,282))
    
    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                return 1

        return 0
    # def colisao_com_ponto():
    
    # def 

        