import random

vetor = []
quantidade6 = 0

for i in range(50):
    valor = random.randint(1, 6)
    vetor.append(valor)

    if valor == 6:
        quantidade6 += 1


percentual = (quantidade6 / 50) * 100

print("Lançamentos:", vetor)
print("Quantidade de faces 6:", quantidade6)
print("Percentual de faces 6:", f" {percentual:.2f}%", sep="")