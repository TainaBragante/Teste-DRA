from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from model.base import Base
from model.funcionario import Funcionario

# url de acesso ao banco 
db_url = os.getenv("DATABASE_URL","postgresql://flask_db_zyx9_user:G11MaHaLJjCSZYaMTtxqUsSj2jcW0yIY@dpg-cuh6am56147c73be5qn0-a.oregon-postgres.render.com:5432/flask_db_zyx9")

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)
