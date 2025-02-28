1. [Introdução](#introdução)
2. [Estrutura do Projeto](#estrutura-do-projeto)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Como Utilizar](#como-utilizar)
5. [Testes](#testes)
6. [Notas Finais](#notas-finais)

## Introdução

Este projeto é uma aplicação para gestão de informações relacionadas a Pokémon, numa versão virtual inspirada na POKÉDEX. Os utilizadores podem escolher o nome da tabela para armazenar os dados.

## Estrutura do Projeto

- **POKÉDEX/**
  - Diretório principal do projeto

### Subdiretórios e Ficheiros

#### 1. **src/**
Contém o código fonte do projeto, dividido por funcionalidade:

- **app/**
  - : Ponto de entrada principal da aplicação.
  - : Script responsável por unir dados de duas tabelas.

- **CREATE/**
  - Scripts responsáveis por criar novos registos na base de dados.
    - : Criação de tabelas personalizadas.

- **READ/**
  - Scripts responsáveis por ler dados da base de dados.
    - : Leitura de dados de Pokémon.
    - : Listagem de tabelas existentes.

- **UPDATE/**
  - Scripts responsáveis por atualizar registos existentes.
    - : Atualização de dados de Pokémon.

- **DELETE/**
  - Scripts responsáveis por eliminar registos.
    - : Eliminação de dados de Pokémon.
    - : Eliminação de tabelas.

- **INSERT/**
  - Scripts responsáveis por inserir novos registos na base de dados.
    - : Inserção de dados de Pokémon e Treinadores.

- **utils.py**
  - Funções utilitárias usadas em todo o projeto.

#### 2. **data/**
Contém a base de dados SQLite:
- : Base de dados principal.

#### 3. **README.md**
Este ficheiro descreve a estrutura do projeto e fornece informações gerais.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **SQLite**: Base de dados utilizada.
- **Estrutura Modular**: Código organizado por módulos e funcionalidades.

## Como Utilizar

1. Certifique-se de que possui o Python instalado na sua máquina.
2. Navegue até o diretório `src/app/` e execute o ficheiro `main.py`:
   
   ```bash
   python main.py
   ```
3. Para utilizar outras funcionalidades, explore os scripts nas subpastas `CREATE/`, `READ/`, `UPDATE/`, `DELETE/` e `INSERT/`.

## Testes

Para rodar os testes, utilize o comando:

```bash
pytest
```

## Notas Finais

Este projeto segue boas práticas de organização de código e está estruturado para facilitar a manutenção e expansão.
