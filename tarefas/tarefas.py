from flask import Blueprint,request,jsonify
from tarefas.models import Tarefas
from database import db


tarefas_blueprint = Blueprint('tarefa',__name__,template_folder='templates')

@tarefas_blueprint.route('/tarefa', methods=['POST'])
def criar_tarefa():
  data = request.json
  print(data)
  nova_tarefa = Tarefas(id_usuario=data["id_usuario"],titulo=data['titulo'],status=data['status'])
  db.session.add(nova_tarefa)
  db.session.commit()
  return jsonify({"mensagem":"Tarefa cadastrada"}), 201