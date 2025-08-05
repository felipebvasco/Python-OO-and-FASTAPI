#Exercício 1
def ex1():
    numero = int(input('Insira um número: '))
    if (numero % 2) == 0:
        print('Esse número é par!')
    else:
        print(('Esse número é ímpar'))

#Exercício 2
def ex2():
    idade = int(input('Insira sua idade: '))
    if idade >= 0 and idade <= 12:
        print('Criança')
    elif idade >= 13 and idade < 18:
        print('Adolescente')
    elif idade >= 18:
        print('Adulto')
    else:
        print('valor inválido')


#Exercício 3
def ex3():
    user = 'felipe'
    senha = 1312
    txtbox = str(input('Insira o nome de usuário:\n'))
    passbox = int(input('Insira sua senha (números)\n'))
    if (txtbox == user) and (passbox == senha):
        print('\nLogado com Sucesso')
    else:
        print('\nUsuário ou senha incorretos')


#Exercício 4
def ex4():
    x = int(input('Insira um valor para x: '))
    y = int(input('Insira um valor para y: '))
    if x > 0:
        if y > 0:
            print('Ponto escolhido no primeiro quadrante')
        elif y < 0:
            print('Ponto escolhido no quarto quadrante')
        else:
            print('Ponto escolhido no eixo Y')
    elif x < 0:
        if y > 0:
            print('Ponto escolhido no segundo quadrante')
        elif y < 0:
            print('Ponto escolhido no terceiro quadrante')
        else:
            print('Ponto escolhido no eixo Y')
    else:
        if y == 0:
            print('Ponto escolhido no ponto de origem')
        else:
            print('ponto escolhido no eixo x')




