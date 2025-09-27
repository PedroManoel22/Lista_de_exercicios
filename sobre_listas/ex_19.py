# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:

# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro

# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 
# O programa deverá ler os valores até ser informado o valor 0, 
# que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
# Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
# Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. 
# O formato da saída foi dado pela empresa, e é o seguinte:

# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40%

from random import randint

print('Qual o melhor sistema operacional para uso em servidores?')

print()

print('Possíveis respostas são:')
print()

print('''
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
      ''')

votos = []
QUANTIDADE_VOTOS = 20000

sistemas_operacionais = {'Windows Server': 1,
                         'Unix': 2,
                         'Linux': 3,
                         'Netware': 4,
                         'Mac OS': 5,
                         'Outro': 6
                         }


def coleta_votos():
    total_votos = 0
    for i in range(1, QUANTIDADE_VOTOS + 1):

        voto_int = randint(1,6)

        if i == QUANTIDADE_VOTOS + 1:
            voto_int = 0

        if voto_int == 0:
            break

        elif voto_int > 6 or voto_int < 1:
            print('\033[1;31mColoque um número entre 0 a 6!\033[m')

        else:
            votos.append(voto_int)
            total_votos += 1
                
    return contagem_votos_exibir(votos, total_votos)


def contagem_votos_exibir(votos, votos_total):
    votos_nao_repetidos = set(votos)
    
    print(f'{"Sistema Operacional":<20}{"votos":>10}{" %":>10}')
    print('-------------------      -----         ---')
    
    for voto in votos_nao_repetidos:
        total = votos.count(voto)

        if votos_total > 0:
            percentual = (total / votos_total) * 100

        else:
            percentual = 0
        
        for k, v in sistemas_operacionais.items():
            if v == voto:
                print(f'{k:<20}{total:8}{percentual:>15.1f}')
    print('-------------------      -----')

    print(f'Total{votos_total:>23}')

if __name__  == '__main__':
    coleta_votos()
