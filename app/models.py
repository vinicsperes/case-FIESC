from sqlalchemy import Column, Integer, String
from app.database import Base

class Endereco(Base):
    __tablename__ = "enderecos"

    id = Column(Integer, primary_key=True, index=True)
    cep = Column(String(10), nullable=False)
    logradouro = Column(String(255), nullable=False)
    complemento = Column(String(255), nullable=False)
    bairro = Column(String(255), nullable=False)
    cidade = Column(String(255), nullable=False)
    estado = Column(String(255), nullable=False)
    estadoSigla = Column(String(2), nullable=False)
    pais = Column(String(255), nullable=False)
    paisSigla = Column(String(2), nullable=False)
