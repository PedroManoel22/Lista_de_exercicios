# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, 
# o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa,
#  baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125

# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, 
# chamado "relatório.txt", no seguinte formato:

# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso

# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB



def ler_arquivo():
    nome_arquivo = "lista_de_exercicios/Lista_de_exercicios/sobre_listas/ex_23/usuarios.txt"
    dados_usuarios = {}

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            
            for _, linha in enumerate(arquivo):
                partes = linha.strip().split()
                
                if len(partes) == 2:
                    nome = partes[0]
                    numero = partes[1]
                    
                    dados_usuarios[nome] = numero

    except FileNotFoundError:
        print(f"Erro: O arquivo \033[1;31m'{nome_arquivo}'\033[m não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    
    return dados_usuarios


def gerar_relatorio(dados_usuarios):

    endereco_arquivo = "lista_de_exercicios/Lista_de_exercicios/sobre_listas/ex_23/relatório.txt"

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


if __name__ == '__main__':

    gerar_relatorio(ler_arquivo())
