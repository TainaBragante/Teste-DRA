import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model.base import Base
from model.funcionario import Funcionario

# Obtendo a URL do banco de dados do ambiente
db_url = os.getenv("DATABASE_URL")

# 🔹 Verifica se a URL está definida
if not db_url:
    raise ValueError("⚠️ ERRO: A variável DATABASE_URL não está definida no ambiente!")

# 🔹 Converte a URL para o formato correto
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

# Criando a engine do banco de dados
engine = create_engine(db_url + "?sslmode=require", echo=True)

# Criando a sessão com o banco de dados
Session = sessionmaker(bind=engine)

# Criando as tabelas no banco, caso não existam
Base.metadata.create_all(engine)