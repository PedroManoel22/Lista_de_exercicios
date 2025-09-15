#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
# e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".



def valida_resposta(pergunta):
   
    while True:
        try:
            resposta = input(pergunta).upper().strip()[0]
            if resposta in 'SN':
                return resposta
            else:
                print('Coloque apenas [S] ou [N].')
        except (IOError, IndexError):
            print('Coloque apenas [S] ou [N].')

def perguntas_investigacao():
    
    perguntas = [
        "Telefonou para a vítima? ",
        "Esteve no local do crime? ",
        "Mora perto da vítima? ",
        "Devia para a vítima? ",
        "Já trabalhou com a vítima? "
    ]

    respostas = []
    print("Responda apenas [S] para Sim ou [N] para Não.\n")
    for pergunta in perguntas:
        resposta = valida_resposta(pergunta)
        respostas.append(resposta)

    pontos = respostas.count('S')

    if pontos == 5:
        return "Assassino" 
    elif pontos == 3 or pontos == 4:
        return "Cúmplice"
    elif pontos == 2:
        return "Suspeito"
    else:
        return "Inocente"

if __name__ == '__main__':
    resultado = perguntas_investigacao()
    print(f"O resultado da investigação é: {resultado}")
