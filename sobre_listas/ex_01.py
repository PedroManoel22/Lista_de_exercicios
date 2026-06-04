# Faça um programa que leia um vetor de 5 números inteiros e mostre-os.


def coletar_numeros(quantidade: int) -> list[int]:

    numeros: list[int] = []

    for i in range(1, quantidade + 1):
        numeros.append(validar_num(i))
    return numeros


def validar_num(x: int) -> int:

    while True:
        try:
            num = input(f"Insira o {x}° número inteiro: ")
            num_int = int(num)
            break
        except ValueError:
            print("\033[1;31mColoque um número inteiro!\033[m")

    return num_int


if __name__ == "__main__":
    NUMEROS_PARA_COLETAR = 5

    numeros_inseridos = coletar_numeros(NUMEROS_PARA_COLETAR)

    print(f"Números inseridos: {numeros_inseridos}")
