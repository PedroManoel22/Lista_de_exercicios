# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

# obtém apenas números int
def obter_inteiro_valido(mensagem: str ='Insira um número inteiro: ') -> None | int:
    while True:
        try:
            num = int(input(mensagem))
            return num 
        except ValueError:
        
            print("❌ \033[1;31mEntrada inválida. Por favor, digite um número inteiro.\033[m")
            
# retorna o inverso do número inserido
def reverso_numero(num: int) -> str:
    num_str = str(num)
    return f'número {num} ao contrário fica: {num_str[::-1]}'


if __name__ == '__main__':
    num = obter_inteiro_valido()
    if num is not None:
        print(reverso_numero(num))
