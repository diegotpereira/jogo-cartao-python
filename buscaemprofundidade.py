class Arvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None 
        self.direita = None 

class buscaEmProfundidade:
    def buscaProfunda(self, arvore):
        if arvore is None:
            return 

        print(arvore.valor, end=" ")
        self.buscaProfunda(arvore.esquerda)
        self.buscaProfunda(arvore.direita)

if __name__ == "__main__":
    root = Arvore(1)
    root.esquerda = Arvore(2)
    root.direita = Arvore(3)    
    root.esquerda.esquerda = Arvore(4)
    root.esquerda.direita = Arvore(5)

    buscaProfunda = buscaEmProfundidade()
    buscaProfunda.buscaProfunda(root)