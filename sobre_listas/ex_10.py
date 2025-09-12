# Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor_1 = [1, 3, 5, 7, 9]
vetor_2 = [2, 4, 6, 8, 10]

vetor_3 = []

for i in range(len(vetor_1)):

    vetor_3.append(vetor_1[i])
    vetor_3.append(vetor_2[i])

print(vetor_3)
