class Musica2:
    nome = ''
    artista = ''
    duracao = int
    playlist = []
    
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica2.playlist.append()
    
    def __str__(self):
        return f'{self.nome} | {self.artista}'
    
    def listar_musicas():
        for musica in Musica2.playlist:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')
    
continuar = 1
idmusica = 'objeto'
while continuar == 1:
    nome = str(input('Insira o nome da música:\n'))
    artista = str(input('\nInsira o nome do artista:\n'))
    duracao = int(input('\nInsira a duração da música em segundos:\n'))
    idmusica = (nome, artista, duracao)
    idmusica += 1
    continuar = int(input('Deseja continuar inserindo músicas?\n1 - Sim\n2 - Não'))

Musica2.listar_musicas()
