#Exercício1
# class Carro:
#     modelo = ''
#     cor = ''
#     ano = int

# car1 = Carro()
# car1.modelo = 'Uno'
# car1.cor = 'Vinho'
# car1.ano = '2009'

# print(vars(car1))


#Exercício2

# class Restaurante:
#     nome = ''
#     categoria = ''
#     ativo = bool
#     nota = float
#     endereco = ''

# rest1 = Restaurante()
# rest1.nome = 'Pé de moleque'
# rest1.categoria = 'Doces Brasileiros'
# rest1.ativo = True
# rest1.nota = 9.5
# rest1.endereco = 'Av. Paulista n° 356'

# print(vars(rest1))


#Exercício3

# class Restaurante:
#     nome = ''
#     categoria = ''
#     ativo = bool
#     nota = float
#     endereco = ''

#     def __init__(self, nome, categoria):
#         self.nome = nome
#         self.categoria = categoria
#         self.ativo = False

# rest1 = Restaurante('Pé de moleque', 'Doces Brasileiros' )
# #  rest1.nota = 9.5
# #  rest1.endereco = 'Av. Paulista n° 356'

# print(vars(rest1))


#Exercício4

# class Restaurante:
#     nome = ''
#     categoria = ''
#     ativo = bool
#     nota = float
#     endereco = ''

#     def __init__(self, nome, categoria):
#         self.nome = nome
#         self.categoria = categoria
#         self.ativo = False

#     def __str__(self):
#         return f'{self.nome.ljust(15)} | {self.categoria}'

# rest1 = Restaurante('Pé de moleque', 'Doces Brasileiros' )
# #  rest1.nota = 9.5
# #  rest1.endereco = 'Av. Paulista n° 356'

# print(rest1)


#Exercício5

# class Cliente:
#     clientes = []
#     nome = ''
#     cpf = int
#     endereco = ''
#     novo = bool

#     def __init__(self, nome, cpf, endereco, novo):
#         self.nome = nome
#         self.cpf = cpf
#         self.endereco = endereco
#         self.novo = novo
#         Cliente.clientes.append(self)
    
#     def listar_clientes():
#         print('\nNome do Cliente'.ljust(19), '|', 'CPF'.ljust(10), '|', 'Endereço'.ljust(18), '|', 'Novo')
#         for ct in Cliente.clientes:
#             print(f'{ct.nome.ljust(18)} | {ct.cpf} | {ct.endereco.ljust(18)} | {ct.novo}')

# c1 = Cliente('Pedro', 1234567890, 'Rua Pindamonhagaba', True)
# c2 = Cliente('Maria', 9876543210, 'Av. Água Fria', False)
# c3 = Cliente('João', 1029384756, 'Av. Santo Amaro', True)

# Cliente.listar_clientes()