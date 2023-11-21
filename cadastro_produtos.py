
'''
faça um programa para cadastrar uma lista de produtos
onde terá
nome, preço, quantidade

menu onde vai digitar os dados a cadastrar no produto
exemplo:

Selecione a opção abaixo:
1 - cadastrar produto
2 - listar produtos
3 - sair

lista = {os produtos ...}

Nome: banana
Preço: 2.5
quantidade: 10
--------------------
Nome: banana
Preço: 2.5
quantidade: 10
'''

import time
import os
import platform
from prettytable import PrettyTable

def limpar_tela():
    # Verifica o sistema operacional
    if platform.system() == "Windows":
        os.system('cls')  # Para Windows
    else:
        os.system('clear')  # Para Linux e MacOS

def imprimir_tabela(produtos):
    tabela = PrettyTable()
    tabela.field_names = ["Nome", "Preço", "Quantidade"]

    # Adicionando linhas à tabela
    for produto in produtos:
        tabela.add_row([produto["nome"], produto["preco"], produto["quantidade"]])

    # Exibindo a tabela
    print(tabela)

    # Determina a largura máxima de cada coluna
    # max_nome = max(len(p["nome"]) for p in produtos)
    # max_preco = max(len(p["preco"]) for p in produtos)
    # max_quantidade = max(len(p["quantidade"]) for p in produtos)

    # # Cabeçalhos da tabela
    # print(f"{'Nome'.ljust(max_nome)} | {'Preço'.ljust(max_preco)} | {'Quantidade'.ljust(max_quantidade)}")
    # print("-" * (max_nome + max_preco + max_quantidade + 6))  # Ajusta o separador

    # # Imprime cada linha da tabela
    # for produto in produtos:
    #     nome = produto["nome"].ljust(max_nome)
    #     preco = produto["preco"].ljust(max_preco)
    #     quantidade = produto["quantidade"].ljust(max_quantidade)
    #     print(f"{nome} | {preco} | {quantidade}")

produtos = []
while(True):
    print("Selecione a opção abaixo:")
    print("1 - cadastrar produto")
    print("2 - listar produtos")
    print("3 - sair")

    opcao = int(input())
    limpar_tela()

    if opcao == 1:
        produto_novo = {}
        nome = input('Nome do produto\n')
        produto_encontrado = False
        for produto in produtos:
            if produto["nome"] == nome:
                print(f"O produto {nome}, já foi cadastrado")
                print(produto)
                produto["quantidade"] = int(produto["quantidade"]) + int(input(f"Digite a quantidade a crescentar no {nome}\n"))
                produto_encontrado = True
                limpar_tela()
                print("Produto foi atualizado com sucesso !")
                time.sleep(2)
                limpar_tela()
                break

        if produto_encontrado:
            continue

        produto_novo["nome"] = nome
        produto_novo["preco"] = input('Preço do produto\n')
        produto_novo["quantidade"] = input('Quantidade do produto\n')
        produtos.append(produto_novo)


        limpar_tela()
        print("\033[92mProduto cadastrado com sucesso !\033[0m")
        time.sleep(2)
        limpar_tela()

    elif opcao == 2:
        if len(produtos) == 0:
            print("Nenhum produto cadastrado !")
            time.sleep(2)
            limpar_tela()
        else:
            # for produto in produtos:
            #     print(f"Nome: {produto['nome']}")
            #     print(f"Preço: {produto['preco']}")
            #     print(f"Quantidade: {produto['quantidade']}")
            #     print("-"*20)

            #     input("Digite enter para continuar ...")
            #     limpar_tela()

            imprimir_tabela(produtos)

            input("Digite enter para continuar ...")
            limpar_tela()
    elif opcao == 3:
        break

