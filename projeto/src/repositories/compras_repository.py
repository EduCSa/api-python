from src.db                 import db
from src.entities.compras   import Compras
from datetime               import datetime

def criar_compra(usuario_id, valor,status_pagamento,forma_pagamento,descricao):
    compra = Compras(
        usuario_id = usuario_id,
        valor = valor,
        status_pagamento = status_pagamento,
        forma_pagamento = forma_pagamento,
        descricao = descricao,
        data_compra=datetime.now()
    )
    db.session.add(compra)
    db.session.commit()
    return compra
