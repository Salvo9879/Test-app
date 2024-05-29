from main.database import database
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

class Test(database.Model):
    __bind_key__ = 'Test'

    identifier = Column('identifier', Integer(), primary_key=True)
    name = Column('name', String(16))