# Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto
# e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!

# Digite uma letra: O
# A palavra é: _ _ _ _ O

# Digite uma letra: E
# A palavra é: _ E _ _ O

# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!

from random import randint

def ler_arquivo():
    caminho_arquivo = 'Lista_de_exercicios/sobre_strings.py/ex_11/palavras.txt'
    with open(caminho_arquivo, 'r') as arquivo:
        palavras = arquivo.read().split()
    
    return palavras


def escolhe_palavra(palavras):
    tamanho = len(palavras)
    escolhido = randint(0, tamanho - 1)

    return palavras[escolhido]


def comecar_jogo(palavra_escolhida):
    tamanho_palavra = len(palavra_escolhida)
    palavra_escolhida  = palavra_escolhida.lower()
    caracteres =  ['_ '] * tamanho_palavra
    palavra_formada = ''
    cont = 0
    letras_ja_escolhidas = []


    while True:
        letra = input('Digite uma letra: ').lower()

        # verifica se a letra escolhida é repetida
        if letra not in letras_ja_escolhidas:
            letras_ja_escolhidas.append(letra)
        else:
            print()
            print(f'\033[1;36m{letra} já foi escolhida, tente outra\033[m')
            print()
            continue

        # verifica se a variável "letra" tem mais de um caractere
        if len(letra) > 1:
            print()
            print('\033[1;31mPor favor insira um letra de cada vez!\033[m')
            print()
            continue

        # verifica se a variável "letra" é um número
        elif letra.isdigit():
            print()
            print('\033[1;31mInsira uma letra e não número\033[m')
            print()
            continue
        
        #verifica se a variável "letra" está vazia
        elif not letra:
            print()
            print('\033[1;31mInsira uma letra!\033[m')
            print()
            continue
        
        # verifica se a letra que o usuário digitou está na palavra_escolhida
        elif letra in palavra_escolhida:
            print('A palavra é: ', end='')

            for i in range(tamanho_palavra):
                if letra == palavra_escolhida[i]:
                    caracteres[i] = letra
                    palavra_formada += letra
            for caractere in caracteres:
                print(f'{caractere}', end='')
            
            print()

            if sorted(palavra_formada) == sorted(palavra_escolhida):
                print()
                print('\033[1;32mParabéns você ganhou\033[m')
                print()
                break
        
        # caso o usuário não acerte a letra 
        else:
            cont += 1
            print(f'\033[1;31mVocê errou pela {cont}ª vez, tente novamente!\033[m')
            if cont == 6:
                print()
                print('\033[1;31mVocê perdeu!\033[m')
                print()
                break
            
                      
if __name__ == '__main__':
    ler_palavras = ler_arquivo()
    palavra = escolhe_palavra(ler_palavras)
    comecar_jogo(palavra)
