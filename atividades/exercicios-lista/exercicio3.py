"""
Faça um programa que percorre duas listas e intercala os 
elementos de ambas, formando uma terceira lista.
a terceira lista deva começar pelo primeiro elemento da lista menor.
exmplo: 
lista1 = [1, 2,3,4]
lista2 = [10,20,30,40,50,60]
lista_intercalada = [1,10,2,20,3,30,4,40,50,60]
"""

lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40, 50, 60]

if len(lista1) > len(lista2):
    lista1, lista2 = lista2, lista1

lista_intercalada = []

for i in range(len(lista1)):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])


lista_intercalada.extend(lista2[len(lista1):])

print(lista_intercalada)