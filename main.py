usuarios = []

def cadastrar_usuario():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    email = input("Digite o email: ")

    usuario = {
        'nome':nome,
        'idade':idade,
        'email':email
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def exibir_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado, por favor cadastre um.")
    else:
        for i, usuario in enumerate(usuarios,1):
            print(f"Usuário {i}: {usuario['nome']} | Idade: {usuario['idade']} | Email: {usuario['email']}")

def menu():
    while True:
        print("\n1. Cadastrar Usuário")
        print("2. Exibir Usuários")
        print("Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            cadastrar_usuario()
        elif escolha == "2":
            exibir_usuarios()
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção invalida! Tente novamente.")

menu()
