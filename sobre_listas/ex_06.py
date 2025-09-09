# Importa a biblioteca 'typing' para tipagem de dados, o que é uma boa prática
# para projetos maiores e facilita a leitura do código.
from typing import List, Dict

# 1. Função para coletar nomes e notas. É a mais importante.
def coleta_dados_alunos(quantidade_alunos: int, quantidade_notas: int) -> List[Dict]:

    alunos = []
    
    for i in range(quantidade_alunos):
       
        while True:

            nome = input(f'Insira o nome do {i+1}º aluno: ')

            if nome.strip() and not nome.isdigit():

                break

            print('Por favor, insira um nome válido.')
            
        notas_validas = []

        for j in range(quantidade_notas):

            while True:

                try:
                   
                    nota = float(input(f'Insira a {j+1}ª nota de {nome}: '))
                    
                    if 0 <= nota <= 10:

                        notas_validas.append(nota)
                        break

                    else:

                        print('Por favor, insira uma nota entre 0 e 10.')

                except ValueError:

                    print('Por favor, coloque um valor numérico válido.')
        
        aluno_info = {'nome': nome, 'notas': notas_validas}
        alunos.append(aluno_info)
        
    return alunos

# 2. Função para calcular a média das notas
def calcula_media(notas: List[float]) -> float:
    """
    Calcula a média de uma lista de notas.
    """
    # Evita divisão por zero
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

# 3. Função para imprimir o resultado e contar os aprovados
def exibe_resultados(alunos: List[Dict]):
    """
    Itera sobre a lista de alunos, calcula as médias e exibe o resultado final.
    """
    aprovados = 0
    print('\n--- Resultados ---')
    for aluno in alunos:
        media = calcula_media(aluno['notas'])
        print(f"O aluno {aluno['nome']} tem a média de {media:.2f}")
        
        if media >= 7.0:
            aprovados += 1
    
    print(f"\n{aprovados} aluno(s) com média igual ou superior a 7.0.")

# Bloco principal para executar o programa
if __name__ == '__main__':
    QUANTIDADE_ALUNOS = 2
    QUANTIDADE_NOTAS = 2
    
    # Apenas uma chamada de função para coletar todos os dados
    lista_de_alunos = coleta_dados_alunos(QUANTIDADE_ALUNOS, QUANTIDADE_NOTAS)
    
    # Chama a função que exibe os resultados
    exibe_resultados(lista_de_alunos)
