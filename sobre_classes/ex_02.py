# Exercício 02
# Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado):
        self._lado = lado
    
    @property
    def lado(self):
        return self._lado
    

    @lado.setter
    def lado(self, valor):
        self._lado = valor
    

    def retona_valor_lado(self):
        print(f'O valor do lado é de {self._lado}')
    

    def calcular_area(self):
        area = self._lado * self._lado
        print(f'A área do quadrado de lado {self._lado} = {area}m²')


quadrado1 = Quadrado(25)
quadrado1.retona_valor_lado()
quadrado1.calcular_area()
quadrado1.lado = 5
quadrado1.retona_valor_lado()
quadrado1.calcular_area()

