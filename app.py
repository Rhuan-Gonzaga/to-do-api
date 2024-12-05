from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from tarefas.tarefas import tarefas_blueprint
from database import db


app = Flask(__name__)
app.config['SECRET_KEY'] = '0101'
conexao = 'mysql+pymysql://root:@localhost/to-do-list'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao

app.register_blueprint(tarefas_blueprint)

db.init_app(app)

