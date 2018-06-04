from peewee import Model, CharField, PostgresqlDatabase,PrimaryKeyField,ForeignKeyField,DateField,DateTimeField,DoubleField,IntegerField,TextField,CompositeKey
from flask import json

db = PostgresqlDatabase('cinema', user='postgres', password='postgres', host="localhost", port="5432")

class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = db



class Usuario(BaseModel):
    idUsuario = PrimaryKeyField()
    login = CharField(unique=True,max_length=18)
    perguntaSecreta = CharField()
    resposta = CharField()
    senha = CharField()


class Cliente(BaseModel):
    codigo = PrimaryKeyField()
    nome = CharField(max_length=42)
    cpf = CharField(max_length=14)
    email = CharField(unique=True,max_length=42)
    usuario = ForeignKeyField(Usuario, backref='Cliente')


class BandeiraCartao(BaseModel):
    codigo = PrimaryKeyField()
    bandeira = CharField(max_length=18)


class Cartao(BaseModel):
    numero = CharField(primary_key=True)
    bandeira = ForeignKeyField(BandeiraCartao)
    cliente = ForeignKeyField(Cliente, backref='Cartao')

class Funcionario(BaseModel):
    codigo = PrimaryKeyField()
    nome = CharField(max_length=42)
    cpf = CharField(max_length=14)
    usuario = ForeignKeyField(Usuario, backref='Cliente')

class Genero(BaseModel):
    codigo = PrimaryKeyField()
    genero = CharField(max_length=18)

class TipoAudio(BaseModel):
    codigo = PrimaryKeyField()
    tipoAudio = CharField(max_length=18)


class Uf(BaseModel):
    sigla = CharField(primary_key=True,max_length=2)
    nome = CharField(max_length=30)

class Cidade(BaseModel):
    codigo = PrimaryKeyField()
    nome = CharField(max_length=42)
    uf = ForeignKeyField(Uf, backref='Cidades')

class Endereco (BaseModel):
    codigo = PrimaryKeyField()
    cidade = ForeignKeyField(Cidade)
    rua = CharField(max_length=50)
    numero = CharField(max_length=10)
    referencia = CharField(max_length=50)

class Cinema(BaseModel):
    codigo = PrimaryKeyField()
    nome = CharField()
    endereco = ForeignKeyField(Endereco)

class Sala(BaseModel):
    codigo = PrimaryKeyField()
    numero = IntegerField()
    cinema = ForeignKeyField(Cinema)
    capacidade = IntegerField()

class Filme(BaseModel):
    codigo = PrimaryKeyField()
    nome = CharField(unique=True)
    site = CharField()
    cartaz = CharField(max_length=100, default="static/images/item-null.jpg")
    embreve = CharField(max_length=100, default="static/images/banner-null.jpg")
    sinopse = TextField()
    genero = ForeignKeyField(Genero, backref='Filmes')

class Programacao(BaseModel):
    codigo = PrimaryKeyField()
    periodoInicio = DateTimeField()
    periodoFinal = DateTimeField()
    filme = ForeignKeyField(Filme, backref='Programacoes')
    cinema = ForeignKeyField(Cinema, backref='Programacoes')

class DiaSemana(BaseModel):
    codigo = PrimaryKeyField()
    nome = CharField()
    numero = IntegerField()
    preco = DoubleField()
    cinema = ForeignKeyField(Cinema, backref='DiasDaSemana')

class TipoTela(BaseModel):
    codigo = PrimaryKeyField()
    tipoTela = CharField()

class Sessao(BaseModel):
    codigo = PrimaryKeyField()
    dataHora = DateTimeField()
    tipoAudio = ForeignKeyField(TipoAudio)
    tipoTela = ForeignKeyField(TipoTela)
    filme = ForeignKeyField(Filme, backref='Sessoes')
    sala = ForeignKeyField(Sala, backref='Sessoes')

class Compra(BaseModel):
    codigo = PrimaryKeyField()
    cliente = ForeignKeyField(Cliente, backref='Vendas')
    dataVenda = DateField()
    status = CharField(max_length=10)

class Boleto(BaseModel):
    numero = CharField(primary_key=True)
    status = CharField()
    compra = ForeignKeyField(Compra, backref='Boletos')

class Ingresso(BaseModel):
    codigo = PrimaryKeyField()
    dono = CharField()
    sessao = ForeignKeyField(Sessao)
    venda = ForeignKeyField(Compra, backref='Ingressos')

class Gostei(BaseModel):
    codigo = PrimaryKeyField()
    usuario = CharField()
    filme = ForeignKeyField(Filme)

class TipoReclamacao(BaseModel):
    codigo = PrimaryKeyField()
    tipo = CharField()

class Reclamacoes(BaseModel):
    codigo = PrimaryKeyField()
    nome = CharField()
    email = CharField()
    tipo = ForeignKeyField(TipoReclamacao)
    telefone = CharField()
    texto = CharField()
    status = CharField(max_length=10)

class Banner(BaseModel):
    codigo = PrimaryKeyField()
    nome = CharField()
    descricao = CharField()
    banner = CharField(max_length=100)
    status = CharField(max_length=10)