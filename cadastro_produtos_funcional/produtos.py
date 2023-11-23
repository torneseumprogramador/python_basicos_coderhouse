import time
import utils

def cadastrar(produtos):
    produto_novo = {}
    nome = input('Nome do produto\n')
    produto_encontrado = False
    for produto in produtos:
        if produto["nome"] == nome:
            print(f"O produto {nome}, já foi cadastrado")
            print(produto)
            produto["quantidade"] = int(produto["quantidade"]) + int(input(f"Digite a quantidade a crescentar no {nome}\n"))
            produto_encontrado = True
            utils.limpar_tela()
            print("Produto foi atualizado com sucesso !")
            time.sleep(2)
            utils.limpar_tela()
            break

    if produto_encontrado:
        return

    produto_novo["nome"] = nome
    produto_novo["preco"] = input('Preço do produto\n')
    produto_novo["quantidade"] = input('Quantidade do produto\n')
    produtos.append(produto_novo)


    utils.limpar_tela()
    print("\033[92mProduto cadastrado com sucesso !\033[0m")
    time.sleep(2)
    utils.limpar_tela()

    return produtos

def listar(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado !")
        time.sleep(2)
        utils.limpar_tela()
    else:
        utils.imprimir_tabela(produtos)

        input("Digite enter para continuar ...")
        utils.limpar_tela()