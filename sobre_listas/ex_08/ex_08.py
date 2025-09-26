# Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.

import json


def dados_pessoas(qtd):
    
    cont = 1
    dados = []

    while True:
        dado_pessoa = []

        try:

            idade = input(f'Idade da {cont}° pessoa: ')
            idade_int = int(idade)
            altura = input(f'Altura da {cont}° pessoa: ')
            altura_float = float(altura)
            dado_pessoa.append(idade_int)
            dado_pessoa.append(altura_float)
            dados.append(dado_pessoa)
            cont += 1
            if cont == qtd + 1:

                break

        except ValueError:

            print('\033[1;31mPor favor coloque uma idade válida!\033[m')
        
        
    salvar(dados, CAMINHO_ARQUIVO)
    return dados[::-1]

def ler(dados, caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo: # ler o arquivo
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('\033[1;31mArquivo não existe\033[m')
        salvar(dados, caminho_arquivo)
    return dados



def salvar(dados, caminho_arquivo):
    dado = dados
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
            dado = json.dump(dados,arquivo,indent=2, ensure_ascii=False)
    return dado



CAMINHO_ARQUIVO = 'C:\\Users\\Pedro\\Documents\\GitHub\\lista_de_exercicios\\Lista_de_exercicios\\sobre_listas\\ex_08\\json_ex08'
ler(dados_pessoas(5), CAMINHO_ARQUIVO)
