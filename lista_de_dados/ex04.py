# Calcule as principais estatísticas descritivas do salário: 
# mínimo, 1o quartil, média, mediana, 3o quartíl, máximo e desvio padrão

from data import data
import numpy as np
from ex01 import media_salarios


salarios: list[float] = []

# percorre lista
for d in data:
    # pecorre os dicionários
    for k, v in d.items():
        if k == "salario":
            salarios.append(float(v))
    
# soma_salarios = sum(salario)

# Mímino

minimo = np.min(salarios)
print(f"\nO valor do menor salário é R${minimo:.2f}")

# Máximo

maximo = np.max(salarios)
print(f"\nO valor do maior salário é R${maximo:.2f}")

# Média

print(f"\nA média salarial é de ${media_salarios:.2f}\n")
