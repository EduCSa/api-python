from flask          import Blueprint, request, jsonify, abort
from src.services.usuario_service import UsuarioService

service = UsuarioService()
usuario_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@usuario_bp.route('', methods=['GET'])
def listar_usuarios():
    lista = service.listar_usuarios()
    return jsonify([u.to_dict() for u in lista])

@usuario_bp.route('', methods=['POST'])
def criar_usuario():
    data = request.json or {}
    usr  = service.criar_usuario(**data)
    return jsonify(usr.to_dict()), 201

@usuario_bp.route('/<int:id>', methods=['GET'])
def buscar_usuario(id):
    usr = service.buscar_usuario_por_id(id)
    if not usr:
        abort(404, "Usuário não encontrado")
    return jsonify(usr.to_dict())

@usuario_bp.route('/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    data = request.json or {}
    print("data",data)
    usr  = service.atualizar_usuario(id, **data)
    if not usr:
        abort(404, "Usuário não encontrado")
    return jsonify(usr.to_dict())

@usuario_bp.route('/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    ok = service.deletar_usuario(id)
    if not ok:
        abort(404, "Usuário não encontrado")
    return ('', 204)
