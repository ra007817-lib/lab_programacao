"""
peça para o usuario ditar uma palavra. o progrma deve percorrer a string
caracter por carter econtar quantas vogas (a, e,i,o,u) exita na palavra.
"""

palavra = input("Digite uma palavra: ").lower()

vogais = "aeiou"
contador = 0

for letra in palavra:
    if letra in vogais:
        contador += 1

print("Quantidade de vogais:", contador)