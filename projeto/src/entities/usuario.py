from src.db        import db
from datetime      import datetime
from sqlalchemy    import text

class Usuario(db.Model):
    __tablename__  = 'usuarios'
    id         = db.Column(db.Integer, primary_key=True)
    nome       = db.Column(db.String(50), nullable=False)
    email      = db.Column(db.String(50), unique=True, nullable=False)
    telefone   = db.Column(db.String(15), nullable=False)
    idade      = db.Column(db.Integer, nullable=False)
    cep        = db.Column(db.String(10), nullable=False)
    pais       = db.Column(db.String(50), nullable=False)
    genero     = db.Column(db.String(10), nullable=False)
    ativo      = db.Column(db.Boolean, default=True)

    # grava timestamp já convertido para a zona America/Sao_Paulo (GMT-3)
    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=text("TIMEZONE('America/Sao_Paulo', NOW())")
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        server_default=text("TIMEZONE('America/Sao_Paulo', NOW())"),
        onupdate=text("TIMEZONE('America/Sao_Paulo', NOW())")
    )

    def to_dict(self):
        return {
            "id":         self.id,
            "nome":       self.nome,
            "email":      self.email,
            "telefone":   self.telefone,
            "idade":      self.idade,
            "cep":        self.cep,
            "pais":       self.pais,
            "genero":     self.genero,
            "ativo":      self.ativo,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    def repr(self):
        return f"<Usuario {self.nome}>"