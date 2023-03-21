import pygame;

pygame.init()

largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))

cor_de_fundo = (255, 255, 255)

pygame.display.set_caption("Meu Jogo")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    tela.fill(cor_de_fundo)

    pygame.draw.rect(tela, (255, 0, 0), (100, 100, 50, 50))

    pygame.display.update()