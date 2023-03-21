import pygame;

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões de largura e altura da janela
largura_tela = 800
altura_tela = 600

# Criando a janela
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Definindo a cor de fundo
cor_de_fundo = (255, 255, 255)


# Definindo o título da janela
pygame.display.set_caption("Meu Jogo")

# Loop principal do jogo
while True:

    # Verificando se o jogador fechou a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Preenchendo o fundo com a cor definida
    tela.fill(cor_de_fundo)

    # Desenhando um retângulo vermelho na tela
    pygame.draw.rect(tela, (255, 0, 0), (100, 100, 50, 50))

    # Atualizando a tela
    pygame.display.update()