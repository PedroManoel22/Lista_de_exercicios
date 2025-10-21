# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere P, se seu argumento 
# for positivo, e N, se seu argumento for zero ou negativo.

def valida_numero():
    while True:
        try:
            x = input('Insira um número inteiro: ')
            x_int = int(x)
            return positivo_negativo(x_int)
        
        except ValueError:
            print('\033[1;31mPor favor coloque um número inteiro!\033[m')
        
        except Exception as e:
            print(f'Erro inesperado! {e}')


def positivo_negativo(x):
    if x > 0:
        return 'P'
    else:
        return 'N'


if __name__ == '__main__':
    print(valida_numero())
    