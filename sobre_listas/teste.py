from typing import Dict, List

def coleta_dados_alunos(quantidade_alunos: int, quantidade_notas: int) -> List[Dict]:

    alunos = []

    for i in range(1, quantidade_alunos + 1):

        nome = input(f'Insira o nome do {i} aluno: ')

        if nome.strip() and not nome.isdigit():

            break

        print('\033[mPor favor insira um nome válido!\033[m')

        notas_validas = []

        for j in range(1, quantidade_notas + 1):

            while True:

                try:
                        
                    nota = float(input(f'Insira a {j+1}ª nota de {nome}: '))
                            
                    if 0 <= nota <= 10:

                        notas_validas.append(nota)
                        break

                    else:

                        print('\033[1;31mPor favor, insira uma nota entre 0 e 10.\033[m')

                except ValueError:

                    print('\033[1;31mPor favor, coloque um valor numérico válido.\033[m')




            