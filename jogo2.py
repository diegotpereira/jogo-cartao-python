import pygame
import random

#inicializando o Pygame
pygame.init()

# definindo as dimensões de largura e altura da janela
tela_largura = 800
tela_altura = 600

# criando a janela
tela = pygame.display.set_mode((tela_largura, tela_altura))

# definindo a cor de fundo
cor_de_fundo = (255, 255, 255)

# definindo título da janela
pygame.display.set_caption("Evite os obstáculos!")

# definindo as cores dos objetos
jogador_cor = (0, 0, 255)
obstaculo_cor = (255, 0, 0)

# definindo as dimensões do jogador e da posição inicial

jogador_largura = 50
jogador_altura = 50
jogador_x = 100
jogador_y = tela_altura // 2 - jogador_altura // 2

# Definindo as dimensões do obstáculo e da posição inicial
obstaculo_largura = 50
obstaculo_altura = 200
obstaculo_x = tela_largura
obstaculo_y = random.randint(0, tela_altura - obstaculo_altura)

# definindo a velocidade do jogador e do obstáculo
jogador_velocidade = 1
obstaculo_velocidade = 1

# função para desenhar o jogador na tela
def desenhar_jogador(x, y):
    pygame.draw.rect(tela, jogador_cor, (x, y, jogador_largura, jogador_altura))

# Função para desenhar o obstáculo na tela
def desenhar_obstaculo(x, y):
    pygame.draw.rect(tela, obstaculo_cor, (x, y, obstaculo_largura, obstaculo_altura))

# Loop principal do jogo
while True:
    # verificando se o jogador fechou a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # movenddo o jogador para cima ou para baixo com as teclas de seta
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and jogador_y > 0: 
        jogador_y -= jogador_velocidade

    if teclas[pygame.K_DOWN] and jogador_y < tela_altura - jogador_altura:
        jogador_y += jogador_velocidade

    # Movendo o obstáculo para a esquerda
    obstaculo_x -= obstaculo_velocidade

    # verificando se o obstáculo atingiu o jogador
    if jogador_x + jogador_largura > obstaculo_x and jogador_x < obstaculo_x + obstaculo_largura:
        if jogador_y + jogador_altura > obstaculo_y and jogador_y < obstaculo_y + obstaculo_altura:
            pygame.quit()
            quit()

    #verificando se o obstáculo saiu da tela e reposicionado-o
    if obstaculo_x + obstaculo_largura < 0:
        obstaculo_x = tela_largura
        obstaculo_y = random.randint(0, tela_altura - obstaculo_altura)

    # preenchendo o fundo com a cor definidade
    tela.fill(cor_de_fundo)

    # desenhando o jogador e o obstáculo na tela
    desenhar_jogador(jogador_x, jogador_y)
    desenhar_obstaculo(obstaculo_x, obstaculo_y)

    # atualizando a tela
    pygame.display.update()
