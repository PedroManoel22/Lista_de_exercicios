
def ler_arquivo() -> dict[str, str]:
    nome_arquivo = "Lista_de_exercicios/lista_de_projetos/Projeto1/usuarios.txt"
    dados_usuarios: dict[str, str] = {}

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            
            for _, linha in enumerate(arquivo):
                partes = linha.strip().split()
                print(f"\nPartes {partes}\n")
                
                if len(partes) == 2:
                    nome = partes[0]
                    numero = partes[1]
                    
                    dados_usuarios[nome] = numero

    except FileNotFoundError:
        print(f"Erro: O arquivo \033[1;31m'{nome_arquivo}'\033[m não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    
    return dados_usuarios


def gerar_relatorio(dados_usuarios: dict[str, str]) -> None:

    endereco_arquivo = "Lista_de_exercicios/lista_de_projetos/Projeto1/relatorio.txt"

    cabecalho = """
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
    """

    LARGURA_NOME = 15   
    LARGURA_MB = 10         
    LARGURA_PCT = 16
    espaco_total = 0
    qtd_usuarios = 0

    try:
        with open(endereco_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(cabecalho)
            arquivo.write('\n')

            # contabiliza o total de memória usada
            for _, nome in enumerate(dados_usuarios):
                espaco_total += int(dados_usuarios[nome])
                
            espaco_total = round(espaco_total / (1024 * 1024), 2)
            espaco_total_str = str(espaco_total)

            # pega os dados de todos os funcionários
            for indice, nome in enumerate(dados_usuarios):
                espaco = round(int(dados_usuarios[nome]) / (1024 * 1024), 2)
                espaco_str = str(espaco)
                indice = indice + 1
                indice_str = str(indice)
                espaco = round(int(dados_usuarios[nome]) / (1024 * 1024), 2)
                porcentagem = round((espaco * 100) / espaco_total, 2)

                arquivo.write(
                    f"{indice_str} "  
                    f"{nome:<{LARGURA_NOME}} " 
                    f"{espaco_str:>{LARGURA_MB}} MB"
                    f"{porcentagem:>{LARGURA_PCT}}%\n"
                             )
            arquivo.write(f'\nEspaço total ocupado: {espaco_total_str} MB')
            qtd_usuarios = len(dados_usuarios)
            espaco_medio = round(espaco_total / qtd_usuarios, 2)
            arquivo.write(f'\nEspaço médio ocupado: {espaco_medio} MB')
            
            print(f"Arquivo '\033[1;32m{endereco_arquivo}\033[m' criado e escrito com sucesso.")

    except IOError as e:
        print(f"Erro ao manipular o arquivo: {e}")
