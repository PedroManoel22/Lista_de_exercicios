# Número por extenso. Escreva um programa que solicite ao usuário a digitação 
# de um número até 99 e imprima-o na tela por extenso.

from num2words import num2words
while True:
    try:
        numero = int(input('Insira um número de 0 a 99: '))
        if numero > 99 or numero < 0:
            print('\033[1;36mPor favor coloque um número entre 0 e 99\033[m')
            continue
        
        break
    
    except ValueError:
        print('\033[1;31mPor favor coloque um número inteiro\033[m')
        
numero_por_extenso = num2words(numero, lang='pt-BR')
print()
print(f'\033[1;32m{numero_por_extenso}\033[m')