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

# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256

import re

caminho_arquivo = 'sobre_arquivos/ex_01/enderecos_IP.txt'

def ler_arquivo():
    with open(caminho_arquivo, 'r') as arquivo:
        enderecos = arquivo.read().split()
    return enderecos

IPV4_REGEX = r"^(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$"

def valida_enderecos_gera_relatorio(enderecos):
    validos = []
    for endereco in enderecos:
        valido_invalido =  re.fullmatch(IPV4_REGEX, endereco) is not None
        if valido_invalido:
            validos.append(valido_invalido)
    return validos

enderecos = ler_arquivo()
print(valida_enderecos_gera_relatorio('200.135.80.9'))
