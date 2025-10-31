# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

string1 = 'Brasil Hexa 2006'
string2 = 'Brasil! Hexa 2006!'
tamanho_str1 = len(string1)
tamanho_str2 = len(string2)

print(f'Tamanho de "{string1}": {tamanho_str1} caracteres\n'
      f'tamanho de "{string2}": {tamanho_str2} caracteres')

if tamanho_str1 == tamanho_str2:
    print('As duas strings são de tamanhos iguais.')

else:
    print('As duas strings são de tamanhos diferentes.')

if string1 in string2:
    print('As duas strings possuem conteúdo igual.')

else:
    print('As duas strings possuem conteúdo diferente.')
