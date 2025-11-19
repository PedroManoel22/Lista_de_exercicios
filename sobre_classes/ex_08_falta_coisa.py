# Desenvolva uma classe Macaco, que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), ver_bucho() e digerir().
# Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando 
# o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:
    def __init__ (self, nome, bucho=[]):
        self.nome = nome
        self.bucho = bucho
    

    def comer(self):
        alimento = input('Qual alimento o macaco vai comer? ')
        self.bucho.append(alimento)
        print(self.bucho)

    
    def ver_bucho(self):
        if self.bucho == 0:
            print(f'\nO bucho do macaco {self.nome} está vazio!')
        
        else:
            print(f'\nNo bucho do macaco {self.nome} tem:\n')
            for comida in self.bucho:
                print(comida)



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
    macaco1.ver_bucho()
    macaco1.comer()