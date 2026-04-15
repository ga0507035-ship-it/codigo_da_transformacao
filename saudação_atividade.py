def saudacao(nome):
    print(f"Olá, {nome}! Seja muito bem-vindo(a).")


saudacao("Carlos")


def calcular_media(notas):
    media = sum(notas) / len(notas)
    
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
        
    print(f"Média: {media:.1f} - Situação: {situacao}")


calcular_media([8.5, 6.0, 7.5])


def maior_menor(lista_numeros):
    maior = max(lista_numeros)
    menor = min(lista_numeros)
    return maior, menor

# Exemplo de uso:
num_maior, num_menor = maior_menor([10, 5, 22, 1, 34])
print(f"O maior número é {num_maior} e o menor é {num_menor}.")



usuarios_cadastrados = {
    "admin": "1234",
    "joao_silva": "senhaSegura",
    "maria": "p@ssword"
}

def validar_login(usuario, senha):
    # Verifica se o usuário existe e se a senha coincide
    if usuario in usuarios_cadastrados and usuarios_cadastrados[usuario] == senha:
        return "Login realizado com sucesso! Bem-vindo."
    else:
        return "Usuário ou senha incorretos."


user_input = input("Digite o usuário: ")
pass_input = input("Digite a senha: ")

print(validar_login(user_input, pass_input))
