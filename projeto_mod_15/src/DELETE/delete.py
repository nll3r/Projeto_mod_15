import sqlite3
from utils import verificar_tabela_existente  # Importando função utilitária

def remover_pokemon():
    nome_tabela = input("Digite o nome da tabela: ")

    # Verificar se a tabela existe
    if not verificar_tabela_existente(nome_tabela, "data/pokedex.db"):
        print(f"❌ A tabela '{nome_tabela}' não existe. Tente novamente.")
        return
    
    id = input("ID do Pokémon que deseja remover: ")

    # Verificar se o ID é um número válido
    if not id.isdigit():
        print("⚠️ ID inválido! Certifique-se de digitar um número.")
        return
    
    # Converter o ID para inteiro
    id = int(id)
    
    # Conectar ao banco de dados e verificar se o Pokémon existe
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {nome_tabela} WHERE id=?", (id,))
    pokemon = cursor.fetchone()
    
    # Verificar se o Pokémon existe
    if pokemon is None:
        print(f"❌ Pokémon com ID {id} não encontrado na tabela '{nome_tabela}'.")
        conn.close()
        return
    
    # Se o Pokémon existir, realizar a remoção
    cursor.execute(f"DELETE FROM {nome_tabela} WHERE id=?", (id,))
    conn.commit()
    conn.close()
    
    print(f"🗑️ Pokémon com ID {id} foi removido da tabela '{nome_tabela}'!")
