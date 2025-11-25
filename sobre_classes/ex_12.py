# Faça uma classe ContaInvestimento que seja semelhante a classe ContaBancaria, com a diferença de que se adicione um atributo taxa_juros. 
# Forneça um inicializador que configure tanto o saldo inicial como a taxa de juros. 
# Forneça um método adicione_juros() (sem parâmetro explícito) que adicione juros à conta.

# Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. 
# Depois aplique o método adicione_juros() cinco vezes e imprime o saldo resultante.


class ContaBancaria():
    def __init__(self, saldo):
        self.saldo = saldo

class ContaInvestimento(ContaBancaria):

    def __init__(self, saldo, taxa):
        super().__init__(saldo)
        self.taxa = taxa

    def adicone_juros(self):
        self.saldo +=  (self.saldo * (self.taxa / 100))


conta_investimento = ContaInvestimento(1000, 10)
conta_investimento.adicone_juros()
conta_investimento.adicone_juros()
conta_investimento.adicone_juros()
conta_investimento.adicone_juros()
conta_investimento.adicone_juros()
saldo = conta_investimento.saldo
print(saldo)
