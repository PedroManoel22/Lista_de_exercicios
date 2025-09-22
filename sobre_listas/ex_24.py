# Faça um programa que simule um lançamento de dados. 
# Lance o dado 100 vezes e armazene os resultados em um vetor . 
# Depois, mostre quantas vezes cada valor foi conseguido. 
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

from random import randint
QUANTIDADE_DADOS = 100
numeros = []
qtd = 0
for _ in range(1,QUANTIDADE_DADOS + 1):
    numeros.append(randint(1, 6))
    qtd += 1

for i in range(1, 7):
    if i:
        qtd_num = numeros.count(i)
    print(f'O número {i} apareceu {qtd_num} vezes!')
