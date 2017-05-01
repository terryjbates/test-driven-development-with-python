# coding: utf-8
get_ipython().magic('cd /tmp')
from sqlalchemy import create_engine
engine = create_engine('sqlite:///cookies.db')
connection = engine.connect()
get_ipython().magic('paste')
get_ipython().magic('paste')
get_ipython().magic('paste')
get_ipython().magic('pinfo Table')
get_ipython().magic('paste')
import sqlalchemy
get_ipython().magic('paste')
sqlalchemy.__version__
engine = create_engine('sqlite:///cookies.db', echo=True)
connection = engine.connect()
engine = create_engine('sqlite:///:memory:', echo=True)
connection = engine.connect()
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String
get_ipython().magic('paste')
User.__table__
Base.metadata.create_all(engine)
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
ed_user.name
ed_user.password
str(ed_user.id)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session
Session = sessionmaker(bind=engine)
get_ipython().magic('pinfo Session')
engin
engine
Session.configure(bind=engine) 
session = Session()
session.add(ed_user)
our_user = session.query(User).filter_by(name='ed').first() 
session.dirty
ed_user.password = 'f8s7ccs'
session.dirty
session.new
session.commit()
ed_user.name = 'Edwardo'
fake_user = User(name='fakeuser', fullname='Invalid', password='12345')
session.add(fake_user)
session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()
session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()
session.rollback()
ed_user.name
ed_user.name
fake_user in session
session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all()
get_ipython().magic('paste')
session.query(User).filter(User.name.in_(['ed', 'wendy', 'mary', 'fred'])).all()
ed_user.password = 'f8s7ccs'
session.dirty
session.new
session.commit()
ed_user.id
mary_user = session.query(User).filter_by(name='mary').first()
mary_user.id
ed_user.name = 'Edwardo'
session.query(User).filter(User.name.in_(['Edwardo'])).all()
session.rollback()
ed_user.name
session.query(User).filter(User.name.in_(['ed'])).all()
for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)
    
for row in session.query(User, User.name).all():
    print(row.User, row.name)
    
for row in session.query(User.name.label('name_label')).all():
    print(row.name_label)
    
from sqlalchemy.orm import aliased
user_alias = aliased(User, name='user_alias')
for row in session.query(user_alias, user_alias.name).all():
    print(row.user_alias)
    
for u in session.query(User).order_by(User.id)[1:3]:
    print(u)
    
for name, in session.query(User.name).filter(User.fullname=='Ed Jones'):
     print(name)
    
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
class Address(Base):
        __tablename__ = 'addresses'
        id = Column(Integer, primary_key=True)
        email_address = Column(String, nullable=False)
        user_id = Column(Integer, ForeignKey('users.id'))
        user = relationship("User", back_populates="addresses")
        def __repr__(self):
                return "<Address(email_address='%s')>" % self.email_address
    
Base.metadata.create_all(engine)
jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
User.addresses = relationship(
"Address", order_by=Address.id, back_populates="user")
jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
Base.metadata.create_all(engine)
jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
class Address(Base):
        __tablename__ = 'addresses'
        id = Column(Integer, primary_key=True)
        email_address = Column(String, nullable=False)
        user_id = Column(Integer, ForeignKey('users.id'))
        user = relationship("User", back_populates="addresses")
        def __repr__(self):
                return "<Address(email_address='%s')>" % self.email_address
    
User.addresses = relationship("Address", order_by=Address.id, back_populates="user")
Base.metadata.create_all(engine)
ack = User(name='jack', fullname='Jack Bean', password='gjffdd')
jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
class Address(Base):
        __tablename__ = 'addresses'
        id = Column(Integer, primary_key=True)
        email_address = Column(String, nullable=False)
        user_id = Column(Integer, ForeignKey('users.id'))
        
user = relationship("User", back_populates="user")
def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address
User.addresses = relationship("Address", order_by=Address.id, back_populates="addresses")
class Address(Base):
        __tablename__ = 'addresses'
        id = Column(Integer, primary_key=True)
        email_address = Column(String, nullable=False)
        user_id = Column(Integer, ForeignKey('users.id'))
        
user = relationship("User", back_populates="addresses")
def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address
class Address(Base):
        __tablename__ = 'addresses'
        id = Column(Integer, primary_key=True)
        email_address = Column(String, nullable=False)
        user_id = Column(Integer, ForeignKey('users.id'))
        
user = relationship("User", back_populates="addresses")
def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address
get_ipython().magic('paste')
class Address(Base):
        __tablename__ = 'addresses'
        id = Column(Integer, primary_key=True)
        email_address = Column(String, nullable=False)
        user_id = Column(Integer, ForeignKey('users.id'))
        
user = relationship("User", back_populates="addresses")
__table_args__ = {'extend_existing': True}
def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address
get_ipython().magic('paste')
User.__table_args__ = {'extend_existing': True}
User.addresses = relationship("Address", order_by=Address.id, back_populates="addresses")
Base.metadata.create_all(engine)
jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
john = User(name='jack', fullname='Jack Bean', password='gjffdd')


################
import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)


User.__table_args__ = {'extend_existing': True}

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)  
session = Session()
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
session.add(ed_user)

ed_user
ed_user in session

session.commit()

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")
    
    def __repr__(self):
       return "<Address(email_address='%s')>" % self.email_address


User.addresses = relationship("Address", order_by=Address.id, back_populates="user")

jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
jack.addresses


Base.metadata.create_all(engine)


jack.addresses = [
                 Address(email_address='jack@google.com'),
                 Address(email_address='j25@yahoo.com')]
session.add(jack)
session.commit()


jack = session.query(User).filter_by(name='jack').one()

for u, a in session.query(User, Address).\
                filter(User.id==Address.user_id).\
                filter(Address.email_address=='jack@google.com').\
                all():
print(u)
print(a)

