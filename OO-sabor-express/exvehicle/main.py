from carro import Carro

c1 = Carro('Honda', 'Civic', 'Preto')
c2 = Carro('Renault', 'Kwid', 'Azul')
c3 = Carro('Mitsubishi', 'Lancer', 'Branca')

print(c1)
print()
print(c2)
print()
print(c3)

c1.listar_informacoes()
c2.listar_informacoes()
c3.listar_informacoes()

print()

c1.ligar()
c1.listar_informacoes()