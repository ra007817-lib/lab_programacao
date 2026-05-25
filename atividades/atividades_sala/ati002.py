"""
o mutiplicador acumulativo probelma:
escreva um progrma peça um neumero inteiro positivo ao usuario
e utilizado um laço for, calcule e mostre o resutado do produto
de todos os numeros impares de 1 ate o numero digitado.
"""

numero = int(input("Digite um número inteiro positivo: "))

produto = 1

for i in range(1, numero + 1):
    if i % 2 != 0:
        produto *= i

print("Resultado do produto dos números ímpares:", produto)