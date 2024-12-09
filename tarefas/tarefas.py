from flask import Blueprint,request,jsonify
from tarefas.models import Tarefas
from database import db


tarefas_blueprint = Blueprint('tarefa',__name__,template_folder='templates')
#Criando uma nova tarefa
@tarefas_blueprint.route('/tarefa', methods=['POST'])
def criar_tarefa():
  data = request.json
  print(data)
  nova_tarefa = Tarefas(id_usuario=data["id_usuario"],titulo=data['titulo'],status=data['status'])
  db.session.add(nova_tarefa)
  db.session.commit()
  return jsonify({"mensagem":"Tarefa cadastrada"}), 201

#Editando o status de uma tarefa
@tarefas_blueprint.route('/status/<int:id>',methods=['POST'])
def mudar_status(id):
  data = request.json

  tarefa = Tarefas.query.id(id)

  if not tarefa:
    return jsonify({"erro": "Tarefa não encontrada"}), 404
  
  tarefa.status = data.get('status', tarefa.status)

  db.session.commit()

  return jsonify({"Mensagem": "Tarefa atualizada com sucesso"}), 201

