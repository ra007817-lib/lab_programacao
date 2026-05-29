"""
preeecha uma lista com 6 nuemros inteiros informando pelo usuario. depois,
peça para ele digitar um nemero x. o progrma deve usar metodos de lista pra informar
quantas vezes x aparsce na lista e,se aparser qual e o indece da primeira ocorrecia
"""

numeros = []

for i in range(6):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

x = int(input("Digite o número X: "))

quantidade = numeros.count(x)

if quantidade > 0:
    indice = numeros.index(x)
    print(f"O número {x} aparece {quantidade} vez(es) na lista.")
    print(f"A primeira ocorrência está no índice {indice}.")
else:
    print(f"O número {x} não aparece na lista.")