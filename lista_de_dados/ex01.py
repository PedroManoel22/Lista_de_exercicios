# Qual o valor do salário médio?

import numpy as np
from data import data

salarios: list[float] = []

for d in data:
    for k, v in d.items():
        if k == "salario":
            salarios.append(float(v))


media_salarios: float = np.mean(salarios)  # type: ignore
print(f"\nA média dos salários é: R${media_salarios:.2f}\n")
