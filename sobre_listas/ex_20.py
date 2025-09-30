# As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou.
# Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.

# Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:

# Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
# O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo;
# Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades.
# Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. 
# Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima.

# Ao final, o programa deverá apresentar:

# O salário de cada funcionário, juntamente com o valor do abono;
# O número total de funcionário processados;
# O valor total a ser gasto com o pagamento do abono;
# O número de funcionário que receberá o valor mínimo de 100 reais;
# O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. 
# Os valores podem mudar a cada execução do programa.
# O piso do abono de R$100 será para salário abaixo de R$700

# Projeção de Gastos com Abono
# ============================ 

# Salário: 1000
# Salário: 300
# Salário: 500
# Salário: 100
# Salário: 4500
# Salário: 0

# Salário    - Abono     
# R$ 1000.00 - R$  200.00
# R$  300.00 - R$  100.00
# R$  500.00 - R$  100.00
# R$  100.00 - R$  100.00
# R$ 4500.00 - R$  900.00

# Foram processados 5 colaboradores
# Total gasto com abonos: R$ 1400.00
# Valor mínimo pago a 3 colaboradores
# Maior valor de abono pago: R$ 900.00




def coletar_salarios():
    salarios = []
    qtd_colaboradores = 0
    while True:
        try:
            salario = input('Salário: ')
            salario_float = float(salario)
            if salario_float == 0:
                break
            
        except ValueError:
            print('\033[1;31m Por favor coloque um salário válido!\033[m')
        
        except Exception as e:
            print(f'Erro desconhecido: {e.__class__.__name__}')
        
        salarios.append(round(salario_float, 2))
        qtd_colaboradores += 1
    
    return calcular_abono(salarios, qtd_colaboradores)


def calcular_abono(salarios, qtd):
    salarios_abonos = []
    abono_min = 0
    for salario in salarios:
        if salario < 700:
            salarios_abonos.append(100)
            abono_min += 1
        else:
            abono = salario * 0.2
            salarios_abonos.append(abono)
    
    return exibir_resultados(salarios, salarios_abonos, qtd, abono_min)


def exibir_resultados(salarios, abonos, qtd, abono_min):
    print()
    print(f'{'Salário':>5}{'- Abono':>9}')
    for i in range(0, len(salarios)):
        print(f'R${salarios[i]} - R${abonos[i]:>2}')
    
    print()
    print(f'Foram processados {qtd} colaboradores')
    total_abonos = round(sum(abonos), 2)
    print(f'Total gasto com abonos: R$ {total_abonos}')
    print(f'Valor minímo pago a {abono_min} colaboradores')
    maior_abono = max(abonos)
    print(f'Maior valor de abono pago: R$ {maior_abono}')

if __name__ == '__main__':
    coletar_salarios()
    