from funcoes import ler_arquivo, ordenar

# orndena o relatório.txt pelo estpaço ocupado
def main():
    nome_arquivo = "Lista_de_exercicios/lista_de_projetos/Projeto1/relatorio.txt"
    dados = ler_arquivo(nome_arquivo)
    ordenar(dados)

if __name__ == '__main__':
    main()