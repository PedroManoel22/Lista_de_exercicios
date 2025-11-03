# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

# F
# U
# L
# A
# N
# O

def valida_nome():
    while True:
        nome = input('Insira seu nome: ')

        if not nome:
            print('\033[1;31mPor favor coloque um nome (o campo não pode ser vazio)\033[m')
            continue
        
        if nome.isdigit():
            print(f'\033[1;33m ⚠️  Entrada inválida: O nome não pode ser um número puro. Tente novamente.\033[m')
            continue

        return nome

def imprime_nome_vertical(nome):
    print('\nNome na vertical:\n')
    for letra in nome:
        print(letra)

if __name__ == '__main__':
    nome_valido = valida_nome()
    imprime_nome_vertical(nome_valido)
