import sqlite3

def verificar_tabela_existente(nome_tabela):
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nome_tabela,))
    tabela = cursor.fetchone()
    conn.close()
    return tabela is not None

def atualizar_pokemon():
    nome_tabela = input("Digite o nome da tabela: ")

    # Verificar se a tabela existe
    if not verificar_tabela_existente(nome_tabela):
        print(f"❌ A tabela '{nome_tabela}' não existe. Tente novamente.")
        return
    
    # Solicitar o ID do Pokémon
    id_pokemon = input("Id do Pokémon que deseja atualizar: ")

    # Perguntar ao usuário se ele quer mudar o nome, o tipo ou ambos
    print("\nO que deseja atualizar?")
    print("1 - Nome")
    print("2 - Tipo")
    print("3 - Nome e Tipo")
    escolha = input("Escolha uma opção: ")

    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()

    # Dependendo da escolha, fazer as atualizações
    if escolha == "1":
        novo_nome = input("Digite o novo nome: ")
        cursor.execute(f"UPDATE {nome_tabela} SET nome=? WHERE id=?", (novo_nome, id_pokemon))
        print(f" O nome do Pokémon com ID {id_pokemon} foi alterado para {novo_nome}!")
    
    elif escolha == "2":
        novo_tipo = input("Digite o novo tipo: ")
        cursor.execute(f"UPDATE {nome_tabela} SET tipo=? WHERE id=?", (novo_tipo, id_pokemon))
        print(f" O Pokémon com ID {id_pokemon} agora é do tipo {novo_tipo}!")
    
    elif escolha == "3":
        novo_nome = input("Digite o novo nome: ")
        novo_tipo = input("Digite o novo tipo: ")
        cursor.execute(f"UPDATE {nome_tabela} SET nome=?, tipo=? WHERE id=?", (novo_nome, novo_tipo, id_pokemon))
        print(f" O Pokémon com ID {id_pokemon} agora tem o nome {novo_nome} e tipo {novo_tipo}!")

    else:
        print("❌ Opção inválida!")
        conn.close()
        return

    conn.commit()
    conn.close()