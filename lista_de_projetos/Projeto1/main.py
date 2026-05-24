# Projeto 01
# Controle de cotas de disco

# Controle de cotas de disco. A ACME Inc., uma organização com mais de 1500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço em disco ocupado pelas contas dos usuários, e identificar os usuários com maior espaço ocupado. Através de um aplicativo baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado usuarios.txt:

# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o primeiro campo corresponde ao login do usuário e o segundo ao espaço em disco ocupado pelo seu diretório home. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado relatório.txt, no seguinte formato:

# ACME Inc.           Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso

# 1    alexandre       434,99 MB            16,85%
# 2    anderson       1187,99 MB            46,02%
# 3    antonio         117,73 MB             4,56%
# 4    carlos           87,03 MB             3,37%
# 5    cesar             0,94 MB             0,04%
# 6    rosemary        752,88 MB            29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

# Recursos adicionais

# Opcionalmente, desenvolva as seguintes funcionalidades:

# 1 Ordenar os usuários pelo percentual de espaço ocupado
# 2 Mostrar apenas os n primeiros em uso, definido pelo usuário
# 3 Gerar a saída numa página html
# 4 Criar o programa que lê as pastas e gera o arquivo inicial


def gerar_relatorio_html(caminho_txt: str, caminho_output: str) -> None:

    html_rows: list[str] = []

    # 1. Cabeçalho do HTML (Mantendo seu estilo)
    html_template_top = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Relatório de Uso</title>
    <style>
        .table-body { display: flex; flex-direction: column; }
        .user-row { display: flex; gap: 15px; border-bottom: 1px solid #333; padding: 5px; }
        .col-number { color: #f8f8f2; }
        .col-name { color: #e6db74; width: 150px; }
        .col-space { color: #ae81ff; width: 100px; }
        .col-percent { color: #38bdf8; }
    </style>
</head>
<body>
    <h1>Relatório de Uso de Disco</h1>
    <div class="table-body">
"""

    html_rows = []

    # 2. Processamento dos dados
    try:
        with open(caminho_txt, "r", encoding="utf-8") as file:
            # Pula as linhas de cabeçalho do TXT (ajuste conforme a necessidade)
            linhas = file.readlines()[5:]

            for linha in linhas:
                partes = linha.split()
                if len(partes) >= 4:
                    # Desempacotamento de lista (Pythonic way)
                    numero, nome, espaco, unidade, percentual = (
                        partes[0],
                        partes[1],
                        partes[2],
                        partes[3],
                        partes[4],
                    )

                    # Cria a linha formatada
                    row = (
                        f'        <div class="user-row">\n'
                        f'            <span class="col-number">{numero}</span>\n'
                        f'            <span class="col-name">{nome}</span>\n'
                        f'            <span class="col-space">{espaco} {unidade}</span>\n'
                        f'            <span class="col-percent">{percentual}</span>\n'
                        f"        </div>"
                    )
                    html_rows.append(row)

    except FileNotFoundError:
        print(f"Erro: Arquivo {caminho_txt} não encontrado.")
        return

    # 3. Fechamento e Salvamento
    html_template_bottom = "\n    </div>\n</body>\n</html>"

    full_html = html_template_top + "\n".join(html_rows) + html_template_bottom

    with open(caminho_output, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Sucesso! Relatório gerado em: {caminho_output}")


if __name__ == "__main__":
    gerar_relatorio_html(
        "Lista_de_exercicios/lista_de_projetos/Projeto1/relatorio.txt", "index.html"
    )
