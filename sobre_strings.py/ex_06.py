# Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês
# por extenso.

from datetime import datetime

def valida_data():
    while True:
        data_str = input("Digite a data no formato dd/mm/aaaa: ")
        
        try:
            datetime.strptime(data_str, '%d/%m/%Y')
            return data_str

        except ValueError:
            print("\033[1;31mFormato de data inválido. Use dd/mm/aaaa.\033[m")
            continue



def data_mes_extenso(data:str):
    meses = ['Janeiro', 'Fevereiro', 'Maço', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    data_lista = data.split('/')
    dia = data_lista[0]
    mes = data_lista[1]
    ano = data_lista[2]
    posicao = int(mes) - 1
    return f'\033[1;32m{dia} de {meses[posicao]} de {ano}\033[m'
    


if __name__ == '__main__':
    data_valida = valida_data()
    data_extenso = data_mes_extenso(data_valida)
    print(data_extenso)