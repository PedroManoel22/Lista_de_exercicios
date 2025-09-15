# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
# Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000,
# ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários
# nos seguintes intervalos de valores:
# $200 - $299  0
# $300 - $399  1 
# $400 - $499  2
# $500 - $599  3
# $600 - $699  4
# $700 - $799  5
# $800 - $899  6
# $900 - $999  7
# $1000 em diante 8


def ler_salarios(quant):

    vendas_funcionario = []

    for i in range(1, quant+1):

        while True:

            try:

                vendas = input(f'Insira o total de vendas do {i}° funcionário: ')
                vendas = int(vendas)
                vendas_funcionario.append(vendas)

                break

            except ValueError:

                print('\033[1;31mPor favor coloque um salário válido!\033[m')

            except Exception as e:

                print(f'Erro desconhecido \033[1;31m{e.__class__.__name__}\033[m')

    return vendas_funcionario


def conta_salarios(vendas_brutas):

    contadores_salario = [0] * 9
    
    # Constantes do problema para manter o código limpo e fácil de ler
    SALARIO_BASE = 200
    TAXA_COMISSAO = 0.09
    
    for vendas in vendas_brutas:
        # 1. Calcular o salário total
        salario = SALARIO_BASE + (vendas * TAXA_COMISSAO)
        
        # 2. Determinar o índice correto para o salário
        # Esta é a parte "mágica" que substitui a cadeia de if/elif
        indice = int(salario // 100) - 2 # Ex: $470 -> 470 // 100 = 4 -> 4 - 2 = 2. Índice 2 corresponde a $400-499.
        
        # 3. Tratar o caso especial de $1000 ou mais
        if indice >= 8:
            indice = 8

        # 4. Incrementar o contador no índice correto
        # Usamos try/except para segurança, caso o cálculo do índice dê um valor inesperado,
        # embora a lógica acima já previna isso.
        try:
            contadores_salario[indice] += 1
        except IndexError:
            # Isso é mais uma medida de segurança.
            # O ideal é que a lógica de cálculo do índice seja robusta.
            print(f"Salário fora dos intervalos previstos: ${salario:.2f}")

    return contadores_salario


def exibir_resultados(contadores):

    print('-------- Relatório de salários dos vendedores --------')
    for i, contador in enumerate(contadores):
        limite_inferior = (i + 2) * 100
        limite_superior = limite_inferior + 99
        print(f"Salário ${limite_inferior} - ${limite_superior}: {contador} vendedores")
        
    # Exibe o último intervalo separadamente
    print(f"Salário $1000 ou mais: {contadores[-1]} vendedores")

if __name__ == "__main__":

    QUANTIDADE_FUNCIONARIOS = 5
    salarios_obtidos = ler_salarios(QUANTIDADE_FUNCIONARIOS)

    resultados = conta_salarios(salarios_obtidos)
    
    exibir_resultados(resultados)
