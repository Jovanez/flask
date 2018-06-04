from banco import Usuario, Sala, Genero, BandeiraCartao, TipoAudio,  Programacao, Uf, Cidade, Endereco, Cinema, \
    Filme, DiaSemana, TipoTela, Sessao, Ingresso, Compra, Cliente, Funcionario, db, Banner, TipoReclamacao, Reclamacoes

db.connect()

try:
    db.drop_tables(
        [Usuario, Cliente, BandeiraCartao, Funcionario, Sala, Genero, TipoAudio,  Programacao, Uf, Cidade,
         Endereco, Cinema, Filme, DiaSemana, TipoTela, Sessao, Compra, Ingresso, TipoReclamacao, Reclamacoes, Banner])

except:
    print("Nao foi possivel Deleta tabelas")
try:
    db.create_tables(
        [Usuario, BandeiraCartao, Cliente, Funcionario, Sala, Genero, TipoAudio,  Programacao, Uf, Cidade,
         Endereco, Cinema, Filme, DiaSemana, TipoTela, Sessao, Compra, Ingresso, TipoReclamacao, Banner, Reclamacoes])
except:
    print("Nao foi possivel Criar tabelas")

user1 = Usuario(login="admim", senha="admim123", perguntaSecreta="Qual melhor Amigo", resposta="Maria")
user2 = Usuario(login="cliente1", senha="111111", perguntaSecreta="Primeiro animal de Estimacao", resposta="foca")
user3 = Usuario(login="cliente2", senha="222222", perguntaSecreta="Primeiro Carro", resposta="fusca")
user1.save()
user2.save()
user3.save()

func1 = Funcionario(nome="Administrador ADM ADM",
                    cpf="000.000.000-00",
                    email="adm@adm.com",
                    usuario=user1)
func1.save()

cliente1 = Cliente(nome="Cliente Silva Silva",
                   cpf="123.123.123-12",
                   email="cliente1@cliente.com",
                   usuario=user2)
cliente2 = Cliente(nome="Cliente Souza Souza",
                   cpf="321.321.321-32",
                   email="cliente2@cliente.com",
                   usuario=user3)
cliente1.save(), cliente2.save()

bandeira1 = BandeiraCartao(bandeira="Visa")
bandeira2 = BandeiraCartao(bandeira="Master Card")
bandeira1.save(), bandeira2.save()

uf1 = Uf(sigla='ES', nome="Espirito Santo")
uf2 = Uf(sigla='RJ', nome="Rio de Janeiro")
uf3 = Uf(sigla='MG', nome="Minas Gerais")
uf1.save(force_insert=True)
uf2.save(force_insert=True)
uf3.save(force_insert=True)


cidade1 = Cidade(nome="Cachoeiro", uf=uf1)
cidade2 = Cidade(nome="Vitoria", uf=uf1)
cidade3 = Cidade(nome="Rio de Janeiro", uf=uf2)
cidade4 = Cidade(nome="Copacabana", uf=uf2)
cidade5 = Cidade(nome="Belo Horizonte", uf=uf3)
cidade6 = Cidade(nome="Ouro Preto", uf=uf3)
cidade1.save(), cidade2.save(), cidade3.save(), cidade4.save(), cidade5.save(), cidade6.save()

end1 = Endereco(cidade=cidade1, rua="Rua principal", numero=100, referencia="Perto do Bob's")
end2 = Endereco(cidade=cidade2, rua="Av Freitas Cardoso", numero=34, referencia="Apos a escola Municipal")
end1.save()
end2.save()

cine1 = Cinema(nome="Perim-Center", endereco=end1)
cine2 = Cinema(nome="Shopping Sul", endereco=end2)
cine1.save()
cine2.save()

genero1 = Genero(genero="Comedia")
genero2 = Genero(genero="Aventura")
genero3 = Genero(genero="Romance")
genero4 = Genero(genero="Terror")
genero1.save(), genero2.save(), genero3.save(), genero4.save()

tipoAudio1 = TipoAudio(tipoAudio="Dublado")
tipoAudio2 = TipoAudio(tipoAudio="Legendado")
tipoAudio1.save(), tipoAudio2.save()

