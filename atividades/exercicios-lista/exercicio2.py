"""
2. Faça um progrma que percorre um vetor e imprime na
tela a média dos valores do vetor e o valor mais
próximo da média. Exemplo:
Vetor: [2.5,7.5,10.0,4.0]
Media: 6.0
Valor mais próximo da média: 7.5
"""
vetor = [2.5, 7.5, 10.0, 4.0]


media = sum(vetor) / len(vetor)

mais_proximo = vetor[0]

for valor in vetor:
    if abs(valor - media) < abs(mais_proximo - media):
        mais_proximo = valor

print("Vetor:", vetor)
print("Média:", media)
print("Valor mais próximo da média:", mais_proximo)