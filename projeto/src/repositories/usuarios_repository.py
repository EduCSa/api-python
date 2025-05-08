from src.db                 import db
from src.entities.usuario   import Usuario
from datetime               import datetime

def criar_usuario(nome, email, telefone, idade, cep, pais, genero, ativo=True):
    u = Usuario(
        nome=nome,
        email=email,
        telefone=telefone,
        idade=idade,
        cep=cep,
        pais=pais,
        genero=genero,
        ativo= ativo,
        created_at=datetime.now()
    )
    
    db.session.add(u)
    db.session.commit()
    return u

def obter_usuario_por_id(usuario_id):
    return Usuario.query.get(usuario_id)

def listar_usuarios():
    return Usuario.query.order_by(Usuario.nome).all()

def atualizar_usuario(usuario_id, **campos):
    u = obter_usuario_por_id(usuario_id)
    if not u:
        return None
    for k, v in campos.items():
        setattr(u, k, v)
    db.session.commit()
    return u

def deletar_usuario(usuario_id):
    u = obter_usuario_por_id(usuario_id)
    if not u:
        return False
    db.session.delete(u)
    db.session.commit()
    return True
