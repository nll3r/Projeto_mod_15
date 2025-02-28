import sqlite3

def criar_tabela_personalizada():
    nome_tabela = input("Digite o nome da nova tabela: ")

    # Conectar ao banco de dados
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()

    # Criar a tabela se não existir
    try:
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {nome_tabela} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT UNIQUE NOT NULL,
                tipo TEXT NOT NULL
            )
        """)
        conn.commit()
        print(f"✅ Tabela '{nome_tabela}' criada com sucesso!")
    except sqlite3.Error as e:
        print(f"❌ Erro ao criar a tabela: {e}")
    finally:
        conn.close()
