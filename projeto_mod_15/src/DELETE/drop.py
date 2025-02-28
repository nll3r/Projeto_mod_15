import sqlite3

def verificar_tabela_existente(nome_tabela):
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nome_tabela,))
    tabela = cursor.fetchone()
    conn.close()
    return tabela is not None

def remover_tabela():
    nome_tabela = input("Digite o nome da tabela que deseja remover: ")

    if not verificar_tabela_existente(nome_tabela):
        print(f"❌ A tabela '{nome_tabela}' não existe. Tente novamente.")
        return
    
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {nome_tabela}")
    conn.commit()
    conn.close()
    print(f"🗑️  Tabela '{nome_tabela}' removida com sucesso!")