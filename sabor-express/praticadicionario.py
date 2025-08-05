#Exercício1
def criar_dicionário():
    pessoas = [{'nome':'Pedro', 'idade':'15', 'cidade':'São Paulo'},
            {'nome':'Julia', 'idade':'22', 'cidade':'Chique-chique'},
            {'nome':'Maria', 'idade': '30', 'cidade':'Paranapiacaba'}]

    for pessoa in pessoas:
        nome_pessoa = pessoa['nome']
        idade_pessoa = pessoa['idade']
        cidade_pessoa = pessoa['cidade']
        print(f'{nome_pessoa.ljust(15)} | {idade_pessoa.ljust(15)} | {cidade_pessoa}')


#Exercício02
def depois_eu_arrumo():
    pessoas = [{'nome':'Pedro', 'idade':'15', 'cidade':'São Paulo'},
            {'nome':'Julia', 'idade':'22', 'cidade':'Chique-chique'},
            {'nome':'Maria', 'idade': '30', 'cidade':'Paranapiacaba'}]

    pessoas.update({'Profissao':'Engenheiro'})
    pessoas.update({'Profissao':'Médica'})
    pessoas.update({'Profissao':'Cientista'})

    for pessoa in pessoas:
            nome_pessoa = pessoa['nome']
            idade_pessoa = pessoa['idade']
            cidade_pessoa = pessoa['cidade']
            profissao_pessoa = pessoa['Profissao']
            print(f'{nome_pessoa.ljust(15)} | {idade_pessoa.ljust(15)} | {cidade_pessoa.ljust(15)} | {profissao_pessoa}')


#Exercício03
def dicion_quadrado():
    numeros_quadrados = {x: x**2 for x in range(1,6)}
    print(numeros_quadrados)


#Exercício04
def checar_chave():
    pessoas = [{'nome':'Pedro', 'idade':'15', 'cidade':'São Paulo'},
            {'nome':'Julia', 'idade':'22', 'cidade':'Chique-chique'},
            {'nome':'Maria', 'idade': '30', 'cidade':'Paranapiacaba'}]

    for pessoa in pessoas:
        if 'nome' in pessoa:
            print('Essa chave existe')
            break
        else:
            print('Essa chave não existe')
            break


#Exercício05
dicionario = {}
frase = str(input('Digite sua frase para contar cada palavra aqui:\n'))
palavras = frase.split()
print(palavras)
for palavra in palavras:
    dicionario[palavra] = dicionario.get(palavra, 0) + 1
print(dicionario)