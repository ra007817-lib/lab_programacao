vetor = []

for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor.append(valor)

x = int(input("Digite o valor que deseja procurar: "))

posicao = -1

for i in range(5):
    if vetor[i] == x:
        posicao = i
        break

print(f"Posição do valor {x}: {posicao}")