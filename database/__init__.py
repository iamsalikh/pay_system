from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_URL = 'sqlite:///data.db'
engine = create_engine(SQLALCHEMY_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

from database import models


# генератор подключений
def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()