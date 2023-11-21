def print_colorido(text, color):
    colors = {
        "amarelo": "\033[93m",
        "azul": "\033[94m",
        "vermelho": "\033[91m",
    }

    # Verifica se a cor fornecida existe no dicionário
    if color in colors:
        # Imprime o texto na cor escolhida
        print(f"{colors[color]}{text}\033[0m")
    else:
        # Se a cor não for reconhecida, imprime o texto sem cor
        print(text)

# Exemplos de uso
print_colorido("Este é um texto em amarelo", "amarelo")
print_colorido("Este é um texto em azul", "azul")
print_colorido("Este é um texto em vermelho", "vermelho")
