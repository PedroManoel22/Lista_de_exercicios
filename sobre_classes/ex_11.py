# Implemente uma classe chamada Carro com as seguintes propriedades:

# Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
# O consumo é especificado no construtor e o nível de combustível inicial é 0.
# Forneça um método andar() que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
# Forneça um método obter_gasolina(), que retorna o nível atual de combustível.
# Forneça um método adicionar_gasolina(), para abastecer o tanque.

# Exemplo de uso:

# meu_fusca = Carro(15)             # 15 quilômetros por litro de combustível. 
# meu_fusca.adicionar_gasolina(20)  # abastece com 20 litros de combustível. 
# meu_fusca.andar(100)              # anda 100 quilômetros.
# meu_fusca.obter_gasolina()         # Imprime o combustível que resta no tanque.

class Carro:
    def __init__(self, kms_litro, nivel_combustivel=0):
        self.kms_litro = kms_litro
        self.nivel_combustivel = nivel_combustivel
    

    def andar(self, kms):
        kms_float = isinstance(kms, (float, int))
        eficiencia_atual = round(self.nivel_combustivel * self.kms_litro, 2)
        if not kms_float:
            raise TypeError('\nPor favor coloque uma distância válida!')

        if kms > eficiencia_atual:
            print(f'\nSeu carro não consegue andar por {kms} Km, pois no tangue só tem {self.nivel_combustivel}'
                   f'e seu carro só consegue andar {eficiencia_atual} km')
        
        else:
            self.nivel_combustivel -= round(kms / self.kms_litro, 2)
            print(f'Seu carro andou mais {kms} kms')


    def obter_gasolina(self):
        print(f'Seu carro está com {self.nivel_combustivel} litros de gasolina')

    
    def adicionar_gasolina(self, litros):
         self.nivel_combustivel += litros
        

meu_fusca = Carro(15)            
meu_fusca.adicionar_gasolina(20)   
meu_fusca.andar(100)              
meu_fusca.obter_gasolina()  
        