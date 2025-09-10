# Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

def coleta_dados_alunos(quantidade_alunos, quantidade_notas):

    alunos = []

    for i in range(1, quantidade_alunos + 1):

        while True:

            nome = input(f'Insira o nome do {i} aluno: ')

            if nome.strip() and not nome.isdigit():

                break

            print('\033[1;31mPor favor insira um nome válido!\033[m')

        notas_validas = []

        for j in range(1, quantidade_notas + 1):

            while True:

                try:
                        
                    nota = float(input(f'Insira a {j}ª nota de {nome}: '))
                            
                    if 0 <= nota <= 10:

                        notas_validas.append(nota)
                        break

                    else:

                        print('\033[1;31mPor favor, insira uma nota entre 0 e 10.\033[m')

                except ValueError:

                    print('\033[1;31mPor favor, coloque um valor numérico válido.\033[m')
    
        aluno_info = {'nome': nome, 'notas': notas_validas}
        alunos.append(aluno_info)

    return alunos



def calcular_media(notas):

    media = 0

    for nota in notas:

        media += nota

    media = media / QUANTIDADE_NOTAS
    return media


def exibir_dados(dados):

    aprovados = 0
    LARGURA = 30
    TITULO = 'Resultado'
    print('-' * LARGURA)
    print(TITULO.center(30))
    print('-' * LARGURA)

    for aluno in dados:

        media = calcular_media(aluno['notas'])
        print(f'O aluno {aluno['nome']} teve as seguintes notas: {aluno['notas']} e ficou com a média de {media:.2f}')

        if media >= 7:

            aprovados += 1
    
    print(f'{aprovados} alunos aprovados')



if __name__ == '__main__':

    QUANTIDADE_ALUNOS = 10
    QUANTIDADE_NOTAS = 4
    lista_alunos = coleta_dados_alunos(QUANTIDADE_ALUNOS, QUANTIDADE_NOTAS)
    exibir_dados(lista_alunos)
          