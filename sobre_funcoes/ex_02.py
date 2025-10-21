# Faça um programa para imprimir:

# 1
# 1   2
# 1   2   3
# .....
# 1   2   3   ...  n
# Para um n informado pelo usuário. Use uma função que receba um valor n inteiro, imprima até a n-ésima linha.

def imprimir(n):
    for i in range(1, n + 1):
        for z in range(1, i + 1):
            print(f'{z} ', end='')
        print()


try:
    x = input('Insira um número: ')
    x_int = int(x)
    
except ValueError:
    print('Insira número inteiro!')

except Exception as e:
    print(f'Error inesperado! {e}')

if __name__ == '__main__':
    imprimir(x_int)
    