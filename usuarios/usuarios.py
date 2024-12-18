from flask import Blueprint,request,jsonify
from usuarios.models import Usuario
from database import db

usuarios_blueprint= Blueprint('usuario',__name__,template_folder='templates')

@usuarios_blueprint.route('/criarusuario', methods=['POST'])
def criar_usuario():
    data = request.json
    usarioo = data.get("usuario")
    senha = data.get("senha")

    if not usarioo or not senha:
        return jsonify({"erro": "Usuário e senha são obrigatórios"}), 400
    
    # Verificar se o usuário já existe
    if Usuario.query.filter_by(usuario=data['usuario']).first():
        return jsonify({"erro": "Usuário já existe"}), 409

    # Criar um novo usuário
    novo_usario = Usuario(usuario=usarioo)
    print(senha)
    novo_usario.set_password(senha)
    db.session.add(novo_usario)
    db.session.commit()

    return jsonify({"mensagem": "Usuario cadastrado"}), 201