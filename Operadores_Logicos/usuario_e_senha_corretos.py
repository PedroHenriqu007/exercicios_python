# Usuário deve ser “admin” e senha “1234”. Se errar qualquer um, exibir “Acesso negado”.

usuario_correto = "admin"
senha_correta = 1234

usuario = input("Usuário: ")
senha = int(input("Senha: "))

if usuario == usuario_correto and senha == senha_correta:
    print("Acesso permitido.")
else:
    print("Acesso negado.")