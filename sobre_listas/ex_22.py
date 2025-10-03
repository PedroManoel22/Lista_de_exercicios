# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área.
# A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.

# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo:
# um número de identificação do mouse o tipo de defeito:

# necessita da esfera;
# necessita de limpeza; 
# a.necessita troca do cabo ou conector; 
# a.quebrado ou inutilizado.
# Uma identificação igual a zero encerra o programa.
# Ao final o programa deverá emitir o seguinte relatório:

# Quantidade de mouses: 100

# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%

situacoes = {'necessita da esfera': 1,
             'necessita de limpeza': 2,
             'necessita troca do cabo ou conector': 3,
             'quebrado ou inutilizado': 4}

def dados_mouses():
    situacoes_mouses = []
    qtd = 0
    while True:
        try:
            id = input('Id do mouse: ')
            id_int = int(id)
            
            if id_int == 0:
                break

            else:
                print()
                print('\033[1;49;32m1- necessita da esfera\n2- necessita de limpeza\n3- necessita troca do cabo ou conector\n4- quebrado ou inutilizado\033[m')
                print()
                qtd += 1

                try:
                    while True:
                        situacao = input(f'Qual a situação do mouse de id ({id_int}): ')
                        situacao_int = int(situacao)

                        if situacao_int not in situacoes.values():
                            print('\033[4;49;35mEsta situação não existe!\033[m')
                            print()
                        else:
                            situacoes_mouses.append(situacao_int)
                            break
                
                except ValueError:
                    print('\033[1;49;31mPor favor coloque uma situaçõa válida!\033[m')


        except ValueError:
            print('\033[1;31mPor favor coloque um número de id válido!\033[m')

    return contabiliza_exibir_situacoes(situacoes_mouses, qtd)


def contabiliza_exibir_situacoes(estado_mouses, qtd):
    print()
    print(f'Quantidades de mouses: {qtd}')
    print()
    for i in range(1, 5):
        total = estado_mouses.count(i)
        for k, v in situacoes.items():
            if v == i:
                print(f'{i} - {k} {total}')
        
        


dados_mouses()

