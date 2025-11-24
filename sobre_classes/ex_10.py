# Faça um programa completo utilizando classes e métodos que:

# Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:

# tipo_combustivel
# valor_litro
# quantidade_combustivel
# Possua no mínimo esses métodos:

# abastecer_por_valor(): método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
# abastecer_por_litro(): método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
# alterar_valor(): altera o valor do litro do combustível.
# alterar_combustivel(): altera o tipo do combustível.
# alterar_quantidade_combustivel(): altera a quantidade de combustível restante na bomba.

# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba

class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    

    def abastecer_por_valor(self, valor):
        quantidade_litro = round(valor / self.valor_litro, 2)
        print(f'\nVocê abasteceu R${valor} que deu {quantidade_litro} litros\n')
        self.alterar_quantidade_combustivel(quantidade_litro)
        
    
    def abastecer_por_litro(self, litros):
        valor_final = round(litros * self.valor_litro, 2)
        print(f'\nVocê abasteceu {litros} litros que deu R${valor_final}\n')
        self.alterar_quantidade_combustivel(litros)


    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
    

    def alterar_combustivel(self):
        novo_combustivel = valida_combustivel()

        if novo_combustivel == self.tipo_combustivel:

            while novo_combustivel == self.tipo_combustivel:       
                print('\nO combustivel não pode ser alterado para o mesmo combustível\n')
                novo_combustivel = valida_combustivel()

        self.tipo_combustivel = novo_combustivel
        
        print(f'\n\033[1;32mCombustível alterado para {self.tipo_combustivel}\033[m\n')
        

    def alterar_quantidade_combustivel(self, qtd_litros):
        print(f'\nAntes tinhamos {self.quantidade_combustivel:.2f} litros')
        self.quantidade_combustivel -= qtd_litros
        print(f'Agora temos {self.quantidade_combustivel:.2f} litros')
        


def valida_combustivel():
    combustiveis_disponiveis = [1, 2]

    # loop para validar o tipo de combustível 
    while True:
        try:
            opcao = int(input('Insira o tipo de combustível ([1] Álcool, [2] Gasolina): '))

            if opcao not in combustiveis_disponiveis:
                print('\n\033[1;31mPor favor coloque uma opção válida!\n\033[m')
            
            else:
                if opcao == 1:
                    return 'Álcool'

                else:
                    return 'Gasolona'

        except ValueError:
            print('\n\033[1;31mPor favor coloque um número inteiro!\033[m\n')
        
        except Exception as e:
            print(f'\n\033[1;33mErro inesperado: {e.__class__.__name__}\033[m\n')


def pede_valor_litro():
    while True:
        try:
            valor = float(input('Insira o valor do combustível: '))
            valor = round(valor, 2)
            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um valor válido!\n\033[m')
        
        except Exception as e:
            print(f'\n\033[1;33mErro inesperado: {e.__class__.__name__}\033[m\n')
    
    return valor


def quantidade_combustivel_bomba():
    while True:
        try:
            litros = float(input('Insira a quantidade de combustível existente na bomba: '))
            litros = round(litros, 2)
            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um valor válido!\n\033[m')
        
        except Exception as e:
            print(f'\n\033[1;33mErro inesperado: {e.__class__.__name__}\033[m\n')
    
    return litros



if __name__ == '__main__':
    tipo_combustivel = valida_combustivel()
    valor_litro = pede_valor_litro()
    quantidade_combustivel = quantidade_combustivel_bomba()
    bomba1 = BombaCombustivel(tipo_combustivel, valor_litro, quantidade_combustivel)
    # menu
    opcoes = [1, 2, 3, 4, 5]
    while True:
        
        print('\n----Menu----\n')
        try:
            opcao = int(input('[1] Abastecer por valor\n'
                        '[2] Abastecer por litro\n'
                        '[3] Alterar combustível\n'
                        '[4] Alterar valor\n'
                        '[5] Sair\n\n' 
                        'O que deseja? '
                        ))
            
            if opcao not in opcoes:
                print('\n\033[1;33mPor favor coloque uma opção válida!\033[m\n')
            
            if opcao in opcoes:
                if opcao == 1:
                    # validação por valor
                    while True:
                        try:
                            valor = float(input('Insira o valor para abastecer em reais: '))
                            valor = round(valor, 2)
                            abastecer = bomba1.abastecer_por_valor(valor)
                            break

                        except ValueError:
                            print('\n\033[1;31mPor favor coloque um valor válido!\n\033[m')
                        
                        except Exception as e:
                            print(f'\n\033[1;33mErro inesperado: {e.__class__.__name__}\033[m\n')
                        
                
                if opcao == 2:
                     # validação por litros
                     while True:
                        try:
                            valor = float(input('Insira o valor para abastecer em litros: '))
                            valor = round(valor, 2)
                            bomba1.abastecer_por_litro(valor)
                            break
                        
                        except ValueError:
                            print('\n\033[1;31mPor favor coloque um valor válido!\n\033[m')
                        
                        except Exception as e:
                            print(f'\n\033[1;33mErro inesperado: {e.__class__.__name__}\033[m\n')

                if opcao == 3:
                    bomba1.alterar_combustivel()

                
                if opcao == 4:
                    # valida valor
                    while True:
                        try:
                            valor = float(input('Para quantos reais você quer alterar o valor do combustível: '))
                            valor = round(valor, 2)
                            bomba1.alterar_valor()
                        
                        except ValueError:
                            print('\n\033[1;31mPor favor coloque um valor válido!\n\033[m')
                        
                        except Exception as e:
                            print(f'\n\033[1;33mErro inesperado: {e.__class__.__name__}\033[m\n')
                
                if opcao == 5:
                    break
                      
        except ValueError:
            print('\n\033[1;31mPor favor coloque um número inteiro!\033[m\n')
        
        except Exception as e:
            print(f'\n\033[1;33mErro inesperado: {e.__class__.__name__}\033[m\n')
            