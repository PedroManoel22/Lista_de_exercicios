# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado~

def qtd_digitos(num):
    num_str = str(num)
    return f'O número \033[1;36m{num}\033[m tem {len(num_str)} dígitos'

if __name__ == '__main__':
    while True:
        try:
            x = int(input('Informe um número inteiro: '))
            print(qtd_digitos(x))
            break

        except ValueError:
            print('\033[1;31mPor favor coloque um número inteiro!\033[m')
