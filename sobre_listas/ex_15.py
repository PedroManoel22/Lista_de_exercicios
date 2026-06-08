# Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:

# Mostre a quantidade de valores que foram lidos; ok
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro; ok
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; ok
# Calcule e mostre a soma dos valores; ok
# Calcule e mostre a média dos valores; ok
# Calcule e mostre a quantidade de valores acima da média calculada; ok
# Calcule e mostre a quantidade de valores abaixo de sete; ok
# Encerre o programa com uma mensagem;
def entrada_dados() -> list[int]:
    numeros: list[int] = []

    while True:
        try:
            num = input("Insira um número inteiro: ")
            num_int = int(num)
            if num_int != -1:
                numeros.append(num_int)
            if num_int == -1:
                break
        except ValueError:
            print("\033[1;31mPor favor coloque um número inteiro!\033[m")

    return numeros


def exibir_dados(nums: list[int]) -> None:

    print(f"A quantidade de números inseridos foi de: {len(nums)} números")
    print("Números inseridos: ", end="")
    for num in nums:
        print(f"{num} ", end="")
    print()
    nums_invertidos = nums[::-1]
    print("Números em ordem invertida:")
    for num in nums_invertidos:
        print(num)
    print(f"Soma: {sum(nums)}")
    media = sum(nums) / len(nums)
    print(f"Média: {media}")
    qtd_maior = 0
    qtd_menor_sete = 0
    for num in nums:
        if num > media:
            qtd_maior += 1
        if num < 7:
            qtd_menor_sete += 1
    print(f"Quantidade de números maiores que a média: {qtd_maior}")
    print(f"Quantidade de números menores que 7: {qtd_menor_sete}")


if __name__ == "__main__":
    exibir_dados(entrada_dados())
    print("Obrigado Volte Sempre!🥰🥰")
