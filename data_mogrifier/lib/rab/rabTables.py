__author__ = 'pieter'
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RABTable(Base):
    __tablename__ = 'RABTable'
    id = Column(Integer, primary_key=True)
    id_persoon_tabel = Column(String(64), index=True)
    Gepoorteplaats = Column(String(255), index=True)
    Geboortedatum = Column(String(255), index=True)
    Aktedatum = Column(String(255), index=True)
    Voornaam = Column(String(255), index=True)
    Naam = Column(String(255), index=True)
    Voornaam_vader = Column(String(255), index=True)
    Naam_vader = Column(String(255), index=True)
    Voornaam_moeder = Column(String(255), index=True)
    Naam_moeder = Column(String(255), index=True)
    Geboorteplaats_vader = Column(String(255), index=True)
    Geboorteplaats_moeder = Column(String(255), index=True)
    Beroep_vader = Column(String(255), index=True)
    Beroep_moeder = Column(String(255), index=True)

