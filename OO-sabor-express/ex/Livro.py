class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo.title()
        self._autor = autor.title()
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
    
    def __str__(self):
        return f'\nTitulo: {self._titulo}\nAutor: {self._autor}\nAno de Publicação: {self._ano_publicacao}\n'

    def emprestar(self):
        self._disponivel = not self._disponivel
    
    def livro_disp(self):
        return 'Disponível' if self._disponivel else 'Indisponível'
        # return print('Disponível') if self._disponivel else print('Indisponível')
    
    @staticmethod
    def verificar_disponibilidade(ano_publicacao):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano_publicacao and livro._disponivel]
        for livro in livros_disponiveis:
            print(f'{livro._titulo}')
        print('')
        return livros_disponiveis

print(dir(Livro))
#Livro é o nome da classe
    


