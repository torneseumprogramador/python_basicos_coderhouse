import sqlite3
class Produto:
    def __init__(self, id=0, nome="", preco=0, quantidade=0):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def incluir(self):
        conn = sqlite3.connect('db/cadastro_de_produtos.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO produtos (nome, preco, quantidade)
            VALUES (?, ?, ?)
        ''', (self.nome, self.preco, self.quantidade))

        # Confirmar a transação e fechar a conexão
        conn.commit()
        conn.close()
        

    @staticmethod
    def todos():
         # Conectar ao banco de dados
        conn = sqlite3.connect('db/cadastro_de_produtos.db')
        cursor = conn.cursor()

        # Buscar todos os produtos no banco de dados
        cursor.execute('SELECT * FROM produtos')
        produtos_db = cursor.fetchall()

        # Fechar a conexão com o banco de dados
        conn.close()

        # Converter os resultados em objetos Produto
        return [Produto(id=id, nome=nome, preco=preco, quantidade=quantidade) for id, nome, preco, quantidade in produtos_db]