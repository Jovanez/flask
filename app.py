# -*- coding: UTF-8 -*-

from flask import Flask, render_template, request, redirect, session
from filme import filme
from peewee import DoesNotExist
import datetime
from banco import Banner,Filme,Usuario, Programacao, TipoReclamacao, Reclamacoes
from carrinho import carrinho

app = Flask(__name__, static_url_path='/static')
app.secret_key = '#*&@)#*#@$*CAMC9asd21ac6as8e4!#!@3'

app.register_blueprint(filme, url_prefix='/filme')
app.register_blueprint(carrinho, url_prefix='/carrinho')

@app.route("/")
def index():
   listaBanner = None
   listaFilme = listarFilme()
   try:
      listaBanner = Banner.select().where(Banner.status=="ativo")
   except DoesNotExist:
      pass

   return render_template("index.html", listaBanner=listaBanner, filmeCartaz=listaFilme)

@app.route("/contato", methods=['POST','GET'])
def contato():
    msg = []
    session['url'] = '/contato'
    if request.method == 'POST':
        try:
            email = request.form['email']
            telefone = request.form['telefone']
            nome = request.form['nome']
            mensagem = request.form['mensagem']
            tipoReclamacao = request.form['tipoReclamacao']
            Reclamacoes(nome=nome, telefone=telefone, texto=mensagem, email=email, tipo=tipoReclamacao, status='ativo').save()
            msg = ['alert-success', 'Sua msg foi enviada']
        except :
            msg = ['alert-danger', 'Sua msg nao foi enviada']

        return render_template("contact.html", tipoReclamacao=tipoReclamacao, msg=msg)
    else:
        tipoReclamacao = TipoReclamacao.select()
        return render_template("contact.html", tipoReclamacao=tipoReclamacao)


@app.route("/sobre")
def sobre():
   session['url'] = '/sobre'
   return render_template("about.html")



def listarFilme():
    listafilmes = None
    try:
        listafilmes = (Filme.select(Filme).where((Programacao.periodoInicio < datetime.datetime.now()) & (Programacao.periodoFinal > datetime.datetime.now())).join(Programacao).group_by(Filme.codigo))

    except DoesNotExist:
        pass

    return listafilmes
