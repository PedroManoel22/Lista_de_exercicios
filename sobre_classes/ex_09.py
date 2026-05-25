# Faça um programa completo utilizando funções e classes que:

# Possua uma classe chamada Ponto, com os atributos x e y. ✔️
# Possua uma classe chamada Retangulo, com os atributos largura e altura. ✔️
# Possua uma função para imprimir os valores da classe Ponto ✔️
# Possua uma função para encontrar o centro de um Retângulo. ✔️
# Você deve criar alguns objetos da classe Retangulo.
# Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
# A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
# O valor do centro do objeto deve ser mostrado na tela
# Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.


class Ponto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Retangulo:
    def __init__(self, largura: float, altura: float):
        self.largura = largura
        self.altura = altura


def mostrar_valores_pontos(pontos: Ponto) -> None:
    x = pontos.x
    y = pontos.y
    print("\nCentro do retângulo:\n")
    print(f"X = {x}\nY = {y}")


def encontrar_centro(retangulo: Retangulo) -> Ponto:

    meio_x: float = retangulo.largura / 2
    meio_y: float = retangulo.altura / 2
    return Ponto(meio_x, meio_y)


def pede_valida_retangulo() -> Retangulo:
    while True:
        # valida largura
        try:
            largura = int(input("\nInsira a largura: "))

            # valida altura
            try:
                altura = int(input("\nInsira a altura: "))

                if altura == largura:
                    print(
                        "\nPor favor coloque a altura diferente da largura, senão forma um quadrado!\n"
                    )
                    continue

                break

            except ValueError:
                print("\n\033[1;31mPor favor coloque uma altura do tipo int!\033[m\n")

            except Exception as e:
                print(f"\n\033[1;31mErro: {e.__class__.__name__}\033[m")

        except ValueError:
            print("\n\033[1;31mPor favor coloque uma largura do tipo int!\033[m\n")

        except Exception as e:
            print(f"\n\033[1;31mErro: {e.__class__.__name__}\033[m")

    return Retangulo(largura, altura)


if __name__ == "__main__":
    opcoes = [1, 2]
    retangulo = pede_valida_retangulo()
    pontos = encontrar_centro(retangulo)
    mostrar_valores_pontos(pontos)
    while True:
        print("\n----Menu----\n")
        try:
            opcao = int(input("[1] - Alterar valores\n[2] - Sair\n\nO que deseja? "))

            if opcao not in opcoes:
                print("\nPor favor insira uma opção válida!\n")

            else:
                if opcao == 1:
                    retangulo = pede_valida_retangulo()
                    pontos = encontrar_centro(retangulo)
                    mostrar_valores_pontos(pontos)

                elif opcao == 2:
                    break

        except ValueError:
            print("\n\033[1;31mPor favor coloque um número inteiro!\033[m\n")

        except Exception as e:
            print(f"\n\033[1;31mError: {e.__class__.__name__}\033[m")

    print("\nVolte sempre!")
