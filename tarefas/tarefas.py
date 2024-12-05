from flask import Blueprint,render_template,request,jsonify
from tarefas.models import Tarefas
from database import db


tarefas_blueprint = Blueprint('tarefa',__name__,template_folder='templates')

@tarefas_blueprint.route('/tarefa', methods=['POST'])
def criar_tarefa():
  data = request.json
  nova_tarefa = Tarefas(titulo=data['titulo'],status=data['status'])
  db.sesstion.add(nova_tarefa)
  db.session.commit()
  return jsonify({"mensagem":"Tarefa cadastrada"}), 201