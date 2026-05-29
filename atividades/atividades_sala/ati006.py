"""
faça um progrma que leia 5 nomes e os armazane em uma lista. em segida, 
o progrma deve criar uma segunda lista contedno os mesmo nome, mas na ordem inversa
(o utimo nome lido deva ser primeiro da nava lista ). imprima ambos

"""
nomes = []

for i in range(5):
    nome = input(f"Digite o {i + 1}º nome: ")
    nomes.append(nome)

nomes_invertidos = nomes[::-1]

print("Lista original:")
print(nomes)
print("Lista invertida:")
print(nomes_invertidos)