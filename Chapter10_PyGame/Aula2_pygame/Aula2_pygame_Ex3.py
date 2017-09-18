# -*- coding: cp1252 -*-
# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu
# Adaptado para projectos de MDP 2011-12

#Tendo por base o c�digo Aula1\_pygame.py e os elementos dispon�veis em aula2.zip resolva os seguintes problemas: 

#
# O invasor:
#
#1- Inicie o pygame com uma janela gr�fica 400x500.
#2- Junta imagem de fundo (sky.jpg).
#3- Desloque no topo da janela, da esquerda para a direita,
#   a imagem de um OVNI (fno.png). Impondo o branco como a
#   cor transparente. 
#4- Use a metade inferior da janela para deslocar a imagem do jogador, controlada pelo rato. Estas imagens est�o em play1.gif, play2.gif e play3.dif, devendo a imagem escolhida depender do movimento do rato. Devendo usar play1.gif quando o rato n�o est� em movimento. Reservado play2.gif e play3.gif, respectivamente, para identificar as situa��es onde o rato se desloca da direita para a esquerda e da esquerda para a direita.   
#5- O jogador dispara um c�rculo, no sentido ascendente, sempre que se usa o bot�o esquerdo do rato. Aten��o: os projecteis que n�o estejam vis�veis devem ser removidas da estrutura auxiliar. 
#6- Meta no ecr� um contador de pontos. Sempre que um proj�ctil intersecte o OVNI, deve increment�-lo. 
#7- Sempre que se dispara ou sempre que um proj�ctil intersecta o OVNI devem ser emitidos sons diferentes.   
#
 
import pygame

black = [  0,  0,  0]
white = [255,255,255]
blue =  [  0,  0,255]
green = [  0,255,  0]
red =   [255,  0,  0]

pygame.init()
  
screen=pygame.display.set_mode([400,500]) 
pygame.display.set_caption("MDP Game - OVNI -2012/13")
 
done=False
xfno=0     #inicia x do OVNI

clock = pygame.time.Clock()

background = pygame.image.load("sky.jpg").convert()
fno = pygame.image.load("fno.png").convert() #imagem do OVNI
fno.set_colorkey(white) # Define Cor que se assume como transparente

while done==False:
      
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True 
 
    screen.fill(blue)

    screen.blit(background, [0,0])

    if xfno>400: #chega ao fim da janela
        xfno=0
    else:
        xfno=xfno+15

    screen.blit(fno, [xfno,50]) #desenha OVNI

    pygame.display.flip()
    clock.tick(10)

pygame.quit ()
