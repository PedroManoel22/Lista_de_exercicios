# Foram anotadas as idades e alturas de 30 alunos. 
# Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
from random import randint, uniform
from pprint import pprint

dados_alunos = [{'idade': randint(10, 18), 'altura': round(uniform(1.60, 2.00), 2)} for _ in range(30)]

media = sum([aluno['altura'] for aluno in dados_alunos])
media = media / len(dados_alunos)
qtd_aluno_maior = len([aluno for aluno in dados_alunos if aluno['idade'] > 13 and aluno['altura'] < media])


print('Alunos:')
pprint(dados_alunos)
print(f'Altura média: {media:.2f}')

print(f'Quantidade de aluno maiores de 13 anos e com menos de {media:.2f} de altura {qtd_aluno_maior}')
