from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Estamos "conectando" a umSQLbanco de dados lite
# O arquivo estará localizado no mesmo diretório do arquivo sql_app.db.
#
# É por isso que a última parte é ../sql_app.db
SQLALCHEMY_DATABSE_URL = "sqlite:///./aql_app.db"

# Se você estivesse usando um PostgreSQLbanco de dados, basta descomentar a linha:
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# ...e adapte-o com os dados e credenciais do seu banco de dados (equivalente para MySQL, MariaDB ou qualquer outro).

engine = create_engine(
    SQLALCHEMY_DATABSE_URL, connect_args={"check_same_thread":False}
#     connect_args={"check_same_thread": False} ---> ...é necessário apenas para SQLite. Não é necessário para outros bancos de dados.
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()