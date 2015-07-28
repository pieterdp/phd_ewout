__author__ = 'pieter'
from sqlalchemy import create_engine, Column, Integer, String, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class PrisonersCheck(Base):
    __tablename__ = 'prisoners_check'
    id = Column(Integer, primary_key=True)
    merged_id = Column(Integer)
    id_gedetineerde = Column(Integer)
    naam = Column(String(255))
    voornaam = Column(String(255))
    geboorteplaats = Column(String(255))
    geboorteplaats_nis = Column(String(255))
    geboorteplaats_8 = Column(String(255))
    geboorteplaats_1846 = Column(String(255))
    geboorteplaats_1876 = Column(String(255))
    geslacht = Column(String(255))
    misdrijf = Column(String(255))
    woonplaats = Column(String(255))
    woonplaats_nis = Column(String(255))
    woonplaats_8 = Column(String(255))
    woonplaats_1846 = Column(String(255))
    woonplaats_1876 = Column(String(255))
    beroep = Column(String(255))
    HISCO = Column(String(255))
    geboortejaar = Column(String(255))
    lichaamslengte = Column(String(255))
    orig_id_gedetineerde = Column(Integer)
    orig_naam = Column(String(255))
    orig_voornaam = Column(String(255))
    orig_geboorteplaats = Column(String(255))
    orig_geboorteplaats_nis = Column(String(255))
    orig_geboorteplaats_8 = Column(Integer)
    orig_geboorteplaats_1846 = Column(Integer)
    orig_geboorteplaats_1876 = Column(Integer)
    orig_geslacht = Column(String(255))
    orig_misdrijf = Column(String(255))
    orig_woonplaats = Column(String(255))
    orig_woonplaats_nis = Column(String(255))
    orig_woonplaats_8 = Column(Integer)
    orig_woonplaats_1846 = Column(Integer)
    orig_woonplaats_1876 = Column(Integer)
    orig_beroep = Column(String(255))
    orig_HISCO = Column(String(255))
    orig_geboortejaar = Column(Integer)
    orig_lichaamslengte = Column(String(255))
    flag = Column(Integer)

class PrisonersMatch(Base):
    __tablename__ = 'prisoners_match'
    id = Column(Integer, primary_key=True)
    id_gedetineerde_master = Column(Integer, index=True)
    id_gedetineerde_slave = Column(Integer, index=True)
