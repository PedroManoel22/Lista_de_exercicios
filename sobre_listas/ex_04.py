# Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

def valida(tamanho):

    global frase

    while True:

        frase = input('Insira sua frase de 10 caracteres: ').lower()

        if len(frase) < 10 or len(frase) > 10:

            print('\033[1;31mPor favor insira uma frase de 10 caracteres!\033[m')
            continue
        else:

            break
    
    return frase

def conta_consoantes(frase):

    global consoantes
    consoantes = 0

    for letra in frase:

        if letra not in 'aeiou':

            consoantes += 1
    
    return consoantes

if __name__ == '__main__':

    TAMANHO_VETOR = 10

    valida(TAMANHO_VETOR)
    conta_consoantes(frase)
    print(f'na frase: "{frase}" temos {consoantes} consoantes')
