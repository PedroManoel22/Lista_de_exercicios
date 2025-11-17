# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com
# as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, 
# informando se o usuário ganhou ou perdeu o jogo.

from random import randint, shuffle

def ler_arquivo():
    caminho_arquivo = 'sobre_strings.py/ex_13/palavras.txt'
    with open(caminho_arquivo, 'r') as arquivo:
        palavras = arquivo.read().split()
    
    return palavras
    

def escolher_e_embaralhar(palavras):
    tamanho = len(palavras)
    indice = randint(0, tamanho - 1)
    palavra = palavras[indice]
    palavra_embaralhada = list(palavras[indice])
    shuffle(palavra_embaralhada)

    return adivinhacao(palavra_embaralhada, palavra)


def adivinhacao(palavra_embaralhada, palavra):
    palavra_original = []
    print('A palavra é:')
    for letra in palavra_embaralhada:
        palavra_original.append(letra)
        print(f'{letra}', end='')
    print()
    print(palavra)
    
    cont = 0

    while True:
        resposta = input('Tente adivinhar: ')

        if resposta == palavra:
            print('\033[1;32mParabéns você acertou a palavra!\033[m')
            break

        else:
            cont += 1
            if cont != 6:
                print(f'\033[1;31mErrou, tente novamente, você tem mais {6 - cont} tentativas....\033[m')
            else:
                break
    
    return f'Obrigado e volte sempre!'


if __name__ == '__main__':
    ler = ler_arquivo()
    print(escolher_e_embaralhar(ler))

