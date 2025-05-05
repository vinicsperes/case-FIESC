from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter(
    prefix="/enderecos",
    tags=["Endereços"]
)

# Dependência para pegar a sessão do banco
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verificar_endereco_duplicado(db: Session, endereco_data: dict):
    endereco = db.query(models.Endereco).filter(
        models.Endereco.cep == endereco_data['cep'],
        models.Endereco.logradouro == endereco_data['logradouro'],
        models.Endereco.complemento == endereco_data['complemento'],
        models.Endereco.bairro == endereco_data['bairro'],
        models.Endereco.cidade == endereco_data['cidade'],
        models.Endereco.estado == endereco_data['estado'],
        models.Endereco.estadoSigla == endereco_data['estadoSigla'],
        models.Endereco.pais == endereco_data['pais'],
        models.Endereco.paisSigla == endereco_data['paisSigla']
    ).first()

    if endereco:
        raise HTTPException(status_code=400, detail="Endereço já cadastrado.")
    return None


@router.post("/", response_model=schemas.Endereco)
def criar_endereco(endereco: schemas.EnderecoCreate, db: Session = Depends(get_db)):
    verificar_endereco_duplicado(db, endereco.dict())

    db_endereco = models.Endereco(**endereco.dict())
    db.add(db_endereco)
    db.commit()
    db.refresh(db_endereco)
    return db_endereco

@router.get("/{id}", response_model=schemas.Endereco)
def buscar_endereco(id: int, db: Session = Depends(get_db)):
    endereco = db.query(models.Endereco).filter(models.Endereco.id == id).first()
    if not endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return endereco

@router.get("/", response_model=list[schemas.Endereco])
def listar_enderecos(db: Session = Depends(get_db)):
    return db.query(models.Endereco).all()

@router.put("/{id}", response_model=schemas.Endereco)
def atualizar_endereco(id: int, endereco: schemas.EnderecoCreate, db: Session = Depends(get_db)):
    db_endereco = db.query(models.Endereco).filter(models.Endereco.id == id).first()
    if not db_endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    for key, value in endereco.model_dump().items():
        setattr(db_endereco, key, value)
    db.commit()
    db.refresh(db_endereco)
    return db_endereco

@router.delete("/{id}")
def deletar_endereco(id: int, db: Session = Depends(get_db)):
    db_endereco = db.query(models.Endereco).filter(models.Endereco.id == id).first()
    if not db_endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    db.delete(db_endereco)
    db.commit()
    return {"mensagem": "Endereço deletado com sucesso"}
