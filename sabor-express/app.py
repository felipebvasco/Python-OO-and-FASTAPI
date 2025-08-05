import os

restaurantes = [{'nome':'Praça', 'categoria':'japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Italiana','ativo':True},
                {'nome':'Cantina','categoria':'italiano','ativo':False}]

def exibir_nome_do_programa():
    '''Essa função é responsável por sempre que chamada mostrar o nome da aplicação na tela'''
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")

def exibir_opcoes():
    '''Essa função é responsável por, sempre que chamada, mostrar as opções na tela'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função é responsável por mostrar na tela a frase de finalizar o app e, apóa isso, fechar o aplicação'''
    exibir_subtitulo('Finalizando o app!')

def voltar_ao_menu_principal():
    '''essa função é responsável por pedir pro usuário clicar em qualquer tecla 
    e, após isso, mandá-lo ao menu principal da aplicação'''
    input('Digite uma tecla para voltar ao menu\n')
    main()

def exibir_subtitulo(texto):
    '''Essa função é responsável por mostrar o subtítulo da tela e formatá-la de
    maneira mais agradável aos olhos'''
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    '''Essa função é responsável por dizer ao usuário que a opção escolhida
    é inválida e após isso, mandá-lo ao menu principal.'''
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurate():
    '''Essa função é responsável por cadastrar uma novo restaurante
    
    Inputs:
    - Nome do Restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes!')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def lista_restaurantes():
    '''Essa função é responsável por listar os restaurantes
    suas categorias e se estão ativos ou não cadastrados no sistema
    
    
    Inputs:
    -
    
    Outputs:
    - Restaurante
    - Categoria
    - Estado
    '''
    exibir_subtitulo('Listando Restaurantes')
    print(f'{'Nome do Restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | {'Status'}')  
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        estado_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {estado_restaurante}')
    print('\nListagem completa!\n\n')
    voltar_ao_menu_principal()

def alterar_estado_do_restaurante():
    '''Essa função é responsável por ativar ou desativas restaurantes no sistema
    
    Inputs:
    - Nome do Restaurante
    
    Outputs:
    -Alteração no Estado do Restaurante'''


    exibir_subtitulo('Alternando estado do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função é responsável por deixar o usuário escolher o que
    ele quer fazer dentro da aplicação e enviá-lo para opção escolhida
    
    Inputs:
    - Seleção de opção (1-4)
    
    Outputs:
    - Função referente a opção selecionada'''
    
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurate()
        elif opcao_escolhida == 2:
            lista_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def escolher_opcao_match():
    opcao_escolhida = int(input('Escolha uma opção: '))
    match opcao_escolhida:
        case 1:
            print('Cadastrar Restaurante')
        case 2:
            print('Listar Restaurantes')
        case 3:
            print('Ativar Restaurante')
        case 4:
            finalizar_app()
        case _:
            print('Opcão inválida')
            escolher_opcao_match()

def main():
    '''Essa função é responsável por fazer o loop principal
    dentro da aplicação permitindo o usuário continuar na mesma'''
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    '''Define que, caso essa seja a aplicação main, que vai chamar a função
    do loop'''
    main()