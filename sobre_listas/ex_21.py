# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
# Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:

# O modelo do carro mais econômico;
# Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, 
# considerando um que a gasolina custe R$ 2,25 o litro.
# Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo.
# Os dados são fictícios e podem mudar a cada execução do programa.

# Comparativo de Consumo de Combustível

# Veículo 1
# Nome: fusca
# Km por litro: 7
# Veículo 2
# Nome: gol
# Km por litro: 10
# Veículo 3
# Nome: uno
# Km por litro: 12.5
# Veículo 4
# Nome: Vectra
# Km por litro: 9
# Veículo 5
# Nome: Peugeout
# Km por litro: 14.5

# Relatório Final
# 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
# 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
# 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
# 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
# 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
# O menor consumo é do peugeout.



def coleta_dados(qtd):
    nomes = []
    kms_litro = []
    for i in range(1, qtd + 1):
        print(f'Veículo {i}')
        nomes.append(input('Nome: '))
        km = float(input('Km por litro: '))
        kms_litro.append(km)

    return calcular_km_custo(nomes, kms_litro)


def calcular_km_custo(nomes, kms_litro):
    consumo_mil_km = []
    custo_mil_km = []

    for i in range(0, len(nomes)):
        consumo = round(QUANTIDADE_KM / kms_litro[i], 1)
        consumo_mil_km.append(consumo)
        custo = round(GASOLINA * consumo, 2)
        custo_mil_km.append(custo)
    
    return exibir(nomes, kms_litro, consumo_mil_km, custo_mil_km)


def exibir(nomes, kms_litro, consumo_mil, custo):
    print('\nRelatório Final')
    
    max_nome_len = max(len(nome) for nome in nomes) if nomes else 0

    largura_kms_litro = 8
    largura_consumo = 10
    largura_custo = 10


    header = (
        f'{"#"}'
        f'{" Veículo":<{max_nome_len + 2}}'  # +2 para espaço após o número
        f'{"Km/L":>{largura_kms_litro}}'
        f'{" Litros":>{largura_consumo}}'
        f'{"Custo":>{largura_custo}}'
    )
    print(header)
    print("-" * len(header)) 


    for i, nome in enumerate(nomes):
        linha = (
            f'{i + 1:<2}'
            f'{nome:<{max_nome_len + 2}}'
            f'{kms_litro[i]:>{largura_kms_litro}.1f}'
            f'{consumo_mil[i]:>{largura_consumo}.2f}'
            f' R${custo[i]:>{largura_custo-3}.2f}'
        )
        print(linha)
    
    # Encontrar o menor consumo de forma mais clara
    # zip() é uma função Pythônica que agrupa elementos de múltiplas listas.
    # min() com a chave 'key' é ideal para encontrar o menor valor baseado em uma métrica.
    menor_consumo, nome_menor_consumo = min(zip(consumo_mil, nomes))
    
    print(f'\nO menor consumo é do {nome_menor_consumo}')


if __name__ == '__main__':
    QUANTIDADE_KM = 1000
    GASOLINA = 2.25
    QUANTIDADE_VEICULOS = 5
    coleta_dados(QUANTIDADE_VEICULOS)

