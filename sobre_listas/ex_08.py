# Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.


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
        
        
    
    return dados[::-1]



print(dados_pessoas(5))
