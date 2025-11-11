# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.

# O arquivo de entrada possui o seguinte formato:

# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256

# O arquivo de saída possui o seguinte formato:

# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4
# 9.8.234.5

# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 192.168.0.256

import re

caminho_arquivo = 'Lista_de_exercicios/sobre_arquivos/ex_01/ex_01/enderecos_IP.txt'

def ler_arquivo():
    with open(caminho_arquivo, 'r') as arquivo:
        enderecos = arquivo.read().split()
    return enderecos


OCTETO_VALIDO = r'(?:25[0-5]|2[0-4]\d|1\d{2}|\d{1,2})'

def validar_ipv4_corrigido(ip_string):
    validos = []
    invalidos = []

    padrao = re.compile(
    r'^' +
    r'(' + OCTETO_VALIDO + r')\.' +
    r'(' + OCTETO_VALIDO + r')\.' +
    r'(' + OCTETO_VALIDO + r')\.' +
    r'(' + OCTETO_VALIDO + r')' +
    r'$'
    )

    for ip in ip_string:
        validar = padrao.match(ip)

        if validar:
            validos.append(ip)

        else:
            invalidos.append(ip)

    return escrever_arquivo(validos, invalidos)


def escrever_arquivo(validos, invalidos):
    caminho_arquivo = 'Lista_de_exercicios/sobre_arquivos/ex_01/ex_01/enderecos_IP_validos.txt'
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write('[Endereços válidos:]\n')

        for valido in validos:
            arquivo.writelines(f'{valido}\n')
        
        arquivo.write('\n[endereços Inválidos:]\n')

        for invalido in invalidos:
            arquivo.writelines(f'{invalido}\n')

if __name__ == '__main__':
    enderecos = ler_arquivo()
    validar_ipv4_corrigido(enderecos)
