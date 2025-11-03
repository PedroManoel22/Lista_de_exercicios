# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.



def valida_frase():
     while True:
        frase = input('Insira uma frase: ').lower()

        if not frase:
            print('\033[1;31mPor favor coloque uma frase (o campo não pode ser vazio)\033[m')
            continue
        
        if frase.isdigit():
            print(f'\033[1;33m ⚠️  Entrada inválida: A frase não pode ser um número puro. Tente novamente.\033[m')
            continue

        return frase

def conta_vogais_espacos(frase):
    vogais = ['a', 'e', 'i', 'o', 'u']
    cont_vogais = 0
    cont_espacos = 0

    for letra in frase:
        if letra in vogais:
            cont_vogais += 1

        if letra == ' ':
            cont_espacos += 1
    return (f'Existem {cont_espacos} espaços em branco na sua frase!\n'
            f'Apareceram {cont_vogais} vogais na sua frase!')


if __name__  == '__main__':
    frase_valida = valida_frase()
    print(conta_vogais_espacos(frase_valida))
    

    
