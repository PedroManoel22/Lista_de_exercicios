'''
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto,
faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. 
Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, 
entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado,
o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:

O total de votos computados; Os númeos e respectivos votos de todos os jogadores que receberam votos; O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.

Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. 
O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. 
Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. 
Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. 
Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo 
texto no disco, obedecendo a mesma disposição apresentada na tela.

Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.


Jogador         Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
'''
def main():
    total_votos = 0
    jogadores = []

    while True:

        try:
            voto = input('Digite qual jogador foi melhor: ')
            voto_int = int(voto)
        
            if voto_int == 0:
                break

            elif voto_int > 23 or voto_int < 1:
                print('\033[1;31mPor favor coloque um número entre 1 a 23\033[m')

            else:
                jogadores.append(voto_int)
                total_votos +=1
        except ValueError:
            print('\033[1;31mPor favor coloque um número válido!\033[m')


    jogadores_nao_repetidos = set(jogadores)
    linhas_saida = ['\nResultados das votações:\n']
    linhas_saida.append('Foram computados {total_votos} votos.\n')
    linhas_saida.append(f'{'Jogador':>5}{'votos':>15}{'%':>16}')
    porcentagens = []
    for jogador in jogadores_nao_repetidos:
        total_jogador = jogadores.count(jogador)
        porcentagem_jogador = (total_jogador/total_votos) * 100
        linhas_saida.append(f'{jogador:>5}{total_jogador:>15}{porcentagem_jogador:>20.1f} %\n')
        porcentagens.append(round(porcentagem_jogador, 1))

    indice = porcentagens.index(max(porcentagens))
    linhas_saida.append(f'O melhor jogador foi o camisa {indice +1}, com {max(porcentagens)}%')

    saida_formatada = "\n".join(linhas_saida)
    print(saida_formatada)
    try:
        nome_arquivo = 'C:\\Users\\Pedro\\Documents\\GitHub\\lista_de_exercicios\\Lista_de_exercicios\\sobre_listas\\resultado_enquete.txt'
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(saida_formatada)
        print(f"\nDados salvos com sucesso no arquivo '{nome_arquivo}'.")
    except IOError as e:
        print(f"\nErro ao salvar o arquivo: {e}")

if __name__ == "__main__":
    main()