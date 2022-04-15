import sys
sys.path.append(".")
from src.prueba_2 import db
from sqlalchemy import Column,Integer,String


class User(db.Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    
    def __init__(self, name, last_name,age,email ):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email
        
    def __repr__(self):
        return f'<User {self.email}>'
      
    def __str__(self):
        return f"Name: {self.name}, Last name: {self.last_name} Email: {self.email}, Age: {self.age}"
      
      
      
