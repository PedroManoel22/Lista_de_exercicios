# Desenvolva uma classe Macaco, que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), ver_bucho() e digerir().
# Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando 
# o conteúdo do estomago a cada refeição.
class Macaco:
    def __init__ (self, nome, bucho=[]):
        self.nome = nome
        self.bucho = bucho
    

  
    def digerir(self):
        while True:
            alimento = input(f'\nQual alimento o macaco {self.nome} irá digerir? ')
            if alimento not in self.bucho:
                print('\n\033[1;31mPor favor coloque um alimento que esteja no bucho do macaco\033[m')
            
            else:
                self.bucho.remove(alimento)
                print(f'\n\033[1;32m{alimento} digerido com sucesso!\033[m')
                break
            


    def ver_bucho(self):
        if not self.bucho:
            print(f'\nO bucho do macaco {self.nome} está vazio!\n')
        
        else:
            print(f'\nNo bucho do macaco {self.nome} tem:\n')
            for comida in self.bucho:
                print(comida)
            print()

    
    def comer(self):
        alimento = input('Qual alimento o macaco vai comer? ')
        self.bucho.append(alimento)
        print(f'\n\033[1;32mMacaco {self.nome} comeu {alimento}\033[m')
        self.ver_bucho()

    



def pede_nome():
    while True:
        nome = input('Insira o nome do macaco: ')

        if nome.isdigit():
            print('\n\033[1;31mO nome do macaco não pode ser apenas números\033[m\n')
        
        elif len(nome) <= 2:
            print('\n\033[1;31mO nome do macaco tem que ter pelo menos 2 caracteres!\033[m\n')
        
        else:
            return nome

def pede_bucho(nome):
    alimentos  = []
    while True:
        comeu = input(f'O macaco chamado {nome} comeu alguma coisa (S/N)? ').upper().strip()

        if comeu == 'S':
            while True:
                try:
                    qtd_alimentos = int(input('Quantos alimentos o macaco comeu? '))
                    break
                
                except ValueError:
                    print('\n\033[mColoque um valor inteiro, quero saber a quantidade de alimentos que o macaco comeu\033[m\n')
            
            for i in range(1, qtd_alimentos + 1):
                alimentos.append(input(f'Qual foi o {i}° alimento do macaco? '))
            
            bucho = alimentos
            return bucho


        elif comeu == 'N':
            bucho = []
            return bucho

if __name__ == '__main__':
    nome = pede_nome()
    bucho =  pede_bucho(nome)
    macaco1 = Macaco(nome, bucho)
    # menu
    while True:
        opcoes = [1, 2, 3, 4]
        print('----Menu----\n')
        try:
            opcao = int(input('[1] Digerir\n'
                '[2] Comer\n'
                '[3] Ver bucho\n'
                '[4] Sair\n\n'
                'O que deseja? '))
            
            if opcao not in opcoes:
                print('\033[m\nPor favor coloque um opção válida!\n')
            
            else:
                if opcao == 1:
                    macaco1.digerir()
                
                elif opcao == 2:
                    macaco1.comer()
                
                elif opcao == 3:
                    macaco1.ver_bucho()
                
                else:
                    break
        
        except ValueError:
            print('\nPor favor coloque um número inteiro!\n')
        
        except Exception as e:
            print(f'\nErro inesperado: {e.__class__.__name__}')
    
    print('\nObrigado e volte sempre!')