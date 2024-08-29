"""
DIGITE A SENHA CORRETA
"""
senha_correta = "abracadabra2B"

while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Senha correta! Acesso concedido.")
        break
    else:
        print("Senha incorreta! Tente novamente.")