# Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

# Atributos: Nome, Fome, Saúde e Idade b.
# Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde,
# ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
# 100 anos será a idade maxima do nosso tamagushi

class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    

    def alterar_nome(self):
        self.nome = pede_valida_nome(alterar=True, nome_antigo=self.nome)
        
        print('\n\033[1;32mNome alterado com sucesso!\n\033[m')
    

    def alterar_fome(self):
        self.fome = pede_valida_fome(alterar=True, fome_antiga=self.fome)

        print('\n\033[1;32mFome alterada com sucesso!\033[m')
    

    def alterar_saude(self):
        self.saude = pede_valida_saude(alterar=True, saude_antiga=self.saude)
        print('\n033[1;32mSaúde alterada com sucesso!\033[m')
    

    def alterar_idade(self):
        self.idade = pede_valida_idade(alterar=True, idade_antiga=self.idade)
    

    

        
# nome ok

def pede_valida_nome(alterar=False, nome_antigo='nenhum'):
    if not alterar:
        # pede o nome a primeira vez
        while True:
            nome = input('Insira o nome do seu tamagushi: ')

            if len(nome) <= 2:
                print('\n\033[1;31mO nome do seu tamagushi deve ter mais de 2 caracteres!\n'
                    'Tente novamente....\033[m\n')
                continue
            
            elif nome.isdigit():
                print('\n\033[1;31mO nome do seu tamagushi não pode ser apenas números!\n'
                    'Tente novamente....\033[m\n')
                continue
            
            else:
                return nome


    else:
        # altera o nome
        while True:
            print('\n\033[1;36m----Alterando o nome do seu tamagushi----\033[m')
            nome = input('\nInsira o novo nome para o seu tamagushi: ')

            if len(nome) <= 2:
                print('\n\033[1;31mO nome do seu tamagushi deve ter mais de 2 caracteres!\n'
                    'Tente novamente....\033[m\n')
                continue
            
            elif nome.isdigit():
                print('\n\033[1;31mO nome do seu tamagushi não pode ser apenas números!\n'
                    'Tente novamente....\033[m\n')
                continue

            elif nome == nome_antigo:
                print('\n\033[1;31mO novo nome não pode ser igual ao anterior!\033[m\n')
            
            else:
                return nome
            
# fome ok            
def pede_valida_fome(alterar=False, fome_antiga=0):
    fome_valida = [x for x in range(0, 101)]

    if not alterar:
        # pede fome primeira vez
        while True:
            try:
                fome = int(input('Insira a fome do seu tamagushi: '))

                if fome not in fome_valida:
                    print('\033[1;31mPor favor coloque uma fome entre 0 a 100!\n'
                      'Tente novamente...\033[m\n')
        
                else:
                    return fome
    
        
            except ValueError:
                print('\n\033[1;31mPor favor insira um valor inteiro!\n\033[m')

    else:
        # alterar valor fome
        while True:
            print('\n\033[1;36m----Alterando a fome do seu tamagushi----\033[m')
            try:
                fome = int(input('\nInsira o novo nivel de fome do seu tamagushi: '))

                if fome not in fome_valida:
                    print('\033[1;31mPor favor coloque uma fome entre 0 a 100!\n'
                        'Tente novamente...\033[m\n')
                
                elif fome == fome_antiga:
                    print('\n\033[1;31mVocê não alterou a fome, coloque um valor difrente do anterior!\033[m')
            
                else:
                    return fome
        
            except ValueError:
                print('\n\033[1;31mPor favor insira um valor inteiro!\n\033[m')

# saude ok
def pede_valida_saude(alterar=False, saude_antiga=0):
    saude_valida = [x for x in range(0, 101)]

    # Pede a saúde a primeira vez
    if not alterar:
        while True:
            try:
                saude = int(input('Insira a saúde do seu tamagushi: '))

                if saude not in saude_valida:
                    print('\033[1;31mPor favor coloque a saúde entre 0 a 100!\n'
                        'Tente novamente...\033[m\n')
            
                else:
                    return saude
        
            except ValueError:
                print('\n\033[1;31mPor favor insira um valor inteiro!\n\033[m')
    
    # altera a saúde
    else:
         while True:
                print('\n\033[1;36m----Alterando o valor da saúde----\033[m')

                try:
                    saude = int(input('\nInsira o novo valor da saúde do seu tamagushi: '))

                    if saude not in saude_valida:
                        print('\033[1;31mPor favor coloque a saúde entre 0 a 100!\n'
                        'Tente novamente...\033[m\n')
                    
                    elif saude == saude_antiga:
                        print('\n\033[1;31mA saúde deve ser diferente da antiga!\033[m')
            
                    else:
                        return saude
        
                except ValueError:
                    print('\n\033[1;31mPor favor insira um valor inteiro!\n\033[m')


def pede_valida_idade(alterar=False, idade_antiga=0):
    idade_valida = [x for x in range(0, 101)]

    # pede idade primeira vez
    if not alterar:
        while True:
            try:
                idade = int(input('Insira a idade do seu tamagushi: '))

                if idade not in idade_valida:
                    print('\033[1;31mPor favor coloque uma idade entre 0 a 100!\n'
                        'Tente novamente...\033[m\n')
            
                else:
                    return idade
        
            
            except ValueError:
                print('\n\033[1;31mPor favor insira um valor inteiro!\n\033[m')
    
    else:
        while True:
            print('\n\033[1;36m----Alterando a idade do tamagushi----\033[m')

            try:
                idade = int(input('Insira a idade do seu tamagushi: '))

                if idade not in idade_valida:
                    print('\033[1;31mPor favor coloque uma idade entre 0 a 100!\n'
                        'Tente novamente...\033[m\n')
                
                elif idade == idade_antiga:
                    print('\n\033[1;31mColoque a idade diferente da anterior!\033[m')
            
                else:
                    return idade
        
            
            except ValueError:
                print('\n\033[1;31mPor favor insira um valor inteiro!\n\033[m')
    


if __name__ == '__main__':
    nome = pede_valida_nome()
    fome = pede_valida_fome()
    saude = pede_valida_saude()
    idade = pede_valida_idade()

    meu_tamagushi = Tamagushi(nome, fome, saude, idade)

    meu_tamagushi.alterar_nome()
    meu_tamagushi.alterar_fome()
    meu_tamagushi.alterar_saude()
    meu_tamagushi.alterar_idade()
    
    

