# creating.py
"""
Looking at creating separate databases for the raw data.
"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, DateTime, NUMERIC
from sqlalchemy.ext.declarative import declarative_base

# create tables
def make_db(the_file):
    engine = create_engine(the_file, echo=True)
    Base = declarative_base()

    class RawData(Base):
        __tablename__ = 'rawdata'
        id = Column(Integer, primary_key=True)
        date_time = Column(DateTime)
        inst_id = Column(Integer)
        temperature = Column(NUMERIC)
        humidity = Column(NUMERIC)

    Base.metadata.create_all(engine)


make_db('sqlite:///data2.db')

