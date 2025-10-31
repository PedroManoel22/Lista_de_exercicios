from random import randint

matriz = [[0, 0, 0],
           [0, 0, 0], 
           [0, 0, 0]]

for i in range(3):
    for z in range(3):
        x = randint(1, 9)
        matriz[i][z] = x


for i in range(3):
    for z in range(3):
        print(f'{matriz[i][z]} ', end='')
    print()
print(matriz)


    