# Crie uma classe que modele uma pessoa:

# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, 
# a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura


    @property
    def idade(self):
        return self._idade


    @idade.setter
    def idade(self):
        self._idade
    
    
    @property
    def altura(self):
        return self._altura


    @altura.setter
    def altura(self):
        self._altura

    
    @property
    def peso(self):
        return self._peso


    @peso.setter
    def peso(self):
        self._peso
    

    def envelhecer(self):
        self._idade += 1
        print(f'\nAgora {self.nome} tem {self._idade} anos!') 

        if self._idade < 21:
            self.crescer(0.5)
        
    
    def engordar(self):
        self._peso += 1
        print(f'\n{self.nome} engordou mais 1KG')
        print(f'E agora está com {self._peso:.2f}KG')
    

    def emagrecer(self):
        self._peso -= 1
        print(f'\n{self.nome} emagreceu  1KG')
        print(f'E agora está com {self._peso:.2f}KG')

    
    def crescer(self, aumenta = 0.2):
        self._altura += aumenta

        print(f'\n{self.nome} cresceu mais {aumenta}cm')
        print(f'Agora {self.nome} tem {self._altura}m')


pessoa1 = Pessoa('Pedro', 21, 73, 1.73)
pessoa1.envelhecer()
pessoa1.crescer()
pessoa1.engordar()
pessoa1.emagrecer()