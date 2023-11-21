print(len('banana'))
print(len('maça'))
print(len('melão'))

frutas = ['banana', 'maça', 'melão']
tamanhos = map(len, frutas)

print(list(tamanhos))


def escrever_colorido(cor_texto):
    cor, texto = cor_texto
    cores = {
        'amarelo': '\033[93m',
        'vermelho': '\033[91m',
        'verde': '\033[92m',
    }

    return f"{cores[cor]}{texto}\033[0m"

textos = [['amarelo', "Escrito em amarelo"], ['vermelho', "Escrito em vermelho"], ['verde', "Escrito em verde"]]
textos_escritos = map(escrever_colorido, textos)

for texto in list(textos_escritos):
    print(texto)