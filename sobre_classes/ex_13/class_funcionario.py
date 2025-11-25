# Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um float). 
# Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.

class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario
    
    def mostra_nome(self):
        print(self.nome)
    

    def mostra_salario(self):
        print(f'R${self.salario}')
       
funcionario1 = Funcionario('Pedro', 7000)