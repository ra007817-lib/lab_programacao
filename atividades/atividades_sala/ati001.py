"""
o valor de intervalo problama:
faça um programa que leia um numero do teclado e verrifique se ele está dentro 
do intervalo entre 10 e 50 (inclusive). se estiver, exiba "dado valido".
caso contrário, exiba "dado invalido". atenta-se para que o progrma respita esse validação
ate que o usuario digite um numero 0 para sair.
"""

while True:
    numero = int(input("Digite um numero: "))
    if numero == 0:
        print("Saindo do programa...")
        break
    elif 10 <= numero <= 50:
        print("Dado valido.")
    else:
        print("Dado invalido.")