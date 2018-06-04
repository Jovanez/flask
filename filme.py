from flask import render_template,redirect,url_for, Blueprint, request, json, session
from banco import Filme, Programacao, Cinema, DiaSemana, Sessao, Sala, TipoAudio, TipoTela
from peewee import DoesNotExist
import datetime
filme = Blueprint("filme", __name__,static_folder='static', url_prefix="/filme")



@filme.route("/sessoes/<int:codigoCinema>/<int:codigoDia>/<int:codigoFilme>")
def sessoesJson(codigoCinema, codigoFilme, codigoDia):
    listaGeral = Sessao.select(Sessao).where((Sessao.dataHora > datetime.datetime.now()) & (
            Sala.cinema == codigoCinema) & (Sessao.filme == codigoFilme)).join(Sala).group_by(Sessao.codigo)
    listaVazio = []
    for s in listaGeral:
        if s.dataHora.strftime("%w") == str(codigoDia):
            print ("fiu")
            listaVazio.append(s)

    return render_template("painelSessoesFilme.html", sessoes=listaVazio)

@filme.route("/diasJson/<int:codigoCinema>")
def diasJson(codigoCinema):
    listaDiasSemana = DiaSemana.select().where((DiaSemana.cinema == codigoCinema)).order_by(DiaSemana.numero)
    return render_template('painelDiasFilme.html', dias=listaDiasSemana)


@filme.route("/", methods=['POST', 'GET'])
def index():
    session['url'] = 'filme/'
    listaCinemas = Cinema.select()
    filmes = (Filme.select(Filme).where((Programacao.periodoInicio < datetime.datetime.now()) & (
            Programacao.periodoFinal > datetime.datetime.now())).join(Programacao).group_by(Filme.codigo))


    if request.method == 'GET':
        return render_template("product.html", listaCinemas=listaCinemas, listaFilmes=filmes)

    else:

        codigoCinema = request.form['cinema']
        if 'codigoFilme' in request.form:
            codigo = request.form['codigoFilme']
            if codigo:
                try:
                    filmes = (Filme.select(Filme).where((Programacao.periodoInicio < datetime.datetime.now()) & (
                                Programacao.periodoFinal > datetime.datetime.now()) & (Programacao.cinema == codigoCinema) & (Filme.codigo == codigo)).join(Programacao).group_by(Filme.codigo))
                except DoesNotExist:
                    pass

        if 'nomeFilme' in request.form:
            nome = request.form['nomeFilme']
            if nome:
                try:
                    filmes = (Filme.select(Filme).where((Programacao.periodoInicio < datetime.datetime.now()) & (
                            Programacao.periodoFinal > datetime.datetime.now()) & (Programacao.cinema == codigoCinema) & (Filme.nome.contains(nome))).join(Programacao).group_by(Filme.codigo))
                except DoesNotExist:
                    pass

        return render_template("product.html", listaCinemas=listaCinemas, listaFilmes=filmes)


@filme.route("/detalhes", methods=['POST', 'GET'])
def detalhes():
    if request.method == 'POST':
        session['url'] = '/detalhes'
        codigo = request.form['codigo']
        filme = None
        cinemas = None

        try:
            filme = Filme.select(Filme).where(
                (Filme.codigo == codigo) & (
                        Programacao.filme == Filme.codigo) & (
                        Programacao.periodoInicio < datetime.datetime.now()) & (
                        Programacao.periodoFinal > datetime.datetime.now()) & (
                        Programacao.cinema == Cinema.codigo)
            ).join(Programacao).join(Cinema).get()
            recomendados = Filme.select().where((Filme.codigo != codigo) & (Filme.genero == filme.genero))
        except DoesNotExist:
            return redirect("/")

        try:
            cinemas = Cinema.select(Cinema).where((Programacao.filme == codigo)& (Programacao.cinema == Cinema.codigo)).join(Programacao).join(Filme).group_by(Cinema.codigo)
        except DoesNotExist:
            return redirect("/")

        return render_template("product-detail.html", filme=filme, listaCinema=cinemas, recomendados=recomendados)


@filme.route("/teste")
def teste():
    filmes = (Filme.select(Filme).where((Programacao.periodoInicio < datetime.datetime.now()) & (Programacao.periodoFinal > datetime.datetime.now())).join(Programacao).group_by(Filme.codigo))
    string = ""
    for ob in filmes:
        string+="Filme: %s \n "%(ob.nome)

    return string

def teste2():
    filmes = (Programacao.select(Programacao,Filme).where((Programacao.periodoInicio < datetime.datetime.now()) & (Programacao.periodoFinal > datetime.datetime.now())).join(Filme))
    string = ""
    for ob in filmes:
        string+="Filme: %s Data:%s "%(ob.filme.nome,ob.periodoInicio.strftime(' %d, %b %Y'))

    return string