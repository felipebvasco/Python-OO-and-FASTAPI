class ClienteBanco:

    clientes = []

    def __init__(self, nome, nconta = 00000, saldo=0.0, end=''):
        self._nome = nome
        self._nconta = nconta
        self._saldo = saldo
        self._cartao = False
        self._end = end
        self._nconta = str(self._nconta)
        self._saldo = str(self._saldo)
        ClienteBanco.clientes.append(self)
    
    def __str__(self):
        return f'{self._nome.ljust(25)} | {self._nconta.ljust(6)} | {self._saldo.ljust(12)} | {self._cartao} | {self._end}'
   
    def ativarcartao(self):
        self._cartao = True        
    
    @classmethod
    def listarclientes(cls):
        print(f'{'Nome do Cliente'.ljust(25)} | {'Conta'.ljust(6)} | {'Saldo'.ljust(14)} | {'Crédito'} | {'Endereço do Cliente'}')
        for cliente in cls.clientes:
            print(f'{cliente._nome.ljust(25)} | {cliente._nconta.ljust(6)} | R${cliente._saldo.ljust(12)} | {cliente._cartao} | {cliente._end}')
    
    @classmethod
    def criar_conta(cls, titular, nconta, saldo, end):
        conta = ClienteBanco(titular, nconta, saldo, end)
        return conta
    
    @property
    def cartao(self):
        return 'Cartão' if self._cartao else 'S/ Cartão' 


cli1 = ClienteBanco('Lucas', 12345, 99.99, 'Rua maria Rita')
cli2 = ClienteBanco('Pedro', 23451, 250.99, 'Rua dos jacarandás mimosos')

ClienteBanco.listarclientes()
cli1.ativarcartao()
ClienteBanco.listarclientes()

conta_nova = ClienteBanco.criar_conta('Marques', 67322, 532.45, 'Av Paulista')
print(f"Conta de {conta_nova._nome} criada com saldo inicial de R${conta_nova._saldo}")

print('\n\n\n', cli1)