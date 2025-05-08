from src.repositories.compras_repository import (
    criar_compra    as repo_criar,
)

from src.repositories.usuarios_repository import (
  obter_usuario_por_id
)

class ComprasService:
    def criar_compra(self, **dados):
      #  o usuario precisa existir antes de chamar o criar comprar 
      if 'usuario_id' not in dados:
          raise ValueError("usuario_id é obrigatório")

      usuario = obter_usuario_por_id(dados['usuario_id'])

      if not usuario:
          raise ValueError(f"Usuário com ID {dados['usuario_id']} não encontrado")

      return repo_criar(**dados)