import sqlite3

# Faz a conexão com o banco; se não existir, ele cria um arquivo "Banco_praticando"
conexao = sqlite3.connect("primeiro_sqlite.db")

# O cursor funciona como uma caneta, permitindo editar/ler as tabelas
cursor = conexao.cursor()

# Tipos de dados mais usados: TEXT, INTEGER, REAL
cursor.execute("CREATE TABLE IF NOT EXISTS pessoa (nome TEXT, idade INTEGER)")
# IF NOT EXISTS → só cria a tabela se ela não existir

# Inserindo valores (exemplo)
# cursor.execute("INSERT INTO pessoa VALUES('Gabriel', 21)")

# Salva as alterações
conexao.commit()

# Fazendo uma consulta
cursor.execute("SELECT * FROM pessoa")  
# SELECT → selecionar
# * → todas as colunas 
# FROM pessoa → indica a tabela de onde virão os dados

# Mostra todos os registros como lista de tuplas
print(cursor.fetchall())

# Fecha a conexão
conexao.close()
