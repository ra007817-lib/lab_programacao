"""
1. Faça um programa que simule um lançamento de dados. Lance
o dado 100 vezes e armazene os resultados em um vetor. Depois,
monte um outro vetor contendo quantas vezes cada valor foi
obtido. Imprima os dois vetores. Use a função random.randint(1,6)
para gerar números aleatórios, simulando os lançamentos dos
dados.

Exemplo de uma possível saída:
[3,1, 5, 3, 5, 4, 5, 5, 3, 6]
[1,0,3, 1, 4, 1]

"""
import random

lancamentos = []

contagem = [0, 0, 0, 0, 0, 0]

for i in range(100):
    valor = random.randint(1, 6)
    lancamentos.append(valor)
    contagem[valor - 1] += 1

print("Lançamentos:")
print(lancamentos)

print("\nQuantidade de vezes que cada valor apareceu:")
print(contagem)