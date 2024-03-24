# lib/models/__init__.py

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import logging
import sys

logging.getLogger('sqlalchemy').setLevel(logging.WARNING)
engine = create_engine('sqlite:///basketball_management.db', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

def create_tables():
    Base.metadata.create_all(engine)
