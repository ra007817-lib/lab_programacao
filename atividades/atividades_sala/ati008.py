"""
sem usar o comando .split() nativo do python, faça um programa que 
receba uma frase curta separada por espaço (ex ["banco de dados"])
e trasnforma cada plavra em um elemento de um vetor (ex: ["banco","de","dados"]).
"""


frase = input("Digite uma frase: ")

vetor = []
palavra = ""

for caractere in frase:
    if caractere != " ":
        palavra += caractere
    else:
        if palavra != "":
            vetor.append(palavra)
            palavra = ""

if palavra != "":
    vetor.append(palavra)

print(vetor)