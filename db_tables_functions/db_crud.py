from sqlalchemy import select
from db_functions import db_connection
from db_functions import db_tables

def get_users():
    session = db_connection.SessionLocal()
    try:
        return session.query(db_tables.users).all()
    finally:
        session.close()

def get_user(username):
    session = db_connection.SessionLocal()
    try:
        return session.scalar(select(db_tables.users).where(db_tables.users.username == username))
    finally:
        session.close()

def register_user(username, profile_img=None):
    with db_connection.SessionLocal() as session:
        existing_user = session.scalar(
            select(db_tables.users).where(db_tables.users.username == username)
        )
        if existing_user:
            raise ValueError("Username already exists")
        user = db_tables.users(
            username=username,
            profile_img=profile_img
        )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def increment_cheese_amount(username, cheese_name):
    session = db_connection.SessionLocal()
    cheese = session.query(db_tables.cheese).filter_by(user_id=username, name=cheese_name).first()
    
    if cheese:
        cheese.amount += 1
    else:
        cheese = db_tables.cheese(
            user_id= username,
            name= cheese_name,
            amount= 1
        )
        session.add(cheese)
    
    session.commit()

def update_cheese_amount(username, cheese_name, cheese_amount):
    session = db_connection.SessionLocal()
    cheese = session.query(db_tables.cheese).filter_by(user_id=username, name=cheese_name).first()
    
    if cheese:
        cheese.amount = cheese_amount
    else:
        cheese = db_tables.cheese(
            user_id= username,
            name= cheese_name,
            amount= cheese_amount
        )
        session.add(cheese)
    
    session.commit()
    
def add_cheese_amount(username, cheese_name, cheese_amount):
    session = db_connection.SessionLocal()
    cheese = session.query(db_tables.cheese).filter_by(user_id=username, name=cheese_name).first()
    
    if cheese:
        cheese.amount += cheese_amount
    else:
        cheese = db_tables.cheese(
            user_id= username,
            name= cheese_name,
            amount= cheese_amount
        )
        session.add(cheese)
    
    session.commit()
    
def get_cheese_amount(username, cheese_name):
    session = db_connection.SessionLocal()
    try:
        return session.scalar(select(db_tables.cheese).where(db_tables.cheese.user_id == username, db_tables.cheese.name==cheese_name))
    finally:
        session.close()
