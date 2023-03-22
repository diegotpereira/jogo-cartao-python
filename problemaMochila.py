



def mochila(capacidade, pesos, valores, itens):
    # Cria uma tabela para armazenar as soluções parciais
    tabela = [[0 for j in range(capacidade + 1)] for i in range(itens + 1)]

    # Preenche a tabela com as soluções ótimas para cada subproblema
    for i in range(itens + 1):
        for j in range(capacidade + 1):

            if i == 0 or j == 0:

                tabela[i][j] = 0

            elif pesos[i - 1] <= j:

                tabela[i][j] = max(valores[i - 1] + tabela[i - 1][j - pesos[i - 1]], tabela[i - 1][j])
            
            else:

                tabela[i][j] = tabela[i - 1][j]

    # Retorna o valor máximo que pode ser carregado na mochila
    return tabela[itens][capacidade]

capacidade = 50
pesos = [10, 20, 30]
valores = [60, 100, 120]

itens = len(pesos)

resultado = mochila(capacidade, pesos, valores, itens)

print("Valor máximo que pode ser transportado: " + str(resultado))