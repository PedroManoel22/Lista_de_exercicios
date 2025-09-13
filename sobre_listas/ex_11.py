# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor_1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
vetor_2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
vetor_3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

vetor_4 = []

for i in range(len(vetor_1)):

    vetor_4.append(vetor_1[i])
    vetor_4.append(vetor_2[i])
    vetor_4.append(vetor_3[i])

print(vetor_4)