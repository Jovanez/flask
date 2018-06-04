from flask import Flask, session,request,render_template,redirect, url_for, Blueprint
from banco import *

from peewee import DoesNotExist
carrinho = Blueprint('carrinho', __name__, static_folder='static')



@carrinho.route("/", methods=['POST','GET'])
def index():
    preco = 12
    if request.method == 'POST':
        if 'sessao' in request.form:
            if 'sessao' in session:
                s = session['sessao']
                sessao = Sessao.select(Filme, Sessao).where(Sessao.codigo == s).join(Filme).get()
                session.pop('sessao')
            else:
                s = request.form['sessao']
                try:
                    sessao = Sessao.select().where(Sessao.codigo == s).join(Filme).get()
                    print(sessao.filme.nome)
                    session['sessao'] = sessao.codigo
                    print("foi")
                except DoesNotExist:
                    redirect(session['url'])

            session['url'] = '/carrinho'

            return render_template('cart.html', sessao=sessao, preco=preco)
        else:
            redirect(session['url'])
    else:
        redirect("/")


