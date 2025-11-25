
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

        if self.saude == 0:
            return 'morto'
        
        else:
            print('\n\033[1;32mSaúde alterada com sucesso!\033[m')
    

    def alterar_idade(self):
        self.idade = pede_valida_idade(alterar=True, idade_antiga=self.idade)
    
    
    def ver_humor(self):
        print('\n----Humor do tamagushi----')
        # humor:
        # 0 a 25 = Triste,
        # 26 a 50 = Normal, 
        # 51 a 75 = Feliz, 
        # 76 a 100 = Muito feliz

        humor_possiveis = ['Triste', 'Normal', 'Feliz', 'Muito feliz']

        if self.saude == 0:
            print('\nSeu tamagushi não tem humor pois está morto')

        else:
            humor = self.saude - self.fome
            
            # Triste
            if humor >= 0 and humor <= 25:
                humor = humor_possiveis[0]
            
            # Normal
            elif humor >= 26 and humor <= 50:
                humor = humor_possiveis[1]
            
            # Feliz
            elif humor >= 51 and humor <= 75:
                humor = humor_possiveis[2]

            # Muito feliz
            elif humor >= 76 and humor <= 100:
                humor = humor_possiveis[3]
        
        print(f'\nSeu tamagushi está {humor}')
            

    def ver_dados(self):
        print('\n---Dados do tamagushi---\n')
        print(f'Nome: {self.nome}\n'
              f'Fome: {self.fome}\n'
              f'Saúde: {self.saude}\n'
              f'Idade: {self.idade}\n')
    

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
    
    # alterar idade
    else:
        while True:
            print('\n\033[1;36m----Alterando a idade do tamagushi----\033[m')

            try:
                idade = int(input('\nInsira a idade do seu tamagushi: '))

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

    if saude == 0:
        print('\nO seu tamagushi está morto 😥')
    
    else:

        # fazer o menu
        while True:
            print('\n-----Menu-----')
            opcoes = [1, 2, 3, 4 , 5, 6, 7]

            opcao = int(input('\n[1] Alterar_nome\n'
                        '[2] Alterar fome\n'
                        '[3] Alterar saúde\n'
                        '[4] Alterar idade\n'
                        '[5] Ver humor\n'
                        '[6] sair\n\n'
                        'Qual opção deseja? '))
            
        
            match opcao:
                case 1:
                    meu_tamagushi.alterar_nome()

                case 2:
                    meu_tamagushi.alterar_fome()

                case 3:
                    saude = meu_tamagushi.alterar_saude()
                    if saude == 'morto':
                        print('\nO seu tamagushi morreu 😥')
                        break

                case 4:
                    meu_tamagushi.alterar_idade()

                case 7:
                    meu_tamagushi.ver_dados()
                    
                case 5:
                    meu_tamagushi.ver_humor()
                        
                case  6:
                    break

                case _:
                    print('\n\033[1;31mPor favor insira uma opção válida!\033[m')
        
    print('\nObrigado e volte sempre! 🥰')
  