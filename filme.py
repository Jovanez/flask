from flask import render_template,redirect,url_for, Blueprint, request, json
from banco import Filme, Programacao, Cinema, DiaSemana
from peewee import DoesNotExist
import datetime
filme = Blueprint("filme", __name__,static_folder='static', url_prefix="/filme")


@filme.route("/diasJson/<int:codigoCinema>")
def diasJson(codigoCinema):
    listaDiasSemana = DiaSemana.select().where(DiaSemana.cinema == codigoCinema).order_by(DiaSemana.numero)
    return render_template('painelDiasFilme.html',dias=listaDiasSemana)


@filme.route("/", methods=['POST', 'GET'])
def index():

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
        except DoesNotExist:
            return redirect("/")

        try:
            cinemas = Cinema.select(Cinema).where((Programacao.filme == codigo)& (Programacao.cinema == Cinema.codigo)).join(Programacao).join(Filme).group_by(Cinema.codigo)
        except DoesNotExist:
            pass

        return render_template("product-detail.html",filme=filme,listaCinema=cinemas)


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