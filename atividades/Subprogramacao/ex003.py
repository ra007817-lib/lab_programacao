def permitir_acesso(ano_nascimento):
    ano_atual = 2026
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        return True
    else:
        return False


ano = int(input("Digite o ano de nascimento: "))

if permitir_acesso(ano):
    print("Bem-vindo! Acesso permitido.")
else:
    print("Acesso bloqueado. Menor de idade.")