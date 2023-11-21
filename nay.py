'''
Geraldo tem uma venda de sapatos
ele anota os seus pedidos em um papel
precisamos criar um programa para ajudar geraldo
no que teremos neste programa:
- captura do nome do cliente
- marca do sapato do cliente
- quantidade sapatos
- valor a pagar

se o cliente deixar mais de 1 sapato, mostrar o valor total a pagar
'''


nome = input("Digite o nome do cliente:\n")
marca = input("Digite a marca do sapato:\n")
quantidade = int(input("Digite a quantidade de sapatos:\n"))
valor = float(input("Digite o valor do sapato:\n"))

valor_total = valor * quantidade
print("O valor total a pagar é de: R$", valor_total)
