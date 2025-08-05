from carro import Carro
from moto import Moto

c1 = Carro('Toyota', 'Supra', 4)
c2 = Carro('Renault', 'Logan', 4)
c3 = Carro('Renault', 'Kwid', 4)

m1 = Moto('Honda', 'CJ 600', 'Esportiva')
m2 = Moto('Yamaha', 'XP 1200', 'Esportiva')
m3 = Moto('Kawasaki', 'Ninja', 'Casual')

print(c1)
print()
print(c2)
print()
print(c3)
print()
print(m1)
print()
print(m2)
print()
print(m3)
print()
c1.ligar_desligar_veiculo()
print(c1)