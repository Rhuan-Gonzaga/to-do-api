from flask import Blueprint,request,jsonify
from tarefas.models import Tarefas
from database import db

tarefas_blueprint = Blueprint('tarefa',__name__,template_folder='templates')

#Criando uma nova tarefa
#Exemplo de requisição: http://127.0.0.1:5000/criartarefa
"""
{
"id_usuario": 1,
"titulo":"tarefa de teste",
"status": false
}
"""
@tarefas_blueprint.route('/criartarefa', methods=['POST'])
def criar_tarefa():
  data = request.json
  print(data)
  nova_tarefa = Tarefas(id_usuario=data["id_usuario"],titulo=data['titulo'],status=data['status'])
  db.session.add(nova_tarefa)
  db.session.commit()
  return jsonify({"mensagem":"Tarefa cadastrada"}), 201

#Editando o status de uma tarefa
#Exemplo de requisição: http://127.0.0.1:5000/status/1 
@tarefas_blueprint.route('/status/<int:id>',methods=['POST'])
def mudar_status(id):
  data = request.json

  #verifiando se a tarefa existe
  tarefa = Tarefas.query.get(id)
  if not tarefa:
    return jsonify({"erro": "Tarefa não encontrada"}), 404
  
  #Pegando o novo statur da tarefa e atualizando no banco
  tarefa.status = data.get('status', tarefa.status)
  db.session.commit()

  return jsonify({"Mensagem": "Tarefa atualizada com sucesso"}), 201

#Deletando uma tarefa pelo ID
#Exemplo de requisição: http://127.0.0.1:5000/deletartarefa/1 
@tarefas_blueprint.route('/deletartarefa/<int:id>',methods=['DELETE'])
def deletar_tarefa(id):

  #verifiando se a tarefa existe
  tarefa = Tarefas.query.get(id)
  if not tarefa:
    return jsonify({"erro": "Tarefa não encontrada"}), 404

  Tarefas.query.filter_by(id=Tarefas.tarefa).delete()
  db.session.commit() 
  
  return jsonify({"Mensagem": "Tarefa deletada com sucesso"}), 201


#Pegando toda a lista de tarefas e filtrando as tarefas com base no status como parâmetro
#Exemplo de requisição: http://127.0.0.1:5000/tarefas?status=0 ou http://127.0.0.1:5000/tarefas?status=1
@tarefas_blueprint.route('/tarefas', methods=['GET'])
def todas_tarefa():
    status = request.args.get('status')  
    
    if status:
        tarefas = Tarefas.query.filter_by(status=status).all()  
    else:
        tarefas = Tarefas.query.all()  

    tarefas_dict = [
        {
            "id_usuario": tarefa.id_usuario,
            "id": tarefa.id,
            "titulo": tarefa.titulo,
            "status": tarefa.status
        }
        for tarefa in tarefas
    ]
    return jsonify(tarefas_dict)

