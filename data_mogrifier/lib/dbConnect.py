from sqlalchemy import create_engine, Column, Integer, String, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base
import lib.cFile
import configparser

Base = declarative_base()

class dbConnect:
    """

    """

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
        self.engine = create_engine('mysql://%s:%s@%s/%s' % (self.config['DB']['user'], self.config['DB']['password'], self.config['DB']['host'], self.config['DB']['database']), encoding='utf8', echo=True)

class Prisoners (Base):
    __tablename__ = 'prisoners_Phase2'
    id = Column(Integer, primary_key=True)
    phase1_id = Column(Integer)
    naam = Column(String)
    voornaam = Column(String)
    geboorteplaats = Column(String)
    geboorteplaats_nis = Column(String)
    geboorteplaats_8 = Column(Integer)
    geboorteplaats_1846 = Column(Integer)
    geboorteplaats_1876 = Column(Integer)
    geslacht = Column(String)
    misdrijf = Column(String)
    woonplaats = Column(String)
    woonplaats_nis = Column(String)
    woonplaats_8 = Column(Integer)
    woonplaats_1846 = Column(Integer)
    woonplaats_1876 = Column(Integer)
    beroep = Column(String)
    HISCO = Column(String)
    geboortejaar = Column(Integer)
    lichaamslengte = Column(Numeric)
    flag = Column(Integer)

class OldPrisoners (Base):
    __tablename__ = 'prisoners_Phase1'
    id = Column(Integer, primary_key=True)
    n_id = Column(Integer)
    pp_id = Column(Integer)
    p_ID = Column(Integer)
    p_ID_old = Column(Integer)
    v_ID = Column(Integer)
    Naam = Column(String)
    Voornaam = Column(String)
    Geslacht = Column(String)
    Leeftijd = Column(String)
    Lichaamslengte = Column(String)
    Inschrijvingsdatum = Column(Date)
    Rolnummer = Column(String)
    Ontslagdatum = Column(String)
    Burgerlijke_staat = Column(String)
    Geletterdheid = Column(String)
    Pokkenletsel = Column(String)
    Verminkingen = Column(String)
    Beroep_letterlijk = Column(String)
    Beroep_vertaling = Column(String)
    Beroep_cat = Column(String)
    HISCO = Column(String)
    Misdrijf_letterlijk = Column(String)
    Misdrijf_vertaling = Column(String)
    Misdrijf_cat = Column(String)
    Rechtbank_plaats = Column(String)
    Rechtbank_soort = Column(String)
    Archief_bestand = Column(String)
    Archief_toegang = Column(String)
    Woonplaats_vertaling = Column(String)
    Woonplaats_NIS = Column(String)
    Woonplaats_8 = Column(Integer)
    Woonplaats_1846 = Column(Integer)
    Woonplaats_1876 = Column(Integer)
    Geboorteplaats_vertaling = Column(String)
    Geboorteplaats_NIS = Column(String)
    Geboorteplaats_8 = Column(Integer)
    Geboorteplaats_1846 = Column(Integer)
    Geboorteplaats_1876 = Column(Integer)
