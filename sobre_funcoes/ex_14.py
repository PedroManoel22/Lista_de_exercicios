# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma.
# Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

# 8  3  4
# 1  5  9
# 6  7  2

# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
# Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

# exemplo de matriz que são quadrado mágigos:

# 8  3  4
# 1  5  9
# 6  7  2

# 4  9  2
# 3  5  7
# 8  1  6

# Plus: podemos fazer com que a matriz não tenha números iguais

from random import randint

def gerar_matrizes():

    matriz = [[0, 0, 0],
        [0, 0, 0], 
        [0, 0, 0]]

    for i in range(3):
        for z in range(3):
            x = randint(1, 9)
            matriz[i][z] = x

        return matriz


def valida_matriz(matriz):
    somas_linhas = []
    # soma elementos linhas
    for i in range(3):
        soma_linhas = 0
        soma_linhas += sum(matriz[i])
        somas_linhas.append(soma_linhas)

    somas_colunas = []
    for i in range(3):
        soma_colunas = 0
        for z in range(3):
            soma_colunas += matriz[z][i]
        somas_colunas.append(soma_colunas)

    elementos_diagonal = []
    # soma diagonal
    for i in range(3):
        elementos_diagonal.append(matriz[i][i])

    soma_diagonal = sum(elementos_diagonal)

    #soma diagonal_segundaria
    N = len(matriz) 
    diagonal_secundaria = [matriz[i][N - 1 - i] for i in range(N)]

    soma_diagonal_segundaria = sum(diagonal_secundaria)

    if soma_colunas == soma_linhas and soma_linhas == soma_diagonal and soma_diagonal == soma_diagonal_segundaria:
        print('\033[1;32mA matriz é um quadrado mágico\033[m')
        for i in range(3):
            for z in range(3):
                print(f'{matriz[i][z]} ', end='')
            print()
    
    else:
        print(f'\033[1;31mA matriz não é um quadrado mágico!\033[m')
        cont = 0
        qtd = 2
        gerar_matrizes()
    
            
if __name__ == '__main__':
    matriz = gerar_matrizes()
    valida_matriz(matriz)

