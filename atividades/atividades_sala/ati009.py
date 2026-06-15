"""
cria um simulador de fluxo de caixa. o progrma de reseber operações
finaseiras de uma impresa. o usuario digita o valor (posivimo para reseita negatovo para dispessa).]
cada valor de ser gurdado em um vertor historioco. o progrma para quando o usurio digitar 0.
no final, lipe todos os valores que forem menores que 5 reais (tato poisivos quando negativos).
usado o comado del ou remove, e msotre o saldo final remansente.
"""

historico = []

while True:
    valor = float(input("Digite o valor da operação (0 para sair): "))

    if valor == 0:
        break

    historico.append(valor)

print("\nHistórico original:")
print(historico)

for valor in historico[:]:
    if abs(valor) < 5:
        historico.remove(valor)

print("\nHistórico após remover valores menores que R$ 5:")
print(historico)

saldo_final = sum(historico)

print(f"\nSaldo final remanescente: R$ {saldo_final:.2f}")