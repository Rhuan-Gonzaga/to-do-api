from database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100), nullable=False, unique=True)  
    senha = db.Column(db.String(120), nullable=False)
    
    # Método para definir o hash da senha
    def set_password(self, password):
        self.senha = generate_password_hash(password)  

    # Método para verificar a senha
    def check_password(self, password):
        return check_password_hash(self.senha, password)
