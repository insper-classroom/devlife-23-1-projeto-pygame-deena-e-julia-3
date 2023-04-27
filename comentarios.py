 # para fazer a colisao, vamos utilizar o mask. O mask quebra a imagem do passaro, a qual eh um retangulo, em varios mini-retangulos, tipo pixels, e verificar se existe a presenca do passaro e da torre ao mesmo tempo, indicando a colisao.
        # mask is a perfect collision detection
        # Voce pega a mascara da bola e a mascara da torra e avalia. Se eles tem pixel em comum, significa que colidiu. Caso contrario, nao colidiu 


# sempre que voce quiser desenhar um objeto rotacionado dentro da tela, voce faz esse processo aqui:    
    # se ele nao tiver todo virado pra cima, ele vai ficar todo virado pra cima, aka rotacao maxima
    # self.altura = e a altura do pomo desde a ultima vez que ele pulou


# a torre nao tem aceleracao porque ela so vai se movimentar na horizontal. Nao sera como uma parabula. Qualquer obejto que voce queira que tenha movimentacao como uma parabula, ele tera a forca da gravidade interferindo na velocidade do eixo y.

# para ter a torre em cima e embaixo, pasta flipar a imagem. if segundo argument for True, voce vai flipa-la na horizontal. If true o third argument, voce o flipa na vertical.



# import classe
# import funcoes  
# import pygame 
# window = pygame.display.set_mode((350,420))
# funcoes.game_loop(window)                               
