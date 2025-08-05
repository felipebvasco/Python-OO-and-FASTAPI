class Musica:
    nome = ''
    artist = ''
    duracao = int

musica1 = Musica()
musica1.nome = "There's nothing holding me back"
musica1.artist = 'Nichola Tesla'
musica1.duracao = 220

musica2 = Musica()
musica2.nome = 'Metro exodus'
musica2.artist = 'Romero Brito'
musica2.duracao = 340

musica3 = Musica()
musica3.nome = 'Whenever a lost my mind'
musica3.artist = 'Crystal'
musica3.duracao = 290

print(f'Primeira música é: |{musica1.nome}| do artista |{musica1.artist}| e tem |{musica1.duracao}| segundos de duração')
print(f'Segunda música é: |{musica2.nome}| do artista |{musica2.artist}| e tem |{musica2.duracao}| segundos de duração')
print(f'Terceira música é: |{musica3.nome}| do artista |{musica3.artist}| e tem |{musica3.duracao}| segundos de duração')