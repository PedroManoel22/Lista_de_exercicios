#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
# e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
pergunta_1 =  "Telefonou para a vítima?"
while True:
    try:

        p1 = input('Telefonou para a vítima? ').upper().strip()[0]
        p2 = input('Esteve no local do crime? ').upper().strip()[0]
        p3 = input('Mora perto da vítima? ').upper().strip()[0]
        p4 = input('Devia para a vítima? ').upper().strip()[0]
        p5 = input('Já trabalhou com a vítima? ').upper().strip()[0]

        if p1 in 'SN' and p2 in 'SN' and p3 in 'SN' and p4 in 'SN' and p5 in 'SN':

            resp_1 = p1
            resp_2 = p2
            resp_3 = p3
            resp_4 = p4
            resp_5 = p5

            break

        else:

            print('\033[1;31mColoque apenas\033[m \033[0;49;96msim\033[m \033[1;31mou\033[m \033[0;49;96mnão\033[m')



    except IndexError:

        print('\033[1;31mPorfavor coloque alguma resposta!\033[m')

print(resp_1)
print(resp_2)
print(resp_3)
print(resp_4)
print(resp_5)

    