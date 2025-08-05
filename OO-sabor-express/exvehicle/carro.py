from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor
    
    def __str__(self):
        return self._modelo

    def ligar(self):
        self._ligado = True
    
    def listar_informacoes(self):
        print(f'Marca: {self._marca} | Modelo: {self._modelo} | Cor: {self._cor} | Estado: {self.ligado}')
    
    @property
    def ligado(self):
        return 'Carro Ligado' if self._ligado else 'Carro Desligado'
