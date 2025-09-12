# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

def ler_valida_numeros(qtd):

    contador = 1
    numeros = []

    while True:

        try: 

            num = input(f'Insira o {contador}° número: ')
            num_int = int(num)
            numeros.append(num_int)
            contador += 1

            if contador == qtd + 1:

                break

        except ValueError:

            print('\033[1;31mPor favor coloque um número inteiro!')

    return numeros

def soma_quadrado(numeros):

    soma = 0

    for num in numeros:

        soma += num ** 2

    return soma


print(soma_quadrado(ler_valida_numeros(10)))
        