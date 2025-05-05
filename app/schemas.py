from pydantic import BaseModel, Field, field_validator

class EnderecoBase(BaseModel):
    cep: str = Field(..., description="CEP do endereço", pattern=r"^\d{5}-?\d{3}$")
    logradouro: str = Field(..., description="Logradouro do endereço")
    complemento: str = Field(..., description="Complemento do endereço")
    bairro: str = Field(..., description="Bairro do endereço")
    cidade: str = Field(..., description="Cidade do endereço")
    estado: str = Field(..., description="Estado do endereço")
    estadoSigla: str = Field(..., min_length=2, max_length=2, description="Sigla do estado")
    pais: str = Field(..., description="País do endereço")
    paisSigla: str = Field(..., min_length=2, max_length=2, description="Sigla do país")

    @field_validator('logradouro', 'complemento', 'bairro', 'cidade', 'estado', 'pais')
    def check_non_empty(cls, v):
        if not v or v.strip() == "":
            raise ValueError(f'O campo não pode ser vazio')
        return v

    @field_validator('estadoSigla', 'paisSigla')
    def check_sigla(cls, v):
        if len(v) != 2:
            raise ValueError(f'O campo deve ter exatamente 2 caracteres')
        return v

class EnderecoCreate(EnderecoBase):
    pass

class Endereco(EnderecoBase):
    id: int

    model_config = {
        "from_attributes": True
    }
