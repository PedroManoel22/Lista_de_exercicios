import re

padrao_num_conta = re.compile(r'\d{8}-\d{2}')
x = input('Coloque o numero da contya: ')
valido = padrao_num_conta.findall(x)
if valido:
    print('válido')
else:
    print('inválido')
print(valido)