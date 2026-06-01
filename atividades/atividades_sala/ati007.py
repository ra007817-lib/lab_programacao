"""
elabore um progrma que leia 10 numeros inteiros do tecaldo. amedida que os 
neumros foem lidos, os pares devem ser inserisdos em uma lista chamada
pares e os impares em uma lista chamada impares. porem,se o usuario
digitar um numero que ja foi iserido anteriormante em qualquer uma das listas,
o progrma deve recusar o numero e pedir para digitar outro nemero.
"""

pares = []
impares = []

while len(pares) + len(impares) < 10:
    numero = int(input("Digite um número inteiro: "))

    if numero in pares or numero in impares:
        print("Número já informado! Digite outro.")
        continue
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\nLista de pares:", pares)
print("Lista de ímpares:", impares)