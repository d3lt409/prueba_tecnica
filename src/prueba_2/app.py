import click
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError, NoResultFound

import sys,json
sys.path.append(".")
from src.prueba_2 import db
from models import User

@click.group()
def main():
    pass

@main.command()
def get_users():
  '''
    Retorna todos los usuarios en un json

    Returns\n
    -------
    list[dict] -> Todos los usuarios en un listado
    '''
  res = db.session.query(User)
  click.echo(json.dumps([{c.key:getattr(row,c.key) for c in inspect(row).mapper.column_attrs} 
                         for row in res],indent=3)) 

@main.command()
@click.option('--name', '-n',required=True,type=str)
@click.option('--last_name', '-l',required=True,type=str)
@click.option('--age', '-a',required=True,type=int)
@click.option('--email', '-e', required=True,type=str)
def create_user(name:str,last_name:str,age:int,email:str):
  '''
    Crea un usuario nuevo
    
    Parameters
    ----------\n
    name : string
        Es el nombre del usuario\n
    last_name : string
        Es el apellido del usuario\n
    age : int
        Es la edad del usuario\n
    email : string
        Es el correo del usuario\n

    Returns
    -------
    User:  Retorna el objeto del nuevo usario
    '''
  user = User(name,last_name,age,email)
  try:
    db.session.add(user)
    db.session.commit()
    click.echo(f"Usuario con {user} creado") 
  except IntegrityError as _:
    click.echo(f"No se puede crear el usuario con email {email}, ya existe este correo") 

@main.command()
@click.option('--id', '-i',required=True,type=int)
def delete_user(id:int):
  '''
    Elimina un usuario por id
    
    Parameters
    ----------\n
    id : int
        El id del usuario a elminar\n
        
    Returns
    -------\n
    User:  Retorna el __str__ del objeto User a elminar
    '''
  user = db.session.query(User).filter(User.id==id)
  email = user.all()
  if len(email) == 0: return click.echo(f"El usuario con id {id} no está en el sistema") 
  user.delete()
  db.session.commit()
  click.echo(f"{email[0]} fue eliminado") 

@main.command()
@click.option('--id', '-i',required=True,type=int)
@click.option('--name', '-n',type=str)
@click.option('--last_name', '-l',type=str)
@click.option('--age', '-a',type=int)
@click.option('--email', '-e', type=str)
def update_user(id,name,last_name,age,email):
  '''
    Actualiza el ususario por id
    
    Parameters
    ----------\n
    name : string
        Es el nuevo nombre del usuario\n
    last_name : string
        Es el nuevo apellido del usuario\n
    age : int
        Es la nueva edad del usuario\n
    email : string
        Es el nuevo correo del usuario\n

    Returns
    -------\n
    User:  Retorna el objeto del nuevo usario
    '''
  values = {}
  if name: values["name"] = name
  if last_name: values["last_name"] = last_name
  if age: values["age"] = age
  if email: values["email"] = email
  user = db.session.query(User).filter(User.id==id)
  try:
    user_obj = user.one()
  except NoResultFound as _:
    click.echo(f"No se encontró el usuario con id {id}")
    return
  try:
    user.update(values)
  except IntegrityError as _:
    return click.echo(f"El usuario no puede tener este email, ya le pertenece a otro usuario")
  db.session.commit()
  click.echo(user_obj) 

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    main()