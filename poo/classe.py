import pdb # = debugger
'''
n = proxima linha
s = entrar dentro do método
c = continua até o proximo break point ou até acabar o programa
l = lista onde está parado no break point
'''

class Cachorro:
    def __init__(self, nome="Cachorro", raca="Fox Paulistano", idade=1):
        # pdb.set_trace() # break point
        self.nome = nome
        self.raca = raca
        self.idade = idade
    
    def descrever(self):
        print(f"Nome: {self.nome}")
        print(f"Raça: {self.raca}")
        print(f"Idade: {self.idade}")

    def incluir(self):
        Cachorro.todos_cachorros.append(self)

    todos_cachorros = []

    @staticmethod
    def todos():
        return Cachorro.todos_cachorros


pdb.set_trace()
Cachorro("Billy", "Beagle", 12).incluir()
Cachorro("Boomer", "Beagle", 10).incluir()

for cachorro in Cachorro.todos():
    print("-"* 30)
    cachorro.descrever()

# billy = Cachorro("Billy", "Beagle", 12)
# billy.descrever()

# print("-"* 30)

# Cachorro().descrever()
# print("-"* 30)

# thanos = Cachorro("thanos", "American bully", 2)
# thanos.descrever()

# print("-"* 30)

# boomer_dict = {"nome": "Boomer", "raca": "", "idade": 0}
# print(boomer_dict["nome"])

# print("-"* 30)

# thanos_dict = {"nome": "Boomer", "raca": "", "idade": 0, "cpf": "ddd"}
# print(thanos_dict["cpf"])
