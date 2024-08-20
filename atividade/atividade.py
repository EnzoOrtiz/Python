nomes = []

def adicionar_nome(nome):
    nomes.append(nome)
    print(f'Nome "{nome}" adicionado à lista.')

def remover_nome(nome):
    if nome in nomes:
        nomes.remove(nome)
        print(f'Nome "{nome}" removido da lista.')
    else:
        print(f'O nome "{nome}" não foi encontrado na lista.')

def listar_nomes():
    if nomes:
        print("Lista de Nomes:")
        for i, nome in enumerate(nomes, 1):
            print(f"{i}. {nome}")
    else:
        print("A lista está vazia.")

while True:
    print("\n1. Adicionar Nome")
    print("2. Remover Nome")
    print("3. Listar Nomes")
    print("4. Sair")
    
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        nome = input("Digite o nome a ser adicionado: ")
        adicionar_nome(nome)
    elif escolha == '2':
        nome = input("Digite o nome a ser removido: ")
        remover_nome(nome)
    elif escolha == '3':
        listar_nomes()
    elif escolha == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida, por favor tente novamente.")
