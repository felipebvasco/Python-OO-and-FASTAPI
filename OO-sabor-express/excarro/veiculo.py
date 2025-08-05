class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._inicializado = False
    
    def __str__(self):
        return f'Marca: {self._marca}\nModelo: {self._modelo}\nLigado: {self.inicializado}'
    
    @property
    def inicializado(self):
        return 'Sim' if self._inicializado else 'Não'
    
    def ligar_desligar_veiculo(self):
        self._inicializado = not self._inicializado
        
