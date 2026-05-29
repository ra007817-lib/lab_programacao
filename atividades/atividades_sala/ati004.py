"""
crie um progrma que preeecha uma lista com as notas de 5 alunos (valores
lidos di teclado). em seguida,o progrma deva remover a menor nota da listta utilizado
comondos de vert e exibir as notas restantes na tela
"""

notas = []

for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

menor_nota = min(notas)

notas.remove(menor_nota)

print("Notas restantes:")
for nota in notas:
    print(nota)