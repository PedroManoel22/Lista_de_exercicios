# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

# F
# FU
# FUL
# FULA
# FULAN
# FULANO

def valida_nome():
    while True:
        nome = input('Insira seu nome: ').strip()

        if not nome:
            print('\033[1;31mPor favor coloque um nome (o campo não pode ser vazio)\033[m')
            continue
        
        if nome.isdigit():
            print(f'\033[1;33m ⚠️  Entrada inválida: O nome não pode ser um número puro. Tente novamente.\033[m')
            continue

        return nome
    

def nome_escada(nome):
    tamanho = len(nome)
    for i in range(tamanho + 1):
        print(nome[:i])


if __name__ == '__main__':
    nome_valido = valida_nome()
    nome_escada(nome_valido)

