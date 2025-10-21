# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
# Plus: só receba numeros inteiros


def coleta_numeros():
    loop = 0
    QTD = 3
    numeros = []
    while True:
        try:
            x = input('Insira um número: ')
            x_int = int(x)
            loop += 1
            numeros.append(x_int)

            if loop == QTD:
                break

        except ValueError:
            print('\033[1;31mPor favor coloque um número inteiro!\033[m')
        
        except Exception as e:
            print(f'\033[1;36mError inesperado! {e}\033[m')

    return numeros


def soma(x, y, z):
    soma = x + y + z
    
    return f'A soma entre {x} + {y} + {z} = {soma}'

if __name__ == '__main__':
    numeros = coleta_numeros()
    print(soma(*numeros))
