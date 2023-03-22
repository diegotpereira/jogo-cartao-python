def encontar_troco(valor):
    moedas = [1, 5, 10, 25, 50]

    i = len(moedas) - 1

    while valor > 0 and i >= 0:

        if moedas[i] <= valor:
            print(f"Usando moeda de {moedas[i]} centavos")
            valor -= moedas[i]

        else:
            i -= 1

troco = 57
encontar_troco(troco)