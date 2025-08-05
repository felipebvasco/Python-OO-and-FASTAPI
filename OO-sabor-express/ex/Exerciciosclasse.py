#Exercício 1

class ContaBancaria:

    def __init__(self, titular='', saldo=0.0,):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False
        self._saldo = str(self._saldo)
    
    def __str__(self):
        #print(f'{'Titular'.ljust(25)} | {'Saldo'.ljust(10)} | {'Estado'}')
        return f'{self._titular.ljust(25)} | {self._saldo.ljust(10)} | {self._ativo}'
    
    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    def ativar_conta(self):
        self._ativo = not self._ativo

conta1 = ContaBancaria('Pedro Ricardo', 12345.99)
conta2 = ContaBancaria('Maria Fernanda', 8765.12)
print(f'Titular da conta 4: {conta1._titular}')
print(conta2)
conta1.ativar_conta()
print(conta1)