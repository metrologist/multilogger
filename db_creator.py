# db_creator.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///eleclog.db', echo=True)
Base = declarative_base()


class Type(Base):
    __tablename__ = 'type'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    protocol = Column(String)


class Instrument(Base):
    __tablename__ = 'instrument'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    serial = Column(String)
    type_id = Column(Integer, ForeignKey("type.id"))
    type = relationship("Type", backref=backref(
        "instrument", order_by=id))
    macaddress = Column(String)
    ipaddress = Column(String)
    params = Column(String)
    status = Column(String)


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    shortname = Column(String)
    instrument_id = Column(Integer, ForeignKey("instrument.id"))
    instrument = relationship("Instrument", backref=backref(
        "location", order_by=id))
    status = Column(String)


# create tables
Base.metadata.create_all(engine)
