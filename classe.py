import os
import pygame 
import random

imagem_pomoouro = pygame.image.load(os.path.join('fotos','pixelado pomo de ouro.png'))
imagem_torre = pygame.image.load(os.path.join('fotos','torres_arrumadas.png'))
#para conseguirmos fazer essa classe usamos como base o video https://www.youtube.com/watch?v=gomDSZaay3E e https://www.youtube.com/watch?v=WSPstecsF90.
class Pomo_de_ouro_classico:

    def __init__(self,posição_x,posição_y):
        self.posição_x = posição_x#posição do pomo x
        self.posição_y = posição_y#altura do pomo 
        self.velocidade = 0#a velocidade que ele se encontra 
        self.angulo = 0# o angulo dele para sabermos o angulo que ele ira voar
        self.altura = self.posição_y
        self.tempo = 0
        self.imagem = imagem_pomoouro
        self.rotacao_maxima = 25
        self.velocidade_rotacao = 20
        self.angulo = 0

    def voar(self): # o pomo so desloca no eixo y, ou vai para cim ou para baixo
        self.velocidade=-10#quando ele voar a velocidade precisa estar negativa para que ele não caia e sim cima
        self.tempo=0# tempo inicial do deslocamento
        self.altura= self.posição_y# a altura atual do pomo de ouro

    def movimento(self):
        # o angulo e respectivo a posicao que a poma vai cair
        self.tempo += 1
        deslocamento = self.tempo * self.velocidade + 2 * (self.tempo**2)/2#formula para descobrir o estado do pomo ultizando o s=so+v.t+a.t**2/2
        # if estado < 20:
        #limitando o tamanho do deslocamento pra 20 pixel de altura 
        #o passaro não muda de posição x ja que o movimento do passaro deve ser de cima para baixo logo quando isso acontesse a unica unidade modificada é o y. Assim, temos que pegar o ponto y e somar com o deslocamento (estado) dele.

        if deslocamento>16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2
        self.posição_y+= deslocamento

        if deslocamento < 0 or self.y < (self.altura + 50):  # testar as opcoes aqui para ver se voce entendeu a forma feita
            if self.angulo < self.rotacao_maxima:
                self.angulo = self.rotacao_maxima
        else:
            if self.angulo < -90:
                self.angulo -= self.velocidade_rotacao


        def desenha(self, window):
            
            imagem_rotacionada = pygame.transform.rotate(self.image, self.angulo)
            centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center  # perguntar ao miranda a estrutura desse codigo
            retangulo = imagem_rotacionada.get_rect(center=centro_imagem)
            # eu uso o topleft para desenhar o retangulo, eu uso o centro para rotacionar o retangulo
            window.blit(imagem_rotacionada, retangulo.topleft)

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

    distancia_entre_torres=150
    velocidade=5
    def __init__(self, posicao_x):
        self.x=posicao_x
        self.altura=0
        self.parte_de_cima=0#da torre
        self.parte_de_baixo=0#da torre
        self.torre_cima= imagem_torre
        self.torre_baixo= imagem_torre
        self.definir_altura()

    def definir_altura(self):
        self.altura=random.randint(50, 370)
        self.parte_de_cima= self.altura - self.torre_cima
        self.parte_de_baixo= self.altura + self.distancia_entre_torres

    def estado(self):
        self.x+= self.velocidade

    def desenha_torre(self,window):
        window.blit (self.torre_cima, (self.x, self.parte_de_cima))
        window.blit (self.torre_baixo, (self.x, self.parte_de_baixo ))

    def colidir(self,pomo):
        pomo_mask= pomo.get_mask()
        torre_cima_mask=pygame.mask.from_surface(self.torre_cima)
        torre_baixo_mask= pygame.mask.from_surface(self.torre_baixo)        

class Torre_movimento:
    pass