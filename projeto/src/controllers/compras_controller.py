# src/controllers/compras_controller.py
from flask import Blueprint, request, jsonify, abort
from src.services.compras_service import ComprasService

compra_service = ComprasService()
compra_bp = Blueprint('compras', __name__, url_prefix='/compras')

@compra_bp.route('', methods=['POST'])
def criar_compra():
    dados = request.get_json() or {}
    try:
        compra = compra_service.criar_compra(**dados)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    # Aqui usamos o to_dict() para converter o objeto em dict
    return jsonify(compra.to_dict()), 201
