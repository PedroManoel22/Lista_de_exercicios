# Faça um programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores

def valida_coleta_int(ordem):

    global numeros
    numeros = []

    for i in range(1, ordem + 1):
        while True:

            try:

                num = input(f'Insira o {i}° número: ')
                num_int = int(num)
                numeros.append(num_int)
                
                break

            except ValueError:

                print('\033[1;31mPor favor insira um número inteiro!\033[m')

    return numeros


def pares_impares(nums):

    global pares
    global impares
    pares = []
    impares = []

    for num in nums:

        if num % 2 == 0:

            pares.append(num)
        
        else:

            impares.append(num)

    return pares, impares


if __name__ == '__main__':

    QUANTIDADE_NUMEROS = 20

    valida_coleta_int(QUANTIDADE_NUMEROS)
    pares_impares(numeros)
    print(f'Números: {numeros}')
    print(f'Pares: {pares}')
    print(f'Ímpares: {impares}')
