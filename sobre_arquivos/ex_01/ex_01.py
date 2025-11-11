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


PADRAO_IP_SIMPLES = re.compile(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$') 

def validar_ipv4_corrigido(ip_string):
    validos = []
    invalidos = []

    for ip in ip_string:
        octetos_capturados = PADRAO_IP_SIMPLES.findall(ip)
        if not octetos_capturados:
            return False

        octetos_str = octetos_capturados[0]

        for octeto_str in octetos_str:
            octeto_int = int(octeto_str)
            
            if not (0 <= octeto_int <= 255):
                invalidos.append(ip)
                
        validos.append(ip)
    print(validos)
    print(invalidos)


enderecos = ler_arquivo()
validar_ipv4_corrigido(enderecos)
