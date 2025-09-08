# Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

def obter_numero_real(ordem):
    """
    Solicita um número real ao usuário e valida a entrada.

    Retorna:
        float: O número real inserido pelo usuário.
    """
    while True:
        try:
            num_str = input(f'Insira o {ordem}º número (ex: 3.14): ')
            num_float = float(num_str)

            # O coração da validação: verifica se a string original continha um ponto decimal.
            if '.' not in num_str:
                print('\033[1;31mPor favor, insira um número real, com casas decimais.\033[m')
                continue # Continua o loop para pedir o número novamente
            
            return num_float
        
        except ValueError:
            print('\033[1;31mPor favor, insira uma entrada numérica válida.\033[m')

def coletar_numeros(quantidade):
    """
    Coleta uma lista de números reais do usuário.

    Args:
        quantidade (int): A quantidade de números a serem coletados.

    Retorna:
        list: Uma lista com os números reais inseridos.
    """
    numeros = []
    for i in range(1, quantidade + 1):
        numeros.append(obter_numero_real(i))
    return numeros


if __name__ == '__main__':
    NUMEROS_PARA_COLETAR = 10
    
    numeros_inseridos = coletar_numeros(NUMEROS_PARA_COLETAR)
    
    print(f'Números inseridos: {numeros_inseridos}')

    numeros_invertidos = numeros_inseridos[::-1]
    
    print(f'Números em ordem invertida: {numeros_invertidos}')

