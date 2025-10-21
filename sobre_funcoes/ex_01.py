# Faça um programa para imprimir:

# 1
# 2   2
# 3   3   3
# .....
# n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def imprimir():
    while True:
        try:
            n = input('Insira um número: ')
            n_int = int(n)
            
            for i in range(1, n_int + 1):
                for z in range(i):
                    print(f'{i} ', end='')
                print()
                
            break

        except ValueError:
            print('\033[1;31mPor favor coloque um número inteiro\033[m')
            
        except Exception as e:
            print(f'ERRO inesperado: {e}')


if __name__ == '__main__':
    imprimir()
