vetor = []
diferentes = []

for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor.append(valor)

for numero in vetor:
    if numero not in diferentes:
        diferentes.append(numero)

print("Quantidade de valores diferentes:", len(diferentes))