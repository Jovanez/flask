from flask import render_template,redirect,url_for, Blueprint, request
from banco import Filme, Programacao, Cinema
from peewee import DoesNotExist
import datetime
filme = Blueprint("filme", __name__,static_folder='static', url_prefix="/filme")



@filme.route("/")
def index():
    return render_template("product-detail.html")


@filme.route("/detalhes", methods=['POST', 'GET'])
def detalhes():
    if request.method == 'POST':
        codigo = request.form['codigo']
        filme = None
        cinemas = None
        try:
            filme = Filme.select().where(Filme.codigo == codigo).get()
        except DoesNotExist:
            pass

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