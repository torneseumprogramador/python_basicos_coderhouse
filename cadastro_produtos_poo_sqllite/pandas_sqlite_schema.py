import pandas as pd
import sqlite3

conn = sqlite3.connect('db/cadastro_de_produtos.db')
query = "select name from sqlite_master where type='table'"
df = pd.read_sql_query(query, conn)

print(df)

conn.close()