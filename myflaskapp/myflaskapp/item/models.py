"""User models."""
import datetime as dt

from flask_login import UserMixin

from myflaskapp.database import Column, Model, SurrogatePK, db, reference_col, relationship
from myflaskapp.extensions import bcrypt

class Item(SurrogatePK, Model):
    __tablename__ = 'items'
    __table_args__ = {'extend_existing': True}
    text = Column(db.String(80),nullable=True)
    user_id = reference_col('users', nullable=True)
    user = relationship('User', backref='items')
    #user = Column(db.String(64), db.ForeignKey('users.username'))
    
    def __init__(self, text=None, user=None):
        self.user = user
        self.text = text



