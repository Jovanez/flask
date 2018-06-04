# -*- coding: UTF-8 -*-
from functools import wraps
from flask import Flask, render_template, request, redirect, wrappers, url_for, session
from filme import filme
from peewee import DoesNotExist
import datetime
from banco import Cliente, Banner, Filme, Usuario, Programacao, TipoReclamacao, Reclamacoes
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


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['usuario'] is None:
            session['url'] = request.url
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        msg = ['', '']
        if 'usuario' and 'senha' in request.form:
            usuario = request.form['usuario']
            senha = request.form['senha']
            try:
                user = Usuario.select().where(usuario == Usuario.login).get()
                if senha == user.senha:
                    session['usuario'] = usuario
                    if 'url' in session :
                        url = session['url']
                        return redirect(url)
                    else:
                       return redirect("/")
                else:
                    msg[1] = "Senha Invalida"
                    msg[0] = "alert-danger"
                    return render_template("login.html",msg=msg)
            except DoesNotExist:
                msg[0] = "alert-danger"
                msg[1] = "Usuario nao Encontrado"
                return render_template("login.html", msg=msg)
        else:
            msg[0] = "alert-danger"
            msg[1] = "Algum campo vazio"
            return render_template("login.html", msg=msg)

@app.route("/usuario", methods=['POST','GET'])
def cadastro():
    msg=[]
    if request.method == 'GET':
        return render_template("cadastro.html")
    else:
        email = request.form['email']
        nome = request.form['email']
        senha = request.form['email']
        login = request.form['email']
        cpf = request.form['email']
        confirmaSenha = request.form['email']


        if email and nome and senha and login and cpf and confirmaSenha:
            if senha == confirmaSenha:
                user = Usuario.select().where((Usuario.login == login))
                if user is None:
                    clie = Cliente.select().where((Cliente.login == login) | (
                           Cliente.cpf == cpf) | (
                           Cliente.email == email)).get()
                    if clie is None:
                        u = Usuario(login=login,senha=senha)

            else:
                msg[0] = "alert-danger"
                msg[1] = "Senhas nao batem"



@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

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
