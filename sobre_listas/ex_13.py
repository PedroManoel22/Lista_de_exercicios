# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, ...).

meses = ['janeiro', 'fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
medias_meses = []

for i in range(1, 13):

    while True:

        try:

            temp = input(f'Insira a média do mês de {meses[i-1]}: ')
            tem_float = float(temp)
            medias_meses.append(tem_float)
            break
    
        except ValueError:

            print('\033[1;31mPor valor coloque uma temperatura válida!\033[m')
            

        except Exception as e:

            print(f'Erro desconhecido \033[1;31m{e.__class__.__name__}\033[m')
            break


media_anual = sum(medias_meses) / 12
print(f'A média anula foi de {media_anual:.2f}')
medias_maiores = []
for i in range(len(medias_meses)):

    if medias_meses[i] > media_anual:

        medias_maiores.append(meses[i])

print('Meses que tiveram a média maior que a média anual: ')
print(*medias_maiores, sep='\n')
