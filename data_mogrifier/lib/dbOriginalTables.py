__author__ = 'pieter'
from sqlalchemy import create_engine, Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base




Base = declarative_base()

class Archiefbestanden(Base):
    __tablename__ = 'Archiefbestanden'
    Id_archief = Column(Integer, primary_key=True, autoincrement=True)
    Archiefbewaarplaats = Column(String(255), nullable=True)
    Toegang = Column(String(255), nullable=True)
    Archiefbestand = Column(String(255), nullable=True)
    Gevangenis = Column(String(255), nullable=True)
    Afdeling = Column(String(255), nullable=True)
    Opmerkingen = Column(String(255), nullable=True)
    Uitgebreide_beschrijving = Column(String(512), nullable=True)
    verblijf = relationship('Verblijf')  # One-To-Many

class Verblijf(Base):
    __tablename__ = 'Verblijf'
    Id_verblijf = Column(Integer, primary_key=True, autoincrement=True)
    Id_ged = Column(Integer, ForeignKey('Gedetineerde.Id_gedetineerde'))
    Id_archief = Column(Integer, ForeignKey('Archiefbestanden.Id_archief'))
    Rolnummer = Column(String(64), index=True)
    Inschrijvingsdatum_d = Column(Integer, index=True, nullable=True)
    Inschrijvingsdatum_m = Column(Integer, index=True, nullable=True)
    Inschrijvingsdatum_j = Column(Integer, index=True, nullable=True)
    Leeftijd = Column(Integer, index=True, nullable=True)
    Lichaamslengte_m = Column(String(255), index=True, nullable=True)
    Lichaamslengte_andere = Column(String(255), nullable=True)
    Lichaamsgewicht_opname = Column(Numeric, nullable=True)
    Lichaamsgewicht_ontslag = Column(Numeric, nullable=True)
    Ontslagdatum_d = Column(Integer, nullable=True)
    Ontslagdatum_m = Column(Integer, nullable=True)
    Ontslagdatum_j = Column(Integer, nullable=True)
    Burgerlijke_staat = Column(String(64), nullable=True, index=True)
    Geletterdheid = Column(String(255), nullable=True)
    Pokkenletsels = Column(Integer, nullable=True, index=True)
    Verminkingen = Column(String(255), nullable=True)
    Opmerkingen = Column(String(255), nullable=True)
    beroep = relationship('Beroep')  # One-To-Many
    geboorteplaats = relationship('Geboorteplaats')  # One-To-Many
    woonplaats = relationship('Woonplaats')  # One-To-Many
    misdrijf = relationship('Misdrijf')  # One-To-Many
    rechtbank = relationship('Rechtbank')  # One-To-Many
    strafmaat = relationship('Strafmaat')  # One-To-Many

class Beroep(Base):
    __tablename__ = 'Beroep'
    Id_beroep = Column(Integer, primary_key=True, autoincrement=True)
    Id_verb = Column(Integer, ForeignKey('Verblijf.Id_verblijf'))
    Beroep_letterlijk = Column(String(255), nullable=True)
    Beroep_vertaling = Column(String(255), nullable=True, index=True)
    Beroep_cat = Column(String(255), nullable=True, index=True)
    HISCO = Column(Integer, index=True, nullable=True)

class Geboorteplaats(Base):
    __tablename__ = 'Geboorteplaats'
    Id_geboorteplaats = Column(Integer, primary_key=True, autoincrement=True)
    Id_verbl = Column(Integer, ForeignKey('Verblijf.Id_verblijf'))
    Plaatsnaam_letterlijk = Column(String(255), nullable=True)
    Plaatsnaam_vertaling = Column(String(255), index=True, nullable=True)
    Plaatsnaam_NIS = Column(String(64), index=True, nullable=True)
    NIS_CODE = Column(String(64), index=True, nullable=True)
    Jaar_VIII = Column(Integer, nullable=True, index=True)
    Jaar_1846 = Column(Integer, nullable=True, index=True)
    Jaar_1876 = Column(Integer, nullable=True, index=True)

class Woonplaats(Base):
    __tablename__ = 'Woonplaats'
    Id_woonplaats = Column(Integer, primary_key=True, autoincrement=True)
    Id_verbl = Column(Integer, ForeignKey('Verblijf.Id_verblijf'))
    Plaatsnaam_letterlijk = Column(String(255), nullable=True)
    Plaatsnaam_vertaling = Column(String(255), index=True, nullable=True)
    Plaatsnaam_NIS = Column(String(64), index=True, nullable=True)

class Gedetineerde(Base):
    __tablename__ = 'Gedetineerde'
    Id_gedetineerde = Column(Integer, primary_key=True, autoincrement=True)
    Voornaam = Column(String(255), index=True, nullable=True)
    Naam = Column(String(255), index=True, nullable=True)
    Geslacht = Column(String(32), nullable=True, index=True)
    Geboortedag = Column(Integer, nullable=True)
    Geboortemaand = Column(Integer, nullable=True)
    Geboortejaar = Column(Integer, nullable=True, index=True)
    Opmerkingen = Column(String(512), nullable=True)

    verblijf = relationship('Verblijf')  # Is One-To-Many because duplicate 'gedetineerden' are represented
    # as multiple rows in this table

class Misdrijf(Base):
    __tablename__ = 'Misdrijf'
    Id_misdrijf = Column(Integer, primary_key=True, autoincrement=True)
    Id_verbl = Column(Integer, ForeignKey('Verblijf.Id_verblijf'))
    Misdrijf_letterlijk = Column(String(255), nullable=True)
    Misdrijf_vertaling = Column(String(255), nullable=True, index=True)
    Misdrijf_cat = Column(String(255), nullable=True, index=True)

class Rechtbank(Base):
    __tablename__ = 'Rechtbank'
    Id_rechtbank = Column(Integer, primary_key=True, autoincrement=True)
    Id_verb = Column(Integer, ForeignKey('Verblijf.Id_verblijf'))
    Plaats = Column(String(255), nullable=True)
    Soort = Column(String(255), nullable=True, index=True)

class Strafmaat(Base):
    __tablename__ = 'Strafmaat'
    Id_strafmaat = Column(Integer, primary_key=True, autoincrement=True)
    Id_verb = Column(Integer, ForeignKey('Verblijf.Id_verblijf'))
    Straf_d = Column(Integer, nullable=True)
    Straf_m = Column(Integer, nullable=True)
    Straf_j = Column(Integer, nullable=True)
    Levenslang = Column(Integer, nullable=True)
    Doodstraf = Column(Integer, nullable=True)
    Strafvermindering = Column(String(255), nullable=True)
    Andere = Column(String(255), nullable=True)

