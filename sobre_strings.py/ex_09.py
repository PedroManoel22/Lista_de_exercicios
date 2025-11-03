# Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
# indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

import re
cpf = input('Insira seu cpf no seguinte formato, xxx.xxx.xxx-xx: ')
def valida_cpf(cpf):
    
    regex = re.compile(
        r"^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})(\d{3}\.\d{3}\.\d{3}-\d{2})$",
        flags=re.MULTILINE
    )

    valido = regex.findall(cpf)
    if valido:
        x = 10
        soma_total = 0

        # validação do primeiro digito
        for i in range(11):
            if cpf[i].isdigit():
                soma = int(cpf[i]) * x
                soma_total += soma
                x -= 1
        resto_divisao = soma_total % 11

        if resto_divisao == 1 or resto_divisao == 0:
            primeiro_digito = 0
    
        else:
            primeiro_digito = 11 - resto_divisao
        
        if primeiro_digito == int(cpf[12]):
            # validação do segundo digito
            y = 11
            soma_total_segundo = 0
            for i in range(12):
                if cpf[i].isdigit():
                    soma_segundo = int(cpf[i]) * y
                    soma_total_segundo += soma_segundo
                    x -= 1
            resto_divisao_segundo = soma_total_segundo % 11
        
            subtracao = 11 - resto_divisao_segundo
            if subtracao >= 10:
                segundo_digito = 0
            else:
                segundo_digito = subtracao
            if segundo_digito == int(cpf[13]):
                print('\033[1;32mCPF válido!\033[m')
    
    else:
        print('\033[1;31mCPF inválido\033[m')
    

if __name__ == '__main__':
    valida_cpf(cpf)