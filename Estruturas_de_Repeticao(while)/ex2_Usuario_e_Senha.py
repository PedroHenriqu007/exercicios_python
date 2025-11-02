""" 
O programa deve pedir usuário e senha até o usuário digitar:
    Usuário: admin
    Senha: 1234
"""

usuario_correto = "admin"
senha_correta = 1234


while True:
    usuario = input("Usuário: ")
    senha = int(input("Senha: "))
    
    if(usuario == usuario_correto and senha == senha_correta):
        print("Acesso permitido.")
        break