# Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class Televisao:
    NUM_CANAIS = 10
    canais = [x for x in range(1, NUM_CANAIS)]
    print(canais)
    def __init__(self, num_canal = 1):
        self.num_canal = num_canal
        self.volume = 1
        if self.num_canal not in self.canais:
            print(f'Canal {num_canal} não existe!')
    
    def aumentar_volume(self):
        limite = 20
        if self.volume < limite:
            print(f'volume da tv foi aumentado!')
            self.volume += 1
            print(f'Agora o volume está em {self.volume}')
        
        else:
            print('\033[1;31mO volume da TV já está no máximo\033[m')
    

    def diminuir_volume(self):
        limite = 0
        if self.volume > 0:
            print('Volume da tv foi diminuido!')
            self.volume -= 1
            print(f'Agora o volume da tv está em {self.volume}')
        
        else:
            print('\033[1;31mO volume da tv já está minimo!\033[m')


    def mostrar_informacoes(self):
        print(f'\033[1;36mA tv está no canal {self.num_canal} e seu volume está no {self.volume}\033[m')
    

    def mudar_canal_mais(self):
        ultimo_canal = max(self.canais)

        if self.num_canal < ultimo_canal:
            self.num_canal += 1
            print(f'Canal mudado para o {self.num_canal}')
        
        else:
            print(f'\033[1;31mNão existe mais canais acima do canal {self.num_canal}\033[m')
    

    def mudar_canal_menos(self):
        primeiro_canal = min(self.canais)
        if self.num_canal > primeiro_canal:
            self.num_canal -= 1
            print(f'Canal mudado para o {self.num_canal}')
        
        else:
            print(f'\033[1;31mNão existe mais canais abaixo do canal {self.num_canal}\033[m')
    


        
tv = Televisao()
tv.aumentar_volume()
tv.aumentar_volume()
tv.mostrar_informacoes()
tv.mudar_canal_mais()
tv.mostrar_informacoes()
tv.mudar_canal_mais()
tv.mostrar_informacoes()
tv.mudar_canal_mais()
