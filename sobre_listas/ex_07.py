# Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.


def ler_numeros(qtd_numeros: int) -> list[int]:

    contador = 0
    numeros: list[int] = []

    while True:
        try:
            num = input("Insira um número inteiro: ")
            num_int = int(num)
            contador += 1
            numeros.append(num_int)

            if contador == qtd_numeros:
                break

        except ValueError:
            print("\033[1;31mPor favor coloque um número inteiro\033[m")

    return numeros


def soma(numeros: list[int]) -> int:

    return sum(numeros)


def multiplicacao(numeros: list[int]) -> int:

    x = 1

    for num in numeros:
        x *= num

    return x


def print_bonito(numeros: list[int]) -> None:

    print(f"Números: {numeros}")
    print(f"Soma: {soma(numeros)}")
    print(f"Multiplicação: {multiplicacao(numeros)}")


if __name__ == "__main__":
    QUANTIDADE_NUMEROS = 5
    print_bonito(ler_numeros(QUANTIDADE_NUMEROS))
