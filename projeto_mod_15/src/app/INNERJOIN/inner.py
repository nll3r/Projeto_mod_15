import sqlite3

def verificar_tabela_existente(nome_tabela):
    """Verifica se a tabela existe no banco de dados"""
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nome_tabela,))
    tabela = cursor.fetchone()
    conn.close()
    return tabela is not None

def unir_tabelas():
    """Permite ao usuário escolher duas tabelas e unir os dados"""
    
    # Solicitar os nomes das tabelas
    tabela1 = input("Digite o nome da primeira tabela: ")
    tabela2 = input("Digite o nome da segunda tabela: ")

    # Verificar se ambas as tabelas existem
    if not verificar_tabela_existente(tabela1):
        print(f"❌ A tabela '{tabela1}' não existe. Tente novamente.")
        return
    
    if not verificar_tabela_existente(tabela2):
        print(f"❌ A tabela '{tabela2}' não existe. Tente novamente.")
        return
    
    # Conectar ao banco de dados e executar a união
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    
    try:
        query = f"""
        SELECT * FROM {tabela1}
        UNION ALL
        SELECT * FROM {tabela2}
        """
        cursor.execute(query)
        resultados = cursor.fetchall()
        
        # Exibir os resultados
        if resultados:
            print("\n📊 RESULTADOS DA UNIÃO DAS TABELAS:")
            for linha in resultados:
                print(linha)
        else:
            print("📭 Nenhum resultado encontrado na união das tabelas.")

    except sqlite3.Error as e:
        print(f"❌ Erro ao unir as tabelas: {e}")

    conn.close()
