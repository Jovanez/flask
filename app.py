# -*- coding: UTF-8 -*-

from flask import Flask, render_template
from filme import filme
from peewee import DoesNotExist
import datetime
from banco import Banner,Filme,Usuario, Programacao
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
      listaBanner = Banner.select()
   except DoesNotExist:
      pass

   return render_template("home-02.html", listaBanner=listaBanner,i=1,filmeCartaz=listaFilme)

@app.route("/contato")
def contato():
   return render_template("contact.html")

@app.route("/sobre")
def sobre():
   return render_template("about.html")



def listarFilme():
    listafilmes = None
    try:
        listafilmes = (Filme.select(Filme).where((Programacao.periodoInicio < datetime.datetime.now()) & (Programacao.periodoFinal > datetime.datetime.now())).join(Programacao).group_by(Filme.codigo))

    except DoesNotExist:
        pass

    return listafilmes