sala1 = Sala(numero=1, capacidade=40, cinema=cine1)
sala2 = Sala(numero=2, capacidade=40, cinema=cine1)
sala3 = Sala(numero=3, capacidade=40, cinema=cine1)
sala4 = Sala(numero=4, capacidade=40, cinema=cine1)
sala5 = Sala(numero=1, capacidade=40, cinema=cine2)
sala6 = Sala(numero=2, capacidade=40, cinema=cine2)
sala7 = Sala(numero=3, capacidade=40, cinema=cine2)
sala1.save(), sala2.save(), sala3.save(), sala4.save(), sala5.save(), sala6.save(), sala7.save()

filme1 = Filme(nome="Vingadores Gerra Infinita",
               site="www.google.com.br",
               estreia="31/05/2018",
               cartaz="static/images/item-1.jpg",
               sinopse="Homem de Ferro, Thor, Hulk e os Vingadores se unem para combater seu inimigo mais poderoso, o maligno Thanos. Em uma missao para coletar todas as seis pedras infinitas, Thanos planeja usa-las para infligir sua vontade malefica sobre a realidade.",
               genero=genero1)
filme2 = Filme(nome="Rampage",
               site="www.google.com.br",
               cartaz="static/images/item-2.jpg",
               sinopse="Davis Okoye e um primatologista, um homem recluso que compartilha um vinculo inabalavel com George, um gorila muito inteligente que esta sob seus cuidados desde o nascimento. Quando um experimento genetico desonesto e feito em um grupo de predadores que inclui o primata, os animais se transformam em monstros que destroem tudo em seu caminho. Agora, Okoye precisa conseguir um antidoto e impedir que seu amigo provoque uma catastrofe global.",
               genero=genero2)
filme3 = Filme(nome="Han Solo",
               site="www.google.com.br",
               estreia="31/05/2018",
               cartaz="static/images/item-3.jpg",
               sinopse="Davis Okoye e um primatologista, um homem recluso que compartilha um vinculo inabalavel com George, um gorila muito inteligente que esta sob seus cuidados desde o nascimento. Quando um experimento genetico desonesto e feito em um grupo de predadores que inclui o primata, os animais se transformam em monstros que destroem tudo em seu caminho. Agora, Okoye precisa conseguir um antidoto e impedir que seu amigo provoque uma catastrofe global.",
               genero=genero3)
filme4 = Filme(nome="John Wick 2",
               site="www.google.com.br",
               estreia="31/05/2018",
               cartaz="static/images/item-4.jpg",
               sinopse="John Wick e forcado a deixar a aposentadoria mais uma vez por causa de uma promessa antiga e viaja para Roma, com o objetivo de ajudar um velho amigo a derrubar uma organizacao secreta, perigosa e mortal de assassinos procurados em todo o mundo.",
               genero=genero1)
filme5 = Filme(nome="Incriveis 2",
               site="www.google.com.br",
               estreia="31/05/2018",
               cartaz="static/images/item-5.jpg",
               sinopse="A Mulher Elastica entra em acao para salvar o dia, enquanto o Sr. Incrivel enfrenta seu maior desafio ate agora: cuidar dos problemas de seus tres filhos.",
               genero=genero2)
filme6 = Filme(nome="Um novo Caminho",
               site="www.google.com.br",
               estreia="31/05/2018",
               cartaz="static/images/item-6.jpg",
               sinopse="Don tem 19 anos e sai do Texas para fugir do passado cristao fervoroso imposto por sua mae. Ele entra em uma faculdade onde todos sao contra religioes e, ao fazer de tudo para se encaixar no lugar, comeca a questionar suas proprias crencas.",
               genero=genero3)
filme7 = Filme(nome="O Contador",
               site="www.google.com.br",
               estreia="static/images/31/05/20188",
               cartaz="item-7.jpg",
               sinopse="Christian Wolff, um contador com uma sindrome que limita suas habilidades sociais, cuida da contabilidade das organizacoes criminosas mais perigosas do mundo. Ao assumir um outro cliente, uma a empresa de robotica state-of-the-art, quanto mais perto ele chega da verdade, maior e o numero de corpos.",
               genero=genero4)

filme1.save(), filme2.save(), filme3.save(), filme4.save(), filme5.save(), filme6.save(), filme7.save()

prog1 = Programacao(periodoInicio="21/05/2018", periodoFinal="21/06/2018", filme=filme1, cinema=cine1)
prog2 = Programacao(periodoInicio="21/05/2018", periodoFinal="21/06/2018", filme=filme1, cinema=cine2)
prog3 = Programacao(periodoInicio="21/05/2018", periodoFinal="21/06/2018", filme=filme2, cinema=cine1)
prog4 = Programacao(periodoInicio="21/05/2018", periodoFinal="21/06/2018", filme=filme2, cinema=cine2)
prog5 = Programacao(periodoInicio="21/06/2018", periodoFinal="30/06/2018", filme=filme3, cinema=cine1)
prog1.save(), prog2.save(), prog3.save(), prog4.save(), prog5.save(),

tipoTela1 = TipoTela(tipoTela="3D")
tipoTela2 = TipoTela(tipoTela="I-Max")
tipoTela3 = TipoTela(tipoTela="2D")
tipoTela1.save(), tipoTela2.save(), tipoTela3.save()

DiaSemana(nome="Segunda", numero="1", preco=14, cinema=cine1).save()
DiaSemana(nome="Terca", numero="2", preco=14, cinema=cine1).save()
DiaSemana(nome="Quarta", numero="3", preco=16, cinema=cine1).save()
DiaSemana(nome="Quinta", numero="4", preco=20, cinema=cine1).save()
DiaSemana(nome="Sexta", numero="5", preco=20, cinema=cine1).save()
DiaSemana(nome="Sabado", numero="6", preco=20, cinema=cine1).save()
DiaSemana(nome="Domingo", numero="0", preco=20, cinema=cine1).save()
DiaSemana(nome="Feriado", numero="7", preco=20, cinema=cine1).save()
DiaSemana(nome="Segunda", numero="1", preco=12, cinema=cine2).save()
DiaSemana(nome="Terca", numero="2", preco=12, cinema=cine2).save()
DiaSemana(nome="Quarta", numero="3", preco=14, cinema=cine2).save()
DiaSemana(nome="Quinta", numero="4", preco=18, cinema=cine2).save()
DiaSemana(nome="Sexta", numero="5", preco=18, cinema=cine2).save()
DiaSemana(nome="Sabado", numero="6", preco=18, cinema=cine2).save()
DiaSemana(nome="Domingo", numero="0", preco=18, cinema=cine2).save()
DiaSemana(nome="Feriado", numero="7", preco=18, cinema=cine2).save()


for i in range(10):
    s1 = Sessao(filme=filme1, dataHora=str(i+3)+"/06/2018 8:00", tipoAudio=tipoAudio1, tipoTela=tipoTela1, sala=sala1)
    s2 = Sessao(filme=filme1, dataHora=str(i+3)+"/06/2018 10:00", tipoAudio=tipoAudio2, tipoTela=tipoTela1, sala=sala1)
    s3 = Sessao(filme=filme2, dataHora=str(i+3)+"/06/2018 16:00", tipoAudio=tipoAudio1, tipoTela=tipoTela3, sala=sala2)
    s4 = Sessao(filme=filme2, dataHora=str(i+3)+"/06/2018 20:00", tipoAudio=tipoAudio2, tipoTela=tipoTela3, sala=sala2)
    s5 = Sessao(filme=filme1, dataHora=str(i+3)+"/06/2018 8:00", tipoAudio=tipoAudio1, tipoTela=tipoTela1, sala=sala5)
    s6 = Sessao(filme=filme1, dataHora=str(i+3)+"/06/2018 10:00", tipoAudio=tipoAudio2, tipoTela=tipoTela1, sala=sala5)
    s7 = Sessao(filme=filme2, dataHora=str(i+3)+"/06/2018 16:00", tipoAudio=tipoAudio1, tipoTela=tipoTela3, sala=sala6)
    s8 = Sessao(filme=filme2, dataHora=str(i+3)+"/06/2018 20:00", tipoAudio=tipoAudio2, tipoTela=tipoTela3, sala=sala6)
    s1.save(), s2.save(), s3.save(), s4.save(), s5.save(), s6.save(), s7.save(), s8.save(),
    db.commit()

TipoReclamacao(tipo="Solicitacao de novos produtos").save()
TipoReclamacao(tipo="Reclamacao").save()
TipoReclamacao(tipo="Problema com entrega").save()
TipoReclamacao(tipo="Problema com pagamento").save()
TipoReclamacao(tipo="Outro assunto").save()

b1 = Banner(nome="Gerra Infinita",descricao="Estreia 26/04",banner="static/images/slider-1.jpg", status="ativo")
b2 = Banner(nome="STAR WARS VIII - THE LAST JEDI", descricao="Reveja outra vez", banner="static/images/slider-2.jpg", status="ativo")
b1.save(), b2.save()



