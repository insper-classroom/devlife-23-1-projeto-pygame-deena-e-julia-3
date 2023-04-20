from funcoes import *
import pygame 
import random
class Pomo_de_ouro_classico:

    def __init__(self,posição_x,posição_y):
        self.posição_x=posição_x#posição do pomo x
        self.posição_y=posição_y#altura do pomo 
        self.velocidade= 0#a velocidade que ele se encontra 
        self.angulo=0# o angulo dele para sabermos o angulo que ele ira voar

    def voar(self):
        self.velocidade=-10#quando ele voar a velocidade precisa estar negativa para que ele não caia e sim cima
        self.tempo=0# tempo inicial do deslocamento
        self.altura= self.posição_y# a altura atual do pomo de ouro

    def movimento(self):
        self.tempo+=1
        estado= self.tempo * self.velocidade + 2 * (self.tempo**2)/2#formula para descobrir o estado do pomo ultizando o s=so+v.t+a.t**2/2
        if estado <20:
            estado=20#limitando o tamanho do deslocamento pra 20 pixel de altura 
        self.posição_y+= estado #o passaro não muda de posição x ja que o movimento do passaro deve ser de cima para baixo logo quando isso acontesse a unica unidade modificada é o y 

class Torre:
    pass