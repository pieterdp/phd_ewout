__author__ = 'pieter'
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AarseleMatch(Base):
    __tablename__ = 'Aarsele_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class AartrijkeMatch(Base):
    __tablename__ = 'Aartrijke_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class ArdooieMatch(Base):
    __tablename__ = 'Ardooie_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class BeernemMatch(Base):
    __tablename__ = 'Beernem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class BekegemMatch(Base):
    __tablename__ = 'Bekegem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class BlankenbergeMatch(Base):
    __tablename__ = 'Blankenberge_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class BredeneMatch(Base):
    __tablename__ = 'Bredene_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class BruggeMatch(Base):
    __tablename__ = 'Brugge_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class DadizeleMatch(Base):
    __tablename__ = 'Dadizele_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class DammeMatch(Base):
    __tablename__ = 'Damme_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class DentergemMatch(Base):
    __tablename__ = 'Dentergem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class EernegemMatch(Base):
    __tablename__ = 'Eernegem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class EgemMatch(Base):
    __tablename__ = 'Egem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class EmelgemMatch(Base):
    __tablename__ = 'Emelgem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class EttelgemMatch(Base):
    __tablename__ = 'Ettelgem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class GistelMatch(Base):
    __tablename__ = 'Gistel_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class GitsMatch(Base):
    __tablename__ = 'Gits_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class HeistMatch(Base):
    __tablename__ = 'Heist_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class HoogledeMatch(Base):
    __tablename__ = 'Hooglede_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class HoutaveMatch(Base):
    __tablename__ = 'Houtave_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class IchtegemMatch(Base):
    __tablename__ = 'Ichtegem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class IngelmunsterMatch(Base):
    __tablename__ = 'Ingelmunster_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class IzegemMatch(Base):
    __tablename__ = 'Izegem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class JabbekeMatch(Base):
    __tablename__ = 'Jabbeke_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class KanegemMatch(Base):
    __tablename__ = 'Kanegem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class KlemskerkeMatch(Base):
    __tablename__ = 'Klemskerke_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class KnokkeMatch(Base):
    __tablename__ = 'Knokke_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class KoolskampMatch(Base):
    __tablename__ = 'Koolskamp_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class LapscheureMatch(Base):
    __tablename__ = 'Lapscheure_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class LeffingeMatch(Base):
    __tablename__ = 'Leffinge_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class LichterveldeMatch(Base):
    __tablename__ = 'Lichtervelde_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class LoppemMatch(Base):
    __tablename__ = 'Loppem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class MarkegemMatch(Base):
    __tablename__ = 'Markegem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class MeulebekeMatch(Base):
    __tablename__ = 'Meulebeke_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class MiddelkerkeMatch(Base):
    __tablename__ = 'Middelkerke_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class MoereMatch(Base):
    __tablename__ = 'Moere_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class MoerkerkeMatch(Base):
    __tablename__ = 'Moerkerke_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class MoorsledeMatch(Base):
    __tablename__ = 'Moorslede_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class OedelemMatch(Base):
    __tablename__ = 'Oedelem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class OostendeMatch(Base):
    __tablename__ = 'Oostende_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class OostkampMatch(Base):
    __tablename__ = 'Oostkamp_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class OostkerkeMatch(Base):
    __tablename__ = 'Oostkerke_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class OostrozebekeMatch(Base):
    __tablename__ = 'Oostrozebeke_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class OudenburgMatch(Base):
    __tablename__ = 'Oudenburg_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class PittemMatch(Base):
    __tablename__ = 'Pittem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class RamskapelleMatch(Base):
    __tablename__ = 'Ramskapelle_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class RoeselareMatch(Base):
    __tablename__ = 'Roeselare_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class RoksemMatch(Base):
    __tablename__ = 'Roksem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class RuddervoordeMatch(Base):
    __tablename__ = 'Ruddervoorde_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class RuiseledeMatch(Base):
    __tablename__ = 'Ruiselede_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class RumbekeMatch(Base):
    __tablename__ = 'Rumbeke_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class SchuiferskapelleMatch(Base):
    __tablename__ = 'Schuiferskapelle_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class SijseleMatch(Base):
    __tablename__ = 'Sijsele_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class SintJorisMatch(Base):
    __tablename__ = 'Sint-Joris_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class SlijpeMatch(Base):
    __tablename__ = 'Slijpe_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class SnaaskerkeMatch(Base):
    __tablename__ = 'Snaaskerke_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class SnellegemMatch(Base):
    __tablename__ = 'Snellegem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class StalhilleMatch(Base):
    __tablename__ = 'Stalhille_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class SteneMatch(Base):
    __tablename__ = 'Stene_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class TieltMatch(Base):
    __tablename__ = 'Tielt_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class TorhoutMatch(Base):
    __tablename__ = 'Torhout_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class UitkerkeMatch(Base):
    __tablename__ = 'Uitkerke_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class VarsenareMatch(Base):
    __tablename__ = 'Varsenare_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class VerblijfMatch(Base):
    __tablename__ = 'Verblijf_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class VlissegemMatch(Base):
    __tablename__ = 'Vlissegem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class WaardammeMatch(Base):
    __tablename__ = 'Waardamme_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class WakkenMatch(Base):
    __tablename__ = 'Wakken_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class WestendeMatch(Base):
    __tablename__ = 'Westende_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class WestkapelleMatch(Base):
    __tablename__ = 'Westkapelle_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class WestkerkeMatch(Base):
    __tablename__ = 'Westkerke_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class WilskerkeMatch(Base):
    __tablename__ = 'Wilskerke_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class WingeneMatch(Base):
    __tablename__ = 'Wingene_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class ZandvoordeMatch(Base):
    __tablename__ = 'Zandvoorde_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class ZedelgemMatch(Base):
    __tablename__ = 'Zedelgem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class ZerkegemMatch(Base):
    __tablename__ = 'Zerkegem_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class ZevekoteMatch(Base):
    __tablename__ = 'Zevekote_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class ZuienkerkeMatch(Base):
    __tablename__ = 'Zuienkerke_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)


class ZwevezeleMatch(Base):
    __tablename__ = 'Zwevezele_match'
    ID = Column(Integer, primary_key=True)
    id_matched = Column(Integer)
    id_match = Column(Integer)
