# Faça um programa que use a função valor_pagamento para determinar o valor a ser pago por uma prestação de uma conta. 
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a
# função valor_pagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
# O programa deverá então exibir o valor a ser pago na tela. Após a execução, o programa deverá voltar a pedir outro valor de 
# prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento, 
# o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
# O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. 
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

# Valor da prestação
def valor_prestacao():
    while True:
        try:    
            valor_prestacao = input('Insira o valor da prestação (0 para cancelar): ')
            valor_prestacao_float = round(float(valor_prestacao), 2)
            break

        except ValueError:
            print(f'\033[1;31mPor favor insira um valor int ou float\033[m')
        
        except Exception as e:
            print(f'Erro inesperado: {e.__name__}')

    return valor_prestacao_float


# Número de dias em atraso
def numero_dias_atraso():
    while True:
        try:
            num_dias_atraso = input('Insira o números de dias em atraso: ')
            num_dias_atraso_float = round(float(num_dias_atraso), 2)
            break

        except ValueError:
            print(f'\033[1;31mPor favor insira um valor do tipo float oi int\033[m')
        
        except Exception as e:
            print(f'Erro inesperado: {e.__name__}')

    return num_dias_atraso_float



def valor_pagamento(prestacao, dias_atraso):
    if dias_atraso == 0:
        valor_final = prestacao

    else:
        valor_multa = prestacao + (prestacao * 0.03)
        juros_dias_atraso = ((100 * 0.001) * dias_atraso)
        valor_final = valor_multa + juros_dias_atraso
    
    return f'\n>>> O valor final a ser pago é R${round(valor_final, 2)}\n'


if __name__ == '__main__':
    while True:
        prestacao = valor_prestacao()
        if prestacao == 0:
            break
        dias_atrasados = numero_dias_atraso()
        print(valor_pagamento(prestacao, dias_atrasados))
    print('Obrigado, e volte sempre! 👍')
     