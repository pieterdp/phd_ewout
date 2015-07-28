__author__ = 'pieter'
from sqlalchemy import Column, Integer, String, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Aarsele(Base):
    __tablename__ = 'Aarsele'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Aartrijke(Base):
    __tablename__ = 'Aartrijke'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Ardooie(Base):
    __tablename__ = 'Ardooie'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Beernem(Base):
    __tablename__ = 'Beernem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Bekegem(Base):
    __tablename__ = 'Bekegem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Blankenberge(Base):
    __tablename__ = 'Blankenberge'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Bredene(Base):
    __tablename__ = 'Bredene'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Brugge(Base):
    __tablename__ = 'Brugge'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Dadizele(Base):
    __tablename__ = 'Dadizele'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Damme(Base):
    __tablename__ = 'Damme'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Dentergem(Base):
    __tablename__ = 'Dentergem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Eernegem(Base):
    __tablename__ = 'Eernegem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Egem(Base):
    __tablename__ = 'Egem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Emelgem(Base):
    __tablename__ = 'Emelgem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Ettelgem(Base):
    __tablename__ = 'Ettelgem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Gistel(Base):
    __tablename__ = 'Gistel'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Gits(Base):
    __tablename__ = 'Gits'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Heist(Base):
    __tablename__ = 'Heist'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Hooglede(Base):
    __tablename__ = 'Hooglede'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Houtave(Base):
    __tablename__ = 'Houtave'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Ichtegem(Base):
    __tablename__ = 'Ichtegem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Ingelmunster(Base):
    __tablename__ = 'Ingelmunster'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Izegem(Base):
    __tablename__ = 'Izegem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Jabbeke(Base):
    __tablename__ = 'Jabbeke'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Kanegem(Base):
    __tablename__ = 'Kanegem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Klemskerke(Base):
    __tablename__ = 'Klemskerke'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Knokke(Base):
    __tablename__ = 'Knokke'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Koolskamp(Base):
    __tablename__ = 'Koolskamp'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Lapscheure(Base):
    __tablename__ = 'Lapscheure'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Leffinge(Base):
    __tablename__ = 'Leffinge'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Lichtervelde(Base):
    __tablename__ = 'Lichtervelde'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Loppem(Base):
    __tablename__ = 'Loppem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Markegem(Base):
    __tablename__ = 'Markegem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Meulebeke(Base):
    __tablename__ = 'Meulebeke'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Middelkerke(Base):
    __tablename__ = 'Middelkerke'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Moere(Base):
    __tablename__ = 'Moere'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Moerkerke(Base):
    __tablename__ = 'Moerkerke'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Moorslede(Base):
    __tablename__ = 'Moorslede'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Oedelem(Base):
    __tablename__ = 'Oedelem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Oostende(Base):
    __tablename__ = 'Oostende'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Oostkamp(Base):
    __tablename__ = 'Oostkamp'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Oostkerke(Base):
    __tablename__ = 'Oostkerke'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Oostrozebeke(Base):
    __tablename__ = 'Oostrozebeke'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Oudenburg(Base):
    __tablename__ = 'Oudenburg'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Pittem(Base):
    __tablename__ = 'Pittem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Ramskapelle(Base):
    __tablename__ = 'Ramskapelle'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Roeselare(Base):
    __tablename__ = 'Roeselare'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Roksem(Base):
    __tablename__ = 'Roksem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Ruddervoorde(Base):
    __tablename__ = 'Ruddervoorde'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Ruiselede(Base):
    __tablename__ = 'Ruiselede'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Rumbeke(Base):
    __tablename__ = 'Rumbeke'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Schuiferskapelle(Base):
    __tablename__ = 'Schuiferskapelle'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Sijsele(Base):
    __tablename__ = 'Sijsele'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class SintJoris(Base):
    __tablename__ = 'Sint-Joris'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Slijpe(Base):
    __tablename__ = 'Slijpe'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Snaaskerke(Base):
    __tablename__ = 'Snaaskerke'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Snellegem(Base):
    __tablename__ = 'Snellegem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Stalhille(Base):
    __tablename__ = 'Stalhille'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Stene(Base):
    __tablename__ = 'Stene'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Tielt(Base):
    __tablename__ = 'Tielt'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Torhout(Base):
    __tablename__ = 'Torhout'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Uitkerke(Base):
    __tablename__ = 'Uitkerke'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Varsenare(Base):
    __tablename__ = 'Varsenare'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Verblijf(Base):
    __tablename__ = 'Verblijf'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Vlissegem(Base):
    __tablename__ = 'Vlissegem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Waardamme(Base):
    __tablename__ = 'Waardamme'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Wakken(Base):
    __tablename__ = 'Wakken'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Westende(Base):
    __tablename__ = 'Westende'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Westkapelle(Base):
    __tablename__ = 'Westkapelle'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Westkerke(Base):
    __tablename__ = 'Westkerke'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Wilskerke(Base):
    __tablename__ = 'Wilskerke'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Wingene(Base):
    __tablename__ = 'Wingene'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Zandvoorde(Base):
    __tablename__ = 'Zandvoorde'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Zedelgem(Base):
    __tablename__ = 'Zedelgem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Zerkegem(Base):
    __tablename__ = 'Zerkegem'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Zevekote(Base):
    __tablename__ = 'Zevekote'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Zuienkerke(Base):
    __tablename__ = 'Zuienkerke'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)


class Zwevezele(Base):
    __tablename__ = 'Zwevezele'
    ID = Column(Integer, primary_key=True)
    p_ID = Column(Integer)
    Inschrijvingsdatum = Column(String)
    Geboorteplaats = Column(String)
    Leeftijd = Column(String)
    Naam = Column(String)
    Voornaam = Column(String)
    matched = Column(String)
    Lichaamslengte = Column(String)
