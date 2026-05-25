# Crie uma classe que modele uma bola:

# Atributos: cor, circunferência, material
# Métodos: troca_cor e mostra_cor


class Bola:
    def __init__(self, cor: str, circunferencia: str, material: str):
        self._cor = cor
        self.circunferencia = circunferencia
        self.material = material

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, nova_cor: str):
        self._cor = nova_cor
        print("A bola mudou de cor!")

    def mostra_cor(self) -> None:
        print(f"A cor da bola de material de {self.material} é da cor {self.cor}")


if __name__ == "__main__":
    bola1 = Bola("Azul", "25", "borracha")
    bola1.mostra_cor()
    bola1.cor = "Preta"
    bola1.mostra_cor()
