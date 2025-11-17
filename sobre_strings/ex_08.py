# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: 
# OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase 
# palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

def valida_frase():
    while True:
        frase = input('Insira uma frase: ').lower().replace(' ', '')

        if not frase:
            print('\033[1;31mPor favor coloque uma frase (o campo não pode ser vazio)\033[m')
            continue
        
        if frase.isdigit():
            print(f'\033[1;33m ⚠️  Entrada inválida: A frase não pode ser um número puro. Tente novamente.\033[m')
            continue

        return frase

def e_palindromo(frase):
    frase_ao_contrario = frase[::-1]

    if frase_ao_contrario == frase:
        print(f'\033[1;32mA frase é um palíndromo!\033[m')

    else:
        print(f'\033[1;31mA frase não é um palíndromo!\033[m')


if __name__ == '__main__':
    frase_valida = valida_frase()
    e_palindromo(frase_valida)

