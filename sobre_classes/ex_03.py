# Crie uma classe que modele um retângulo:

# Atributos: Lado_a, Lado_b (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.


class Triangulo:
    def __init__(self, comprimento, largura):
        self._comprimento = comprimento
        self._largura = largura

    @property
    def mudar_valor_dos_lados(self):
        return self._comprimento, self._largura
    

    @mudar_valor_dos_lados.setter
    def mudar_valor_dos_lados(self, novos_valores):
        comprimento, largura = novos_valores
        self._comprimento = comprimento
        self._largura = largura


triangulo1 = Triangulo(5, 2)
print(triangulo1._comprimento)
print(triangulo1._largura)
triangulo1.mudar_valor_dos_lados = (5, 6)
print(triangulo1._comprimento)
print(triangulo1._largura)



        