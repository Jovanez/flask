from banco import Cinema,Filme, Programacao,db

db.connect()

cine = Cinema.select(Cinema).where((Programacao.filme == 3)& (Programacao.cinema == Cinema.codigo)).join(Programacao).join(Filme).group_by(Cinema.codigo)

for c in cine:
    print(c.nome +" \n")