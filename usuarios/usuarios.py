from flask import Blueprint,request,jsonify
from usuarios.models import Usuario
from database import db

usuarios_blueprint= Blueprint('usuario',__name__,template_folder='templates')

@usuarios_blueprint.route('/criarusuario', methods=['POST'])
def criar_usuario():
    data = request.json
    novo_usuario = Usuario(usuario=data['usuario'], senha=data['senha'])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({"mensagem": "Usuario cadastrado"}), 201