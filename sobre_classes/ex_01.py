# Crie uma classe que modele uma bola:

# Atributos: cor, circunferência, material
# Métodos: troca_cor e mostra_cor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self._cor = cor
        self.circunferencia = circunferencia
        self.material = material

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, nova_cor):
        self._cor = nova_cor
        print('A bola mudou de cor!')
        
    def mostra_cor(self):
        print(f'A cor da bola de material de {self.material} é da cor {self.cor}')


bola1 = Bola('Azul', '25', 'borracha')
bola1.mostra_cor()
bola1.cor = 'Preta'
bola1.mostra_cor()
