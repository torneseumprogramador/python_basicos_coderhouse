import mysql.connector

# Conectar ao banco de dados MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='cadastro_de_produtos'
)

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar a tabela 'produtos'
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    preco FLOAT NOT NULL,
    quantidade INT NOT NULL
)
''')

# Confirmar (commit) a transação
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
