# Qual a quantidade de colunas do DataFrame
from data import data 

number_of_columns: int = 0

for d in data:
    number_of_columns = len(d)

    break

print(f"\nO número de colunas é: {number_of_columns}\n")