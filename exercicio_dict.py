'''
Professora elena precisa de um programa para 
anotar os dados de notas de seus amigos professores
ela precisa anotar o nome do professor + uma lista de alunos com 4 notas cada
um e se os alunos estão aprovados ou reprovados.
'''

profesores = [
    [
        'Claber', 
        [
            ['josé', [9, 6, 7]],
            ['leandro', [9, 6, 7]],
            ['Jeniffer', [9, 6, 7]],
        ]
    ],
    [
        'Vinicius', 
        [
            ['Keyla', [9, 6, 7]],
            ['Helena', [10, 8, 7]],
            ['Fabiana', [1, 2, 7]],
        ]
    ]
]








print(profesores[1][1][0][0])
print(profesores[1]['alunos'][0]["nome"])








profesores = [
    {
        'professor': 'Claber', 
        'alunos': [
            {'nome': 'josé', 'notas': [9, 6, 7]},
            {'nome': 'leandro', 'notas': [9, 6, 7]},
            {'nome': 'Jeniffer', 'notas': [9, 6, 7]},
        ]
    },
    {
        'professor': 'Vinicius', 
        'alunos': [
            {'nome': 'Keyla', 'notas': [9, 6, 7]},
            {'nome': 'Helena', 'notas': [10, 8, 7]},
            {'nome': 'Fabiana', 'notas': [1, 2, 7]},
        ]
    }
]

print(profesores[1]['alunos'][0]["nome"])









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