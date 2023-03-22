import pygame
import random

# definindo constantes
TELA_LARGURA = 800
TELA_ALTURA = 600
COR_FUNDO = (0, 0, 0)
JOGADOR_COR = (255, 255, 255)
INIMIGO_COR = (255, 0, 0)
OBSTACULO_COR = (255, 255, 0)
JOGADOR_TAMANHO = 50
INIMIGO_TAMANHO = 30
OBSTACULO_TAMANHO = 20
JOGADOR_VELOCIDADE = 5
INIMIGO_VELOCIDADE = 3
OBSTACULO_VELOCIDADE = 4
inimigos = []
obstaculos = []

# inicialzando o Pygame
pygame.init()

# configurar a tela
tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption("Jogo Nave Espacial")

# # definindo o jogador
jogador_x = TELA_LARGURA // 2
jogador_y = TELA_ALTURA - JOGADOR_TAMANHO
jogador_rect = pygame.Rect(jogador_x, jogador_y, JOGADOR_TAMANHO, JOGADOR_TAMANHO)

# iniciando o jogo
pontuacao = 0
relogio = pygame.time.Clock()
correndo = True 

while correndo: 
    # lidar com eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correndo = False

    # Movendo o jogador
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT] and jogador_x > 0:
        jogador_x -= JOGADOR_VELOCIDADE

    if teclas[pygame.K_RIGHT] and jogador_x < TELA_LARGURA - JOGADOR_TAMANHO:
        jogador_x += JOGADOR_VELOCIDADE
    jogador_rect.x = jogador_x

    # criando inimigos aleatoriamente
    if random.randint(0, 100) < 5:
        inimigo_x = random.randint(0, TELA_LARGURA - INIMIGO_TAMANHO)
        inimigo_y = 0
        inimigo_rect = pygame.Rect(inimigo_x, inimigo_y, INIMIGO_TAMANHO, INIMIGO_TAMANHO)
        inimigos.append(inimigo_rect)

    # mover inimigos

    for inimigo_rect in inimigos:
        inimigo_rect.y += INIMIGO_VELOCIDADE

        if inimigo_rect.y > TELA_ALTURA:
            inimigos.remove(inimigo_rect)

    # criar obstaculos aleatoriamente
    if random.randint(0, 100) < 10:
        obstaculo_x = random.randint(0, TELA_LARGURA - OBSTACULO_TAMANHO)
        obstaculo_y = 0
        obstaculo_rect = pygame.Rect(obstaculo_x, obstaculo_y, OBSTACULO_TAMANHO, OBSTACULO_TAMANHO)
        obstaculos.append(obstaculo_rect)

    # Mover obstáculos
    for obstaculo_rect in obstaculos:
        obstaculo_rect.y += OBSTACULO_VELOCIDADE

        if obstaculo_rect.y > TELA_LARGURA:
            obstaculos.remove(obstaculo_rect)

    # verificar colisões

    for inimigo_rect in inimigos:

        if jogador_rect.colliderect(inimigo_rect):
            correndo = False

    for obstaculo_rect in obstaculos:
        
        if jogador_rect.colliderect(obstaculo_rect):
            pontuacao += 1
            obstaculos.remove(obstaculo_rect)

    # desenha a tela
    tela.fill(COR_FUNDO)
    pygame.draw.rect(tela, JOGADOR_COR, jogador_rect)

    for inimigo_rect in inimigos:
        pygame.draw.rect(tela, INIMIGO_COR, inimigo_rect)

    for obstaculo_rect in obstaculos:
        pygame.draw.rect(tela, OBSTACULO_COR, obstaculo_rect)

    pygame.display.update()

    # atualizar relógio
    relogio.tick(60)

# encerrar pygame
pygame.quit
