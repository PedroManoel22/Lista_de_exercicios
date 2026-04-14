from funcoes import ler_arquivo, mostrar_n_primeiros

def main():
    arquivo = "Lista_de_exercicios/lista_de_projetos/Projeto1/relatorio.txt"
    dados = ler_arquivo(arquivo)
    mostrar_n_primeiros(dados)

if __name__ == "__main__":
    main()