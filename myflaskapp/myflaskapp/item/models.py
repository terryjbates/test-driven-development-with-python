"""User models."""
import datetime as dt

from flask_login import UserMixin

from myflaskapp.database import Column, Model, SurrogatePK, db, reference_col, relationship
from myflaskapp.extensions import bcrypt

class Item(SurrogatePK, Model):
    __tablename__ = 'items'
    text = Column(db.String(80),nullable=True)

