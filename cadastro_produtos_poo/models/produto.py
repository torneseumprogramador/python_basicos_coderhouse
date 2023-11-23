class Produto:
    def __init__(self, nome="", preco=0, quantidade=0):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    produtos = []

    def incluir(self):
        Produto.produtos.append(self)

    @staticmethod
    def todos():
        return Produto.produtos