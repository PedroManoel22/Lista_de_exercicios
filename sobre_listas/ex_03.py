# Faça um programa que leia 4 notas, mostre as notas e a média na tela.

def validar_notas(ordem):

    while True:

        try:

            nota = input(f'Insira a {ordem}° nota: ')
            nota_int_float = float(nota) or int(nota)

            if nota_int_float > 10 or nota_int_float < 0:

                print('\033[1;33mPor favor coloque um nota entre 0 a 10!\033[m')
                continue

            return nota_int_float

        except ValueError:

            print('\033[1;31mPor favor coloque uma nota válida\033[m')

def coletar_notas(quantidade):

    global notas    
    notas = []

    for i in range(1, quantidade + 1):

        notas.append(validar_notas(i))

    return notas

if __name__  == '__main__':

    QUANTIDADE_NOTAS = 4 # variavel constante 

    notas_coletadas = coletar_notas(QUANTIDADE_NOTAS)

    print(f'Notas: {notas_coletadas}')
    media = sum(notas) / QUANTIDADE_NOTAS

    print(f'Média: {media:.2f}') 
        