

def ler_lista(index, numeros):
    if (index + 1) >= len(numeros):
        return
    
    print(f"Numero: {numeros[index]}")
    ler_lista(index+1, numeros)

numeros = [6,7,3,4,7,10,8]

ler_lista(0, numeros)