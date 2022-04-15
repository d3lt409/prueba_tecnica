from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///src/prueba_2/db_prueba.sqlite')

Sessionmaker = sessionmaker(bind=engine)
session:Session = Sessionmaker()

Base = declarative_base()