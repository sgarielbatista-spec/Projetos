import sqlite3
import os

conexao = sqlite3.connect("banco_mercado.db")
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        preco REAL
    )

""")

def adicionar_banco(nome, preco):
    cursor.execute("INSERT INTO produtos (nome, preco) VALUES(?,?)", (nome, preco))
    conexao.commit()

def ver_banco():
    cursor.execute("SELECT * FROM produtos")
    conteudo_banco = cursor.fetchall()
    if not conteudo_banco:
        print("")
        return
    for id, nome, preco in conteudo_banco:
        print(f"ID: {id} | Nome: {nome} | preço: R${preco:.2f}")

def deletar_produto(id):
    try:
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
    except sqlite3.Error as erro:
        os.system('cls')
        print("Erro ao remover produto, digite o id corretamente")
    
    conexao.commit()

def loop_adicionarprodutos():
    while True:
            nome = input("Digite o nome o produto para adicionar ou [s]air: ")
            if nome.lower() == 's':
                break

            try:
                preco = float(input("Agora digite o seu preço: "))
            except ValueError:
                os.system("cls")
                print("Digite apenas numeros")
                continue

            adicionar_banco(nome, preco)

while True:
    print("Escolhas:")
    print("addcionar[a]")
    print("remover[r]")
    print("ver[v]")
    print("fechar[f]")
    escolha = input("Digite qual a opçao executar: ").lower()
    os.system('cls')

    #valida a entrada, se não for algo esperado ele volta o código.
    entradas_verificadas = 'arvf'
    if escolha not in entradas_verificadas:
        print("Digíte apenas as opções permitidas")
        continue
    
    elif escolha == 'a':#onde adciona ao banco de dados, nome e preço
        loop_adicionarprodutos()
        
    elif escolha == 'f': #onde fecha o programa caso o usuario escolha 'f'
        os.system('cls')
        conexao.close()
        break
    
    elif escolha == "v":#local para ver os itens que estão no banco de dados
        ver_banco()
        qual_quer_coisa_para_fechar = input("Digite qualuer coisa para fechar: ")
        os.system('cls')
        
    elif escolha == 'r': #onde eu posso ver o que tem salvo no banco de dados.
        ver_banco()
        try:
            excluir_por_id = int(input("Digite o id do produto no qual quer excluir: "))
            deletar_produto(excluir_por_id)
        except ValueError:
            print("Digite apenas números validos para o id")
        os.system("cls")
print("programa fechado.")