# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
# O resultado do atleta será determinado pela média dos cinco valores restantes. 
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome,
# os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. 
# A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m



# temos que corrigir este exercicio, devemos fazer uma unica função para pedir os dados dos atletas
QUANTIDADE = 5
def pedir_nomes():

    nomes = []
    qtd_atleta = 0
    while True:
        
        nome = input('Insira um nome: ')

        if nome.isnumeric():

            print('favor coloque um nome!')
        
        if not nome:

            return exibir_dados(nomes, saltos(QUANTIDADE, nome))
        
        else:

            nomes.append(nome)
            qtd_atleta += 1
            return saltos(2, nomes, qtd_atleta)


def saltos(qtd_saltos,nome, atleta):

    distancias_saltos = []
    print('Atleta: ', end='')
    print(nome[atleta-1])
    for i in range(1, qtd_saltos + 1):

        dado = []
        while True:

            try:

                saltos = input(f'Insira o {i}° salto: ')
                saltos = float(saltos)
                dado.append(saltos)
                break
                
            except ValueError:

                print('\033[1;31mPor favor coloque uma distância válida!\033[m')
    distancias_saltos.append(dado)         
    return pedir_nomes()


def exibir_dados(nomes, saltos):

    print(nomes)
    print(saltos)



print(pedir_nomes())
