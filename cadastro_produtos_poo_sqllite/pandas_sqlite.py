import pandas as pd
import sqlite3

conn = sqlite3.connect('db/cadastro_de_produtos.db')
query = "select * from produtos"
df = pd.read_sql(query, conn)

print(df)

conn.close()