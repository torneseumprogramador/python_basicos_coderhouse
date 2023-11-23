import utils
import produtos

produtos = []
while(True):
    print("Selecione a opção abaixo:")
    print("1 - cadastrar produto")
    print("2 - listar produtos")
    print("3 - sair")

    opcao = int(input())
    utils.limpar_tela()

    if opcao == 1:
        produtos = produtos.cadastrar(produtos)
    elif opcao == 2:
        produtos.listar(produtos)
    elif opcao == 3:
        break

