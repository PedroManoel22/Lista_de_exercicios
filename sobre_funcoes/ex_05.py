# Exercício 05
# Faça um programa com uma função chamada soma_imposto. A função possui dois parâmetros formais: 
# taxa_imposto, que é a quantia de imposto sobre vendas expressas em porcentagem, e custo, que é o custo de um item antes do imposto.
# A função "altera" o valor de custo para incluir o imposto sobre vendas.

def soma_imposto(taxa_imposto, custo):
    taxa = taxa_imposto / 100
    novo_custo =  custo + (custo * taxa)
    return f'Custo anterior: {custo}\nNovo custo com taxa de {taxa_imposto}% de imposto: {round(novo_custo, 2)}'


taxa = 5
custo = 100
print(soma_imposto(taxa, custo))
