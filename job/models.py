#! -*- coding: utf-8 -*-

"""
Web Scraper Project

Scrape data from a regularly updated website livingsocial.com and
save to a database (postgres).

Database models part - defines table for storing scraped data.
Direct run will create the table.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()


def db_connect():
    """Performs database connection using database settings from settings.py.

    Returns sqlalchemy engine instance.

    """
    return create_engine(URL(**settings.DATABASE))

def create_jobs_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)

class Jobs(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    job_title = Column('title', String)
    company = Column('company', String, nullable=True)
    location = Column('location', String, nullable=True)
    date = Column('date', String, nullable=True)