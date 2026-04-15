# Qual o valor do salário médio?

from data import data
import numpy as np


salarios: list[float] = []

for d in data:
    for k, v in d.items():
        if k == "salario":
            salarios.append(float(v))


media_salarios = np.mean(salarios)
print(f"\nA média dos salários é: R${media_salarios:.2f}\n")        
