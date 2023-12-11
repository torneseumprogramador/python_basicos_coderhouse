import sqlite3

# Conectar ao banco de dados SQLite; será criado se não existir
conn = sqlite3.connect('db/cadastro_de_produtos.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar a tabela 'produtos'
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(150) NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
)
''')

# Confirmar (commit) a transação
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
