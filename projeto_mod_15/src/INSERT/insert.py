import sqlite3

# Função para verificar se a tabela existe em um banco específico
def verificar_tabela_existente(nome_tabela, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nome_tabela,))
    tabela = cursor.fetchone()
    conn.close()
    return tabela is not None

# Função para remover acentos manualmente
def remover_acentos(texto):
    mapeamento = {
        'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c'
    }
    return ''.join(mapeamento.get(c, c) for c in texto)

# Lista de todos os tipos de Pokémon válidos (sem acentos e em minúsculas)
TIPOS_VALIDOS = [
    "normal", "fogo", "agua", "eletrico", "grama", "gelo", "lutador", "venenoso",
    "terra", "voador", "psiquico", "inseto", "pedra", "fantasma", "dragao",
    "sombrio", "aco", "fada"
]

# Função para adicionar Pokémon à Pokedex
def adicionar_pokemon():
    nome_tabela = input("Digite o nome da tabela onde deseja adicionar o Pokémon: ")

    # Verificar se a tabela existe no banco de dados do Pokémon
    if not verificar_tabela_existente(nome_tabela, "data/pokedex.db"):
        print(f"❌ A tabela '{nome_tabela}' não existe. Tente novamente.")
        return
    
    nome = input("Nome do Pokémon: ")
    tipo = input("Tipo do Pokémon: ")
    
    tipo_normalizado = remover_acentos(tipo.lower())
    if tipo_normalizado not in TIPOS_VALIDOS:
        print(f"❌ Tipo '{tipo}' inválido! Escolha um dos seguintes: {', '.join(TIPOS_VALIDOS)}")
        return
    
    tipo_formatado = tipo_normalizado.capitalize()
    conn = sqlite3.connect("data/pokedex.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {nome_tabela} (nome, tipo) VALUES (?, ?)", (nome, tipo_formatado))
    conn.commit()
    conn.close()
    print(f"✅ Pokémon '{nome}' adicionado à tabela '{nome_tabela}' com sucesso!")

# Função para adicionar Treinador à tabela de Treinadores
def adicionar_treinador():
    nome_tabela = input("Digite o nome da tabela onde deseja adicionar o Treinador: ")

    # Verificar se a tabela existe no banco de dados do Treinador
    if not verificar_tabela_existente(nome_tabela, "data/treinadores.db"):
        print(f"❌ A tabela '{nome_tabela}' não existe. Tente novamente.")
        return
    
    nome = input("Nome do Treinador: ")
    idade = input("Idade do Treinador: ")
    cidade = input("Cidade de origem do Treinador: ")
    
    conn = sqlite3.connect("data/treinadores.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {nome_tabela} (nome, idade, cidade) VALUES (?, ?, ?)", (nome, idade, cidade))
    conn.commit()
    conn.close()
    print(f"✅ Treinador '{nome}' adicionado à tabela '{nome_tabela}' com sucesso!")
