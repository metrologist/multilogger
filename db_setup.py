# db_setup.py

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# note the forced allowing of multiple threads appears necessary but not ideal
# I wasn't able to minimise threads by lots of db_session.close() but that is likely a better approach
engine = create_engine('sqlite:///eleclog.db', convert_unicode=True, connect_args={"check_same_thread": False})
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)