# nome1 = input("Digite o nome do aluno 1\n")
# nome2 = input("Digite o nome do aluno 2\n")
# nome3 = input("Digite o nome do aluno 3\n")
# nome4 = input("Digite o nome do aluno 4\n")

# matriz
aluno1 = ["Matheus",6,7,8]
aluno2 = ["Bruno", 8,7,8]
aluno3 = ["Naiara", 3,7,10]
aluno4 = ["Kethelyn", 8,8,9]

alunos = [aluno1, aluno2, aluno3, aluno4]

# # matriz
print(f"Nome: {alunos[3][0]}")
print(f"Nota 1: {alunos[3][2]}")

# print(len(alunos))

# print(alunos)

alunos = [
    { "nome": "Matheus", "notas": [6,7,8] },
    { "nome": "Tomás", "notas": [8,10,9] }
]
print(alunos[1]["nome"])
print(alunos[1]["notas"])



