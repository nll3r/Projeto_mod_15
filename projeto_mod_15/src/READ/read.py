import sqlite3

def verificar_tabela_existente(nome_tabela):
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nome_tabela,))
    tabela = cursor.fetchone()
    conn.close()
    return tabela is not None


def listar_pokedex():
    nome_tabela = input("Digite o nome da tabela que deseja listar: ")

    if not verificar_tabela_existente(nome_tabela):
        print(f"❌ A tabela '{nome_tabela}' não existe. Tente novamente.")
        return
    
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {nome_tabela}")
    pokemons = cursor.fetchall()
    conn.close()
    
    if pokemons:
        print("\n📖 POKEDEX:")
        for p in pokemons:
            print(f"ID: {p[0]} | Nome: {p[1]} | Tipo: {p[2]}")
    else:
        print("Pokédex vazia!")

def buscar_pokemon(nome_tabela, id):
    
    if not verificar_tabela_existente(nome_tabela):
        print(f"❌ A tabela '{nome_tabela}' não existe. Tente novamente.")
        return
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    # Alterando a consulta para buscar pelo id
    cursor.execute(f"SELECT * FROM {nome_tabela} WHERE id=?", (id,))
    pokemon = cursor.fetchone()
    conn.close()

    if pokemon:
        print(f"🔍 Pokémon encontrado: ID: {pokemon[0]} | Nome: {pokemon[1]} | Tipo: {pokemon[2]}")
    else:
        print("❌ Pokémon não encontrado!")