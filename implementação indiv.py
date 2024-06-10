usuarioEsenha = {}
livros = {}

def gerenciar_usuario(usuarios, senhas):
    usuarios = input("Digite o nome de usuário: ")
    nome_capitalizado = usuarios.capitalize()
    senhas = input("Digite sua senha: ")

    usuarioEsenha[nome_capitalizado] = senhas

    try:
        with open("usuarios.txt", "r") as f:
            conteudo = f.read().strip()
        
    except Exception as e:
        print(f"Erro: {e}")
        conteudo = ""

    with open("usuarios.txt", "w") as f:
        if conteudo:
            f.write(conteudo + "\n")
        f.write(f"Usuario: ({nome_capitalizado}) senha: ({senhas})")
    
    print("Usuario", nome_capitalizado, "registrado com sucesso!")
    
def login(usuarios, senhas):
    usuarios = input("Digite o nome de usuário ")
    nome_capitalizado = usuarios.capitalize()
    senhas = input("Digite sua senha: ")

    if nome_capitalizado in usuarioEsenha and usuarioEsenha[nome_capitalizado] == senhas:
        print("Login feito com sucesso!")
    else:
        print("Nome de usuário ou senha incorreta!")

def cadastrar_livros(livro):
    livro = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    ano = input("Digite o ano de publicação: ")
    livros[livro] = {'autor': autor, 'ano_publicacao': ano}
    
    try:
        with open("livros.txt", "r") as f:
            conteudo = f.read().strip()
    except FileNotFoundError:
        conteudo = ""

    with open("livros.txt", "w") as f:
        if conteudo:
            f.write(conteudo + "\n")
        f.write(f"Livro: ({livro}) Autor: ({autor}) Ano: ({ano})")
    
    print("Livro registrado com sucesso!")

def retornar_usuarios(usuarios, senhas):
    print("Usuários registrados:")
    for usuarios, senhas in usuarioEsenha.items():
        print(f"Usuário: {usuarios}, Senha: {senhas}")

def retornar_livros(livro):
    print("Livros cadastrados:")
    for livro, detalhes in livros.items():
        print(f"Título do livro: {livro}, Autor: {detalhes['autor']}, Ano: {detalhes['ano_publicacao']}")

def ordenar_usuarios():
    for usuarios in sorted(usuarioEsenha):
        print(f"Usuário: {usuarios}, Senha: {usuarioEsenha[usuarios]}")

def ordenar_livros():
    for livro in sorted(livros):
        detalhes = livros[livro]
        print(f"Título do livro: {livro}, Autor: {detalhes['autor']}, Ano: {detalhes['ano_publicacao']}")

def main():
    usuarios = []
    senhas = {}
    livro = {}
    while True:
        print("\n*** Menu ***")
        print("1. Cadastrar usuário")
        print("2. Login")
        print("3. Cadastrar livro")
        print("4. Mostrar usuários cadastrados (ordenados)")
        print("5. Mostrar livros cadastrados (ordenados)")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            gerenciar_usuario(usuarios, senhas)
        elif opcao == "2":
            login(usuarios, senhas)
        elif opcao == "3":
            cadastrar_livros(livro)
        elif opcao == "4":
            ordenar_usuarios()
        elif opcao == "5":
            ordenar_livros()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
