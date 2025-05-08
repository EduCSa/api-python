from src.repositories.usuarios_repository import (
    criar_usuario       as repo_criar,
    obter_usuario_por_id as repo_obter,
    listar_usuarios      as repo_listar,
    atualizar_usuario    as repo_atualizar,
    deletar_usuario      as repo_deletar,
)

class UsuarioService:
    def criar_usuario(self, **dados):
        return repo_criar(**dados)

    def buscar_usuario_por_id(self, usuario_id):
        return repo_obter(usuario_id)

    def listar_usuarios(self):
        return repo_listar()

    def atualizar_usuario(self, usuario_id, **dados):
        print("dados service",dados)
        return repo_atualizar(usuario_id, **dados)

    def deletar_usuario(self, usuario_id):
        return repo_deletar(usuario_id)
