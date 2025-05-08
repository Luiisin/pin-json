import json
import os

ARQUIVO = 'dados.json'

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    else:
        return {}

def salvar_dados(dados):
    with open(ARQUIVO, 'w') as f:
        json.dump(dados, f, indent=4)

def menu():
    while True:
        print("\n1. Adicionar dado")
        print("2. Consultar dados")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome: ")
            idade = input("Digite a idade: ")
            dados = carregar_dados()
            dados[nome] = idade
            salvar_dados(dados)
            print("Dado salvo com sucesso!")
        elif opcao == '2':
            dados = carregar_dados()
            if dados:
                for nome, idade in dados.items():
                    print(f"{nome}: {idade} anos")
            else:
                print("Nenhum dado encontrado.")
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()
