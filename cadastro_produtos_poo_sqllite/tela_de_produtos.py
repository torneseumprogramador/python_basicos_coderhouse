import time
from models.produto import Produto
import utils

def cadastrar():
    nome = input('Nome do produto\n')
    produto_encontrado = False
    for produto in Produto.todos():
        if produto.nome == nome:
            print(f"O produto {nome}, já foi cadastrado")
            produto.quantidade = int(produto["quantidade"]) + int(input(f"Digite a quantidade a crescentar no {nome}\n"))
            produto_encontrado = True
            utils.limpar_tela()
            print("Produto foi atualizado com sucesso !")
            time.sleep(2)
            utils.limpar_tela()
            break

    if produto_encontrado:
        return

    produto = Produto()
    produto.nome = nome
    produto.preco = input('Preço do produto\n')
    produto.quantidade = input('Quantidade do produto\n')
    produto.incluir()

    utils.limpar_tela()
    print("\033[92mProduto cadastrado com sucesso !\033[0m")
    time.sleep(2)
    utils.limpar_tela()

def listar():
    if len(Produto.todos()) == 0:
        print("Nenhum produto cadastrado !")
        time.sleep(2)
        utils.limpar_tela()
    else:
        utils.imprimir_tabela(Produto.todos())

        input("Digite enter para continuar ...")
        utils.limpar_tela()