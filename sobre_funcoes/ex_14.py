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

def gerar_matrizes() ->  list[list[int]]:

    matriz = [[0, 0, 0],
        [0, 0, 0], 
        [0, 0, 0]]

    for i in range(3):
        for z in range(3):
            x = randint(1, 9)
            matriz[i][z] = x

    return matriz


def valida_matriz(matriz: list[list[int]]):
    somas_linhas: list[int] = []
    somas_colunas: list[int] = []
    elementos_diagonal: list[int] = []
    soma_linhas: int = 0
    soma_colunas: int = 0

    # soma elementos linhas
    for i in range(3):
        soma_linhas += sum(matriz[i])
        somas_linhas.append(soma_linhas)

    for i in range(3):
        for z in range(3):
            soma_colunas += matriz[z][i]
        somas_colunas.append(soma_colunas)


    # soma diagonal
    for i in range(3):
        elementos_diagonal.append(matriz[i][i])

    soma_diagonal = sum(elementos_diagonal)

    # soma diagonal_segundaria
    N = len(matriz) 
    diagonal_secundaria = [matriz[i][N - 1 - i] for i in range(N)]

    soma_diagonal_segundaria = sum(diagonal_secundaria)

    soma_linhas = int(soma_linhas / 3)
    soma_colunas = int(soma_colunas / 3)

    if len({soma_linhas, soma_colunas, soma_diagonal, soma_diagonal_segundaria}) == 1:
        print('\033[1;32mA matriz é um quadrado mágico\033[m')
        for i in range(3):
            for z in range(3):
                print(f'{matriz[i][z]} ', end='')
            print()
    
    else:
        print(f'\033[1;31mA matriz não é um quadrado mágico!\033[m')
        # cont = 0
        # qtd = 2
        gerar_matrizes()
           
            
if __name__ == '__main__':
    matriz = gerar_matrizes()

    matriz = [[8, 1, 6],
              [3, 5, 7], 
              [4, 9, 2]] # quadrado mágico
    
    valida_matriz(matriz)

