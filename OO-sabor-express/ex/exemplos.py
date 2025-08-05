# nome = 'Felipe'
# idade = 20

# print(f'\nMeu nome é {nome} e eu tenho {idade} anos\n')

# nome = 'felipe luis'
# nome1 = 'lucas marques'
# nome2 = 'gabriel molo'

# print(f'{nome} | {nome1} | {nome2}\n')

# nome = nome.title()
# nome1 = nome1.title()
# nome2 = nome2.title()

# print(f'{nome} | {nome1} | {nome2}\n')

# import os #importa biblioteca

# limpa_console()
#     os.system('clear') # Limpa o console
#     pass

# limpa_console()

# def escolher_opcao_match():
#     opcao_escolhida = int(input('Escolha uma opção: '))
#     match opcao_escolhida:
#         case 1:
#             print('Cadastrar Restaurante')
#         case 2:
#             print('Listar Restaurantes')
#         case 3:
#             print('Ativar Restaurante')
#         case 4:
#             finalizar_app()
#         case _:
#             print('Opcão inválida')
#             escolher_opcao_match()

#   try:
#         opcao_escolhida = int(input('Escolha uma opção: '))
#         if opcao_escolhida == 1:
#             cadastrar_novo_restaurate()
#         elif opcao_escolhida == 2:
#             lista_restaurantes()
#         elif opcao_escolhida == 3:
#             alterar_estado_do_restaurante()
#         elif opcao_escolhida == 4:
#             finalizar_app()
#         else:
#             opcao_invalida()
#     except:
#         opcao_invalida()

# lista = ['x', 'y', 'z', 'a', 'b', 'c']
# for letras in lista:
#     print(letras)

# Dicionario [{}]

# lampada = False #apagada
# print(lampada)
# lampada = not lampada
# print(lampada)

# dicionario = {'nome' : 'Felipe', 'curso' : 'ADS'}
# print(dicionario)
# dicionario.update({'nome' : 'Hermerson'})
# print(dicionario)

class Pessoa:
    
    def __init__(self, nome, idade, profissao):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao
        self._vivo = True
    
    def __str__(self):
        return f'Nome: {self._nome}\nIdade: {self._idade}\nProfissão: {self._profissao}\nVivo: Sim' if self._vivo else f'Nome: {self._nome}\nIdade: {self._idade}\nProfissão: {self._profissao}\nVivo: não'

p1 = Pessoa('Lucas', 24, 'Pedreiro')
print(p1)


