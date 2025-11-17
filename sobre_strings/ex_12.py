# Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste
# conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

import re # Módulo essencial para manipulação avançada de strings (Regex)

def valida_e_corrige_telefone(numero_original):

    # remove todos os caracteres que não são números
    telefone_limpo = re.sub(r'\D', '', numero_original)
    tamanho = len(telefone_limpo)
    telefone_final = telefone_limpo
    print('\n--- Análise ---')
    print()
    print(f'Telefone fornecido: {numero_original}')
    print(f'Telefone apenas dígitos: {telefone_limpo}')
    print(f'Número de dígitos: {tamanho}')

    if tamanho == 7:
        print('O telefone possui 7 dígitos. Vou acrescentar o dígito três na frente')
        telefone_final = '3' + telefone_limpo
        tamanho = 8

    elif tamanho == 8:
        print('Telefone já possui 8 dígitos')

    else:
        print(f'O número tem {tamanho} dígitos. O padrão não se aplica (7 ou 8 digitos esperados)')
        return f'Inválido: {numero_original}'
    
    if tamanho == 8:
        parte1 = telefone_final[:4]
        parte2 = telefone_final[4:]
        telefone_formatado = f'{parte1}-{parte2}'
        print(f'Telefone corrigido sem formatação: {telefone_final}')
        print(f'Telefone corrigido com formatação: {telefone_formatado}')
        print()

        return telefone_formatado
    
valida_e_corrige_telefone('461-0133')