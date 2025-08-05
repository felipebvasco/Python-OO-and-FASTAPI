#Exercício 1
def de_um_a_dez():
    onetoten = []
    for i in range(11):
        i + 1
        onetoten.append(i)
    print(onetoten)

def lista_de_quatro_nomes():
    nomes4 = []
    contador = 0
    while contador < 4:
        nome = input('Insira aqui o nome para adicionar à lista: ')
        contador += 1
        nomes4.append(nome.capitalize())
    print(nomes4)

def anoscontados():
    anos = []
    anonasc = int(input('Digite o ano que você nasceu: '))
    anoatual = int(input('Digite o ano em que estamos: '))
    anos.append(anonasc)
    anos.append(anoatual)
    print(anos)


#Exercício 2
def listar_compras():
    compras = ['Sabonete, Shampoo, Pepino, Tomate, Alface, Arroz, Feijão']
    for produtos in compras:
        print(f'-{produtos}')


#Exercício 3
#Esse usa uma variável declarada a mais para somar (feito com while)
def soma_impares():
    regressivo = 10
    soma = 0
    while regressivo >= 1:
        if (regressivo % 2) == 1:
            soma += regressivo
        regressivo -= 1    
    print(soma)

#Esse usa uma variável declarada a menos porém usa o I do laço pra somar (feito com For)
def soma_impares2():
    soma1 = 0
    for i in range (11):
        if (i % 2) == 1:
            soma1 += i
    print(soma1)


#Exercício 4
def contagem_regressiva():
    countdown = 10
    while countdown >= 1:
        print(countdown)
        countdown -= 1


#Exercício 5
def gera_tabuada():
    numero = int(input('Insira o númeo desejada pra descobrir sua tabuada: '))
    for i in range(11):
        print(f'{numero} x {i} = {numero * i}')


#Exercício 6
def soma_lista_user():
    numeros_soma = []
    continuar = 1
    total = 0
    while continuar == 1:
        numeros_soma.append(input('Digite um número para adicionar à lista: '))
        continuar = (int(input('Deseja Continuar?\n1 - Sim\n2 - Não\n')))
    try:
        for numero in numeros_soma:
            total += int(numero)
        print(total)
    except:
        print('Há dados na lista que não são Números, reinsira os dados novamente')