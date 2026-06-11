from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL connection URL format:
# mysql+pymysql://<username>:<password>@<host>/<database_name>
DATABASE_URL = "mysql+pymysql://root:yourpassword@localhost/yourdatabase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
