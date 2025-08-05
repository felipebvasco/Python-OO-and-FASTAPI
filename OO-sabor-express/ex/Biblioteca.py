from Livro import Livro

l1 = Livro('Senhor dos Aneis', 'Tokien', 1993)
l2 = Livro('Como tocar piano', 'Steve Wonder', 1992)
l3 = Livro('Como treinar o seu dragão', 'Steve Wonder', 1992)
l4 = Livro('Como raspar a cabeça da sua avó', 'Steve Wonder', 1992)
l5 = Livro('Como enfiar uma chave de fenda...', 'Steve Wonder', 1992)
l6 = Livro('Por onde anda Patrick Estrela', 'Steve Wonder', 1992)
l7 = Livro('Cadu Maverick vs Gabriel Medina', 'Steve Wonder', 1992)
Livro.livros = [l1, l2, l3, l4, l5, l6, l7]


Livro.verificar_disponibilidade(1992)
l2.livro_disp()
l2.emprestar()
l2.livro_disp()
l4.emprestar()
l5.emprestar()

Livro.verificar_disponibilidade(1992)










