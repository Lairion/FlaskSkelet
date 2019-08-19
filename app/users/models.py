from flask_login import UserMixin
from app import db,Base

# Define a User model
class User(UserMixin, Base):
    __tablename__ = 'auth_user'
    # User Name
    name = db.Column(
        db.String(128),  
        nullable=False)
    # Identification Data: email & password
    email = db.Column(
        db.String(128),  
        nullable=False,
        unique=True)
    password = db.Column(
        db.String(192),  
        nullable=False)
    # Authorisation Data: role & status
    role = db.Column(
        db.SmallInteger, 
        nullable=False)
    status = db.Column(
        db.SmallInteger, 
        nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password,role=0,status=0):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.status = status

    def __repr__(self):
        return '<User %r>' % (self.name) 
    
    def __str__(self):
        return self.name   