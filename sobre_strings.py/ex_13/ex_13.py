# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com
# as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, 
# informando se o usuário ganhou ou perdeu o jogo.

from random import randint, shuffle
def ler_arquivo():
    caminho_arquivo = 'Lista_de_exercicios/sobre_strings.py/ex_13/palavras.txt'
    with open(caminho_arquivo, 'r') as arquivo:
        palavras = arquivo.read().split()
    
    return palavras
    

def escolher_e_embaralhar(palavras):
    tamanho = len(palavras)
    indice = randint(0, tamanho - 1)
    palavra = list(palavras[indice])
    shuffle(palavra)
    return palavra


def adivinhacao(palavra):
    palavra_original = []
    print('A palavra é:')
    for letra in palavra:
        print(f'{letra}', end='')
        palavra_original.append(letra)
    
    cont = 0
    
    # while True:
    #     resposta = input('Tente adivinhar: ')
    print(palavra_original)

    


palavras = ler_arquivo()

adivinhacao(escolher_e_embaralhar(palavras))


