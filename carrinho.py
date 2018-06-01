from flask import Flask, session,request,render_template,redirect,url_for, Blueprint

carrinho = Blueprint('carrinho', __name__, static_folder='controllers')

@carrinho.route("/")
def index():
    return render_template("cart.html")
