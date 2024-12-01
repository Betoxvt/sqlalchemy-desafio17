from desafio import Fornecedor, Produto, engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

resultado = session.query(
    Fornecedor.nome,
    func.sum(Produto.preco).label('total_preco')
).join(Produto, Fornecedor.id == Produto.fornecedor_id).group_by(Fornecedor.nome).all()

for nome, total_preco in resultado:
    print(f"Fornecedor: {nome}, Preço Total: {total_preco}")