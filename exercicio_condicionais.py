'''
Crie uma aplicação para calcular a média de um aluno
vc vai digitar o nome do aluno e 3 notas
no final do programa mostrar se o aluno está aprovado, reprovado ou recuperação
critério:
- media menor que 5 = reprovado
- media entre 5 e 6.9 = recuperacao
- 7 ou acima = aprovado
'''

nome = input("Digite o nome do aluno:\n")
nota1 = float(input(f"Digite a nota 1 do {nome}:\n"))
nota2 = float(input(f"Digite a nota 2 do {nome}:\n"))
nota3 = float(input(f"Digite a nota 3 do {nome}:\n"))

media = (nota1 + nota1 + nota3) / 3

print(f"Média do aluno: {media}")

if media < 5:
    print(f"O aluno {nome} está reprovado")
elif media >= 5 and media < 7 :
    print(f"O aluno {nome} está em recuparação")
else:
    print(f"O aluno {nome} está aprovado")

