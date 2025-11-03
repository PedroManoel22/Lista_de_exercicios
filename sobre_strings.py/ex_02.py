# Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente
# letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.


def obter_nome():
    while True:
        nome = input('Digite seu nome: ').strip() 

        if not nome:
            print(f'\033[1;31mPor favor, coloque um nome (o campo não pode ser vazio)!\033[m')
            continue

        if nome.isdigit():
            print(f'\033[1;33m ⚠️  Entrada inválida: O nome não pode ser um número puro. Tente novamente.\033[m')
            continue 

        return nome


def nome_ao_contrario(nome):
    print(f'{nome[::-1].upper()}')


nome_validado = obter_nome()
nome_ao_contrario(nome_validado)
