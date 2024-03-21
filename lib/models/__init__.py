# lib/models/__init__.py

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///basketball_management.db', echo=True)
Base = declarative_base()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
