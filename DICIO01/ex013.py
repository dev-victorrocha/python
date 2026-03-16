turma = {
    'Matheus': [10, 4, 6],
    'Bernardo': [6.7, 8, 2],
    'Victor': [5, 7, 9],
    'Pedrin': [0, 5, 1]
}
situação = 'Reprovado'

for aluno in turma:
    media = sum(turma[aluno])/3
    if media >= 6:
        situação = 'Aprovado'
    else:
        situação = 'Reprovado'
    print(f'{aluno} - Média: {media:.2f} - Situação: {situação}')