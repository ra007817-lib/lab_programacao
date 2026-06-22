"""
faça uma função que informe o status do aluno a partir da sua mediaide 
de acordo com a tebala a serguir
-nota acima de 6 = "aprovado"
-nota antre 4 e 6 = "verificção suplementar"
-nota abixo de 4 = "reprovado"
"""

def nota_status_aluno(nota):
    if nota > 6:
        print("Aprovado")
    elif 4 <= nota <= 6:
        print("Verefição Suplementar")
    else:
        print("Reprovado")


nota = int(input("qual é a nota do aluno:"))
nota_status_aluno(nota)




