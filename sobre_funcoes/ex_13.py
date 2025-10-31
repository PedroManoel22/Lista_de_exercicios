# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. 
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20.
# Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

def recebe_linha_colunas():
    #Valida o número de linhas
    while True:
        try:
            linha = int(input('Insira o número de linhas: '))
            if linha < 1:
                linha = 1
                print('O valor mínimo de linha é 1, como você colocou menos, vou considerar como 1')
            
            elif linha > 20:
                linha = 20
                print('O valor máximo de linha é de 20, como você colocou a mais, vou considerar como 20')
            break
        except ValueError:
            print(f'\033[1;31mPor favor insira um valor do tipo int\033[m')
        
        except Exception as e:
            print(f'Erro inesperado, {e.__name__}')
    

    #Valida o número de colunas
    while True:
        try:
            coluna = int(input('Insira o número de colunas: '))
            if coluna < 1:
                coluna = 1
                print('O valor mínimo de coluna é 1, como você colocou menos, vou considerar como 1')
            
            elif coluna > 20:
                coluna = 20
                print('O valor máximo de coluna é de 20, como você colocou a mais, vou considerar como 20')
            break
        except ValueError:
            print(f'\033[1;31mPor favor insira um valor do tipo int\033[m')
        
        except Exception as e:
            print(f'Erro inesperado, {e.__name__}')

    return linha, coluna


def valida_carcteres():
    caracteres = ['+', '-', '|']
    while True:
        caractere = input('Insira qual caractere você quer para seu retângulo: ["+", "-" e "|"]: ')

        if caractere not in caracteres:
            print('\033[1;31mColoque um caractere válido!\033[m')

        else:
            break
    
    return caractere


def printar_retangulo(linha, coluna, caractere):
    if linha == coluna:
        print('Você me deu dois valores iguais com isso vamos ter um quadrado, por isso irei tirar 1 de linha ')
        linha -= 1

    for _ in range(linha):
        print(caractere, end=' ')
        for _ in range(coluna-1):
            print(caractere, end=' ')
        print()
        


if __name__ == '__main__':
    linhas_colunas = recebe_linha_colunas()
    caractere = valida_carcteres()
    printar_retangulo(*linhas_colunas, caractere)
            