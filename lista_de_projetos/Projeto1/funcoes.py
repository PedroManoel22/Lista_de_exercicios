from typing import Any


def ler_arquivo(nome_arquivo: str) -> dict[str, Any]:
    dados_usuarios: dict[str, Any] = {}
    count: int = 0

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for _, linha in enumerate(arquivo):
                partes = linha.strip().split()
                if len(partes) == 5:
                    dados_usuarios[f"linha{count}"] = partes
                count += 1

            return dados_usuarios

    except FileNotFoundError:
        print(f"Erro: O arquivo \033[1;31m'{nome_arquivo}'\033[m não foi encontrado.")
        return {}

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return {}


# 1. Ordenar os usuários pelo percentual de espaço ocupado


def ordenar(dados: dict[str, Any]) -> None:
    from rich import print

    usuarios_ordenados = sorted(dados.items(), key=lambda x: x[1][-1], reverse=True)

    print("\nLista Ordenada pelo percentual de espaço ocupado:")
    print(f"\n{'Nr.':<4} {'Usuário':<15} {'Espaço':<10} {'%':<10}")
    for _, ds in usuarios_ordenados:
        # 'dados' é a lista completa que você capturou
        print(f"{ds[0]:<4} {ds[1]:<15} {ds[2]:>7} {ds[3]} {ds[4]:>10}")

    print()


# 2. Mostrar apenas os n primeiros em uso, definido pelo usuário
def mostrar_n_primeiros(dados: dict[str, Any]) -> None:
    while True:
        try:
            x = int(
                input(
                    f"Informe a quantidade de usuário para o relatório [1 - {len(dados)}]: "
                )
            )

            if x > 80 or x < 1:
                print(f"\n[red]Por favor insira um valor entre 1 e {len(dados)}[/]\n")
                continue
            break

        except (ValueError, KeyboardInterrupt):
            print("\n[red]Por favor insira um número inteiro![/]\n")

    print(f"\nUsuários de 1 a {x}:\n")
    for i in range(x):
        print(list(dados.values())[i])

    print()
