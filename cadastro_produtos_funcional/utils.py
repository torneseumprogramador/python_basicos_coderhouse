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