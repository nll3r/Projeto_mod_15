import sqlite3

def verificar_tabela_existente(nome_tabela):
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nome_tabela,))
    tabela = cursor.fetchone()
    conn.close()
    return tabela is not None

def listar_tabelas():
    # Conectar ao banco de dados
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()

    # Consultar todas as tabelas no banco de dados
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tabelas = cursor.fetchall()
    conn.close()

    # Verificar se existem tabelas no banco de dados
    if tabelas:
        print("\n📜 Tabelas existentes no banco de dados:")
        for tabela in tabelas:
            print(f"- {tabela[0]}")
    else:
        print("❌ Nenhuma tabela encontrada no banco de dados!")