# Crie uma classe que modele um retângulo:

# Atributos: Lado_a, Lado_b (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidadas de um local. 
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

# Aqui vamos usar um piso de 30x30cm
# Area piso =  0,09m²
# A quantidade de pisos será acrescentada mais 10% de sobra


class Retangulo:
    def __init__(self, comprimento, largura):
        self._comprimento = comprimento
        self._largura = largura

    @property
    def mudar_valor_dos_lados(self):
        return self._comprimento, self._largura
    

    @mudar_valor_dos_lados.setter
    def mudar_valor_dos_lados(self, novos_valores):
        comprimento_antigo = self._comprimento
        largura_antigo = self._largura
        comprimento, largura = novos_valores
        self._comprimento = comprimento
        self._largura = largura
        print(f'\n\033[1;32mO valor do comprimento de {comprimento_antigo:.2f} foi para {self._comprimento:.2f}\n'
              f'O valor da largura de {largura_antigo:.2f} foi para {self._largura:.2f}\033[m')

    
    def retonar_valor_lados(self):
        print(f'\n\033[1;34mO valor do comprimento é = {self._comprimento:.2f} metros\n'
              f'O valor da largura é = {self._largura:.2f} metros\033[m')

    
    def calcular_area(self):
        area = self._comprimento * self._largura
        return area

    
    def calcular_perimetro(self):
        perimetro = (self._largura * 2 ) + (self._comprimento * 2)
        return perimetro


if __name__ == '__main__':
    print('----Insira as medidas do local----\n')
    # Largura
    def pede_comprimento_largura():
        while True:
            try:
                largura = float(input('Insira a largura: '))
                break
            
            except ValueError:
                print('\n\033[1;31mPor favor coloque uma largura válida\033[m\n')
        
        # Comprimento
        while True:
            try:
                comprimento = float(input('Insira a comprimento: '))
                break
            
            except ValueError:
                print('\n\033[1;31mPor favor coloque uma largura válida\033[m\n')
        
        return comprimento, largura
    
    comprimento, largura = pede_comprimento_largura()
    molde = Retangulo(comprimento, largura)

    # menu
    while True:
        opcoes = [x for x in range(0,6)]
        print('\n------Menu------')
        try:
            opcao = input('[0] - sair\n'
                        '[1] - Mudar valores\n'
                        '[2] - Ver valores\n'
                        '[3] - Calcular área\n'
                        '[4] - Calcular perímetro\n' \
                        '[5] - Saber a quantidade de piso (considerando o rodapé) a ser usado\n\n'
                        'O que deseja executar: ')
            
            opcao = int(opcao)

        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um número inteiro!\033[m')
        
        except Exception as e:
            print(f'\nErro inesperado, tente novamente! {e.__class__.__name__}')
        

        if opcao not in opcoes:
            print('\n\033[1;31mPor favor uma das opções\033[m')
            
        else:
            if opcao == 0:
                break

            if opcao == 1:
                comprimento, largura = pede_comprimento_largura()
                molde.mudar_valor_dos_lados = (comprimento, largura)
            
            if opcao == 2:
                molde.retonar_valor_lados()
            
            if opcao == 3:
                area = molde.calcular_area()
                print(f'\n\033[1;35mA área do retângulo é de {area:.2f}m²\033[m')
                
            
            if opcao == 4:
                perimetro = molde.calcular_perimetro()
                print(f'\n\033[1;34mO perímetro é de {perimetro:.2f} metros\033[m')
            
            if opcao == 5:
                area = molde.calcular_area()
                perimetro = molde.calcular_perimetro()
                total_piso = (area / 0.09) + (perimetro / 0.3)
                total_piso_sobra = total_piso + (total_piso * 0.1)
                print(f'\no total de piso vai ser de {total_piso:.1f} pisos\n'
                      f'Com os 10% de folga ficamos com {total_piso_sobra:.1f} pisos')
            
    print('\nVolte sempre!')
