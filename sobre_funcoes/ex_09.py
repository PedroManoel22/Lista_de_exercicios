# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

# obtém apenas números int
def obter_inteiro_valido(mensagem='Insira um número inteiro: '):
    while True:
        try:
            num = int(input(mensagem))
            return num 
        except ValueError:
        
            print("❌ \033[1;31mEntrada inválida. Por favor, digite um número inteiro.\033[m")
            
# retorna o inverso do número inserido
def reverso_numero(num):
    num_str = str(num)
    return f'número {num} ao contrário fica: {num_str[::-1]}'


if __name__ == '__main__':
    num = obter_inteiro_valido()
    num_reverso = reverso_numero(num)
    print(num_reverso)