# Aprimore a classe do exercício anterior para adicionar o método aumentar_salario() (porcentual_de_aumento) que aumente o salário do funcionário em uma certa porcentagem.

# Exemplo de uso:

# harry = funcionário('Harry', 25000)
# harry.aumentar_salario(10)

class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario
    
    def mostra_nome(self):
        print(self.nome)
    

    def mostra_salario(self):
        print(f'R${self.salario}')
    
    def aumentar_salario(self, taxa):
        self.salario += self.salario * (taxa / 100)
        print(f'\nO salário de {self.nome} foi para {self.salario} ')
       
funcionario1 = Funcionario('Pedro', 7000)
