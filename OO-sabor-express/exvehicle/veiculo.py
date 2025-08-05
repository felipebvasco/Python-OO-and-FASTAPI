from abc import ABC, abstractmethod

class Veiculo(ABC):

    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False
    
    # def __str__(self):
        # return f'Seu veículo é um {self._marca} modelo {self._modelo}'
    
    @abstractmethod
    def ligar(self):
        pass
    
