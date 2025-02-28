import sys
import os

# Adiciona o diretório pai ao sys.path para permitir importações de outros diretórios
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa as funções de cada módulo

# Importa as funções de cada módulo
from CREATE.create import criar_tabela_personalizada
from INSERT.insert import adicionar_pokemon
from READ.read import listar_pokedex, buscar_pokemon
from UPDATE.update import atualizar_pokemon
from DELETE.delete import remover_pokemon
from DELETE.drop import remover_tabela
from READ.tabela import listar_tabelas
from INNERJOIN.inner import unir_tabelas



# Menu principal
def menu():
    while True:
        print("\n📌 MENU DA POKEDEX")
        print("1️ - Criar nova Pokédex")
        print("2️ - Apagar uma Pokédex")
        print("3️ - Adicionar um Pokémon")
        print("4️ - Listar toda a Pokédex")
        print("5️ - Buscar Pokémon por nome")
        print("6️ - Atualizar informações de um Pokémon")
        print("7️ - Remover Pokémon")
        print("8️ - Listar Pokédexs")
        print("9️ - Juntar Pokédexs")
        print("0️ - Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            criar_tabela_personalizada()
        elif escolha == "2":
            remover_tabela()
        elif escolha == "3":
            adicionar_pokemon()
        elif escolha == "4":
            listar_pokedex()
        elif escolha == "5":   
            nome_tabela = input("Digite o nome da tabela que deseja listar: ") 
            id = input("ID do Pokémon que deseja buscar: ")
            buscar_pokemon(nome_tabela, id)
        elif escolha == "6":
            nome = input("Nome do Pokémon que deseja atualizar: ")
            novo_tipo = input("Novo tipo: ")
            atualizar_pokemon(nome, novo_tipo)
        elif escolha == "7":
            remover_pokemon()
        elif escolha == "8":
            listar_tabelas() 
        elif escolha == "9":
                unir_tabelas()
        elif escolha == "0":
            print("Saindo da Pokedex...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
