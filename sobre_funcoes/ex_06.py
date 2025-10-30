# Exercício 06
# Faça um programa que converta a notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M.

# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.

# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. 
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas às vezes que desejar.

def entrada():
    while True:
        # valida hora
        try:
            hora = input('Insira as horas: ')
            hora_int = int(hora)

            if hora_int > 12 and hora_int <= 24:
                conversao = 'P'

            elif hora_int <= 12 and hora_int >= 0:
                conversao = 'A'

            else:
                print('\033[1;31;41mColoque uma hora válida!\033[m')
                continue

            # valida minuto
            try:
                minuto = input('Insira os minutos: ')
                minuto_int = int(minuto)

                if minuto_int > 59 or minuto_int < 0:
                    print('\033[1;33mminuto inválido, por favor coloque um valor entre 0 a 59\033[m')

                else:

                    saida(hora_int, conversao, minuto_int)
                    while True:
                        continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]

                        if continuar == 'N':
                            break

                        elif continuar == 'S':
                            break
                        
                        else:
                            print('Por favor coloque um resposta válida!')
                    if continuar == 'N':
                         break

            
            except ValueError:
                print('por favor coloque um número inteiro!')

        except ValueError:
            print('\033[1;31mPor favor insira um valor inteiro!\033[m')

   

def saida(hora, conversao, minutos):
    print(f'antes: {hora}:{minutos}')

    if conversao == 'A':
        manha_tarde = 'A.M'
        print(f'Depois: {hora}:{minutos} {manha_tarde}') 

    else:
        manha_tarde = 'P.M'
        hora = hora - 12
        print(f'Depois: {hora}:{minutos} {manha_tarde}') 



if __name__ == '__main__':
    entrada()
    print('Obrigado, volte sempre!🥰')
