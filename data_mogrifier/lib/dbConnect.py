from sqlalchemy import create_engine, Column, Integer, String, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import lib.cFile
import configparser

Base = declarative_base()

class dbConnect:
    """

    """
    engine = create_engine('mysql://%s:%s@%s/%s' % ('', '', '', ''), encoding='utf8', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self, config_file='etc/settings.conf'):
        """
        :param config_file:
        :return:
        """
        self.config = configparser.ConfigParser()
        self.engine = None
        try:
            self.config.read(config_file)
        except FileNotFoundError:
            print("Warning. Configuration file does not exist.")
            lib.cFile.cFile(config_file)
            self.config.read(config_file)

    def connect(self):
        self.engine = create_engine('mysql://%s:%s@%s/%s' % (self.config['DB']['user'], self.config['DB']['password'], self.config['DB']['host'], self.config['DB']['database']), encoding='utf8', echo=False)

class Prisoners (Base):
    __tablename__ = 'prisoners_Phase2'
    id = Column(Integer, primary_key=True)
    phase1_id = Column(Integer)
    naam = Column(String(255))
    voornaam = Column(String(255))
    geboorteplaats = Column(String(255))
    geboorteplaats_nis = Column(String(255))
    geboorteplaats_8 = Column(Integer)
    geboorteplaats_1846 = Column(Integer)
    geboorteplaats_1876 = Column(Integer)
    geslacht = Column(String(255))
    misdrijf = Column(String(255))
    woonplaats = Column(String(255))
    woonplaats_nis = Column(String(255))
    woonplaats_8 = Column(Integer)
    woonplaats_1846 = Column(Integer)
    woonplaats_1876 = Column(Integer)
    beroep = Column(String(255))
    HISCO = Column(String(255))
    geboortejaar = Column(Integer)
    lichaamslengte = Column(Numeric)
    flag = Column(Integer)



class PrisonersMerged(Base):
    __tablename__ = 'prisoners_merged'
    id = Column(Integer, primary_key=True)
    Id_gedetineerde = Column(Integer, index=True)
    Naam = Column(String(255))
    Voornaam = Column(String(255))
    Geslacht = Column(String(255))
    Leeftijd = Column(String(255))
    Lichaamslengte = Column(String(255))
    Inschrijvingsdatum = Column(Date)
    Rolnummer = Column(String(255))
    Ontslagdatum = Column(String(255))
    Burgerlijke_staat = Column(String(255))
    Geletterdheid = Column(String(255))
    Pokkenletsel = Column(String(255))
    Verminkingen = Column(String(255))
    Beroep_letterlijk = Column(String(255))
    Beroep_vertaling = Column(String(255))
    Beroep_cat = Column(String(255))
    HISCO = Column(String(255))
    Misdrijf_letterlijk = Column(String(255))
    Misdrijf_vertaling = Column(String(255))
    Misdrijf_cat = Column(String(255))
    Rechtbank_plaats = Column(String(255))
    Rechtbank_soort = Column(String(255))
    Archief_bestand = Column(String(255))
    Archief_toegang = Column(String(255))
    Woonplaats_vertaling = Column(String(255))
    Woonplaats_NIS = Column(String(255))
    Woonplaats_8 = Column(Integer)
    Woonplaats_1846 = Column(Integer)
    Woonplaats_1876 = Column(Integer)
    Geboorteplaats_vertaling = Column(String(255))
    Geboorteplaats_NIS = Column(String(255))
    Geboorteplaats_8 = Column(Integer)
    Geboorteplaats_1846 = Column(Integer)
    Geboorteplaats_1876 = Column(Integer)

class OldPrisoners (Base):
    __tablename__ = 'prisoners_Phase1'
    id = Column(Integer, primary_key=True)
    n_id = Column(Integer)
    pp_id = Column(Integer)
    p_ID = Column(Integer)
    p_ID_old = Column(Integer)
    v_ID = Column(Integer)
    Naam = Column(String(255))
    Voornaam = Column(String(255))
    Geslacht = Column(String(255))
    Leeftijd = Column(String(255))
    Lichaamslengte = Column(String(255))
    Inschrijvingsdatum = Column(Date)
    Rolnummer = Column(String(255))
    Ontslagdatum = Column(String(255))
    Burgerlijke_staat = Column(String(255))
    Geletterdheid = Column(String(255))
    Pokkenletsel = Column(String(255))
    Verminkingen = Column(String(255))
    Beroep_letterlijk = Column(String(255))
    Beroep_vertaling = Column(String(255))
    Beroep_cat = Column(String(255))
    HISCO = Column(String(255))
    Misdrijf_letterlijk = Column(String(255))
    Misdrijf_vertaling = Column(String(255))
    Misdrijf_cat = Column(String(255))
    Rechtbank_plaats = Column(String(255))
    Rechtbank_soort = Column(String(255))
    Archief_bestand = Column(String(255))
    Archief_toegang = Column(String(255))
    Woonplaats_vertaling = Column(String(255))
    Woonplaats_NIS = Column(String(255))
    Woonplaats_8 = Column(Integer)
    Woonplaats_1846 = Column(Integer)
    Woonplaats_1876 = Column(Integer)
    Geboorteplaats_vertaling = Column(String(255))
    Geboorteplaats_NIS = Column(String(255))
    Geboorteplaats_8 = Column(Integer)
    Geboorteplaats_1846 = Column(Integer)
    Geboorteplaats_1876 = Column(Integer)
