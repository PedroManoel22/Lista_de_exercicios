# Exercício 05
# Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta,
# nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
# com valor default zero e os demais atributos são obrigatórios.
# o número da conta deve seguir o seguinte padrão -> xxxxxxxx-xx

import re

class ContaCorrente:
    padrao_num_conta = re.compile(r'\d{8}-\d{2}')
    padrao_nome = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s'-]+$", re.UNICODE)

    def __init__(self, num_conta, nome_correntista, saldo=0):
        valido = self.padrao_num_conta.findall(num_conta)

        # valida num_conta
        if not valido:
            print('\n\033[1;31mPadrão da conta errado!\033[m')
            print('Por favor insira o número da conta no seguinte padrão: xxxxxxxx-xx\n')
            pede_conta()

        # Valida nome_correntista
        if not self.padrao_nome.match(self.nome_correntista):
            print('O nome possui caracteres errados!')
            pede_nome()
            
            
        
        else:
            self.nome_correntista = nome_correntista
        self.num_conta = num_conta
        self.saldo = saldo


def pede_conta():
        return input('Insira o número da sua conta: ')


def pede_nome():
        return input('Insira o nome do correntista: ')


def criar_conta():
    conta = None

    while conta is None:
        try:
            num_conta = pede_conta()
            nome = pede_nome()
            conta = ContaCorrente(num_conta, nome)
            print('\033[1;32mTodos os dados estão válidos!')
        
        except ValueError as e:
             print('Erro de validação. Tente novamente. Detalhe: {e}')
    
    return conta



if __name__ == '__main__': 
    
    conta = criar_conta()
