from prettytable import PrettyTable

# Suponha que sua lista de produtos seja algo assim:
produtos = [
    {"nome": "Produto 1", "preco": "10.00", "quantidade": "5"},
    {"nome": "Produto 2", "preco": "20.00", "quantidade": "3"},
    # Adicione mais produtos conforme necessário
]

# Criando a tabela
tabela = PrettyTable()
tabela.field_names = ["Nome", "Preço", "Quantidade"]

# Adicionando linhas à tabela
for produto in produtos:
    tabela.add_row([produto["nome"], produto["preco"], produto["quantidade"]])

# Exibindo a tabela
print(tabela)
