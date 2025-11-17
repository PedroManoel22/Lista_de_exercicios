# Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, 
# como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de
# computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. 
# Depois, faça um programa que peça um texto e transforme-o para a grafia leet speak.

# Substituição de letras
# Substituição direta: Troque letras por números ou símbolos que se assemelham graficamente.

# 'e' por '3'
# 'a' por '4'
# 's' por '$' ou '5'
# 't' por '7'
# 'o' por '0'
# 'eu' por '1'

# Substituição mais elaborada: Utilize uma tabela de tradução que pode incluir caracteres mais variados.

# 'A' pode se tornar '4', '/\', '@', '^' ou 'ä'
# 'B' pode se tornar '8' ou '6'
# 'G' pode se tornar '6' ou '9'
# 'Z' pode se tornar '2' ou '$' 

def gerar_leet_speak(texto):
    
    tabela_leet = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        's': '5',
        't': '7',
        'l': '1',
        'b': '8',
        'g': '6',
        'z': '2',
        'h': '#',
        'x': '%',
    }
    
    texto_leet = ''.join(tabela_leet.get(letra, letra) for letra in texto.lower())

    return texto_leet

if __name__ == '__main__':
    entrada_usuario = input('Digite um texto: ')
    resultado = gerar_leet_speak(entrada_usuario)
    print('\n~~~~~~~~Resultado~~~~~~~~')
    print(f'Texto original: {entrada_usuario}')
    print(f'Texto em L33t: {resultado}')
    ''