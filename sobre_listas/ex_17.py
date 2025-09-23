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


def dados():
    atletas = []
    qtd_atleta = 0

    while True:
        
        nome = input('Insira um nome: ')

        if nome.isnumeric():
            print('\033[1;31mfavor coloque um nome!\033[m')
            continue
        
        if not nome:
            break
        
        else:
            atleta = {}
            saltos = []
            atleta['nome'] = nome
            qtd_atleta += 1
            print(f'atleta: {nome}')
           
           # Pegar saltos
            for i in range(1, QUANTIDADE_SALTOS + 1):
                while True:
                    try:
                        salto = input(f'Insira a {i}° distância: ')
                        salto_int = int(salto)
                        saltos.append(salto_int)
                        atleta['saltos'] = saltos
                        break

                    except ValueError:
                        print('\033[1;31mPor favor coloque uma distância válida\033[m')
            atletas.append(atleta)

    
    return atletas


def exibir_dados(dados):
    print()
    print('Resultado Final:')
    print()
    if not dados:
        print('Nenhum atleta registrado!')
    for dado in dados:
        print(f'Atleta: {dado['nome']}')
        saltos_str = ' - '.join(map(str, dado['saltos']))
        print(f'Saltos: {saltos_str}')
        media = sum(dado['saltos']) / QUANTIDADE_SALTOS
        print(f'Média: {media}m')
        print()
    

if __name__ == '__main__':
    QUANTIDADE_SALTOS = 5
    exibir_dados(dados())
