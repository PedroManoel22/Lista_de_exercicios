# Jogo de Craps. 
# Faça um programa que implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
# Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, 
# isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". 
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, 
# no entanto, se tirar um 7 antes de tirar este Ponto novamente.

from random import randint
from time import sleep

def primeira_jogada():
    ganhou = [7, 11]
    perdeu = [2, 3, 12]
    ponto = [4, 5, 6, 8, 9, 10]
                
    while True:
        x = input('Aperte enter para jogar os dados: ')
        if x == '': # enter foi apertado
                print()
                print('Jogando o primeiro dado...')
                print()
                sleep(1)
                num1 = randint(1, 6)
                print(num1)
                print()
                print('Jogando o segundo dado...')
                print()
                sleep(1)
                num2 = randint(1, 6)
                print(num2)
                soma = num1 + num2
              
                if soma in ganhou:
                    return ganhar()

                elif soma in perdeu:
                    return perder()

                if soma in ponto:
                    x = soma
                    return continuar(x)

    
        else:
            print('\033[1;31mPor favor aperte enter para jogar\033[m')


def ganhar():
    print('\n\033[1;32mNATUTRAL\033[m\n'
          'Parabéns você ganhou!\n'
          'Obrigado por jogar')


def perder():
    print('\n\033[1;31mCRAPS\033[m\n'
          'Você perdeu!\n'
          'Obrigado por jogar')


def continuar(num_acertar):
    print(f'\n\033[1;36mPONTO: {num_acertar}\033[m')
    print('Continue jogando....\n')

    while True:
        x = input('\nAperte enter para jogar os dados: ')

        if x == '': # enter foi apertado
            print()
            print('Jogando o primeiro dado...')
            sleep(1)
            num1 = randint(1, 6)
            print()
            print(num1)
            print()
            print('Jogando o segundo dado...')
            sleep(1)
            num2 = randint(1, 6)
            print()
            print(num2)
            soma = num1 + num2

        else:
             print('\033[1;31mPor favor aperte enter para jogar\033[m')

        if soma == 7:
             print('\033[1;31mPerdeu Playboy\033[m')
             break
        
        elif soma == num_acertar:
             print('\033[1;32mParabéns você ganhou!\033[m')
             break
        
    print()
    print('Obrigado por jogar')


if __name__ == '__main__':
    primeira_jogada()
