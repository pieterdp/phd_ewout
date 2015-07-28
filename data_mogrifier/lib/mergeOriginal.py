from lib.dbConnect import PrisonersMerged, dbConnect
from lib.dbPrisonersMatch import PrisonersCheck, PrisonersMatch
from lib.dbOriginalTables import *
from sqlalchemy import and_, or_
from lib import matchTables
from lib import gbTables
from sqlalchemy.orm.exc import NoResultFound
import datetime
from lib.fResolve import fResolve
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class MergeOriginal(dbConnect):
    def mk_big_match(self):
        """
        Create a big match list from all the little ones
        PrisonersMatch
        :return:
        """
        lengine = create_engine(
            'mysql://%s:%s@%s/%s' % ('', '', '', ''),
            encoding='utf8',
            echo=True)
        lSession = sessionmaker(bind=lengine)
        lsession = lSession()
        gm = ['Aarsele', 'Aartrijke', 'Ardooie', 'Beernem', 'Bekegem', 'Blankenberge', 'Bredene', 'Brugge', 'Dadizele',
              'Damme',
              'Dentergem', 'Eernegem', 'Egem', 'Emelgem', 'Ettelgem', 'Gistel', 'Gits', 'Heist', 'Hooglede', 'Houtave',
              'Ichtegem', 'Ingelmunster', 'Izegem', 'Jabbeke', 'Kanegem', 'Klemskerke', 'Knokke', 'Koolskamp',
              'Lapscheure',
              'Leffinge', 'Lichtervelde', 'Loppem', 'Markegem', 'Meulebeke', 'Middelkerke', 'Moere', 'Moerkerke',
              'Moorslede',
              'Oedelem', 'Oostende', 'Oostkamp', 'Oostkerke', 'Oostrozebeke', 'Oudenburg', 'Pittem', 'Ramskapelle',
              'Roeselare',
              'Roksem', 'Ruddervoorde', 'Ruiselede', 'Rumbeke', 'Schuiferskapelle', 'Sijsele', 'SintJoris', 'Slijpe',
              'Snaaskerke', 'Snellegem', 'Stalhille', 'Stene', 'Tielt', 'Torhout', 'Uitkerke', 'Varsenare', 'Vlissegem',
              'Waardamme', 'Wakken', 'Westende', 'Westkapelle', 'Westkerke', 'Wilskerke', 'Wingene', 'Zandvoorde',
              'Zedelgem', 'Zerkegem', 'Zevekote', 'Zuienkerke', 'Zwevezele']
        gedetineerden = []
        for g in gm:
            g_c = getattr(gbTables, g)  # Gemeente
            m_c = getattr(matchTables, '%sMatch' % g)  # Match
            # Get all matches
            for match in lsession.query(m_c).all():
                # Get id_gedetineerde for master (0) & slave (1)
                master = lsession.query(g_c).filter(g_c.ID == match.id_matched).one()
                slave = lsession.query(g_c).filter(g_c.ID == match.id_match).one()
                gedetineerden.append((master.p_ID, slave.p_ID))
        for ged in gedetineerden:
            new_match = PrisonersMatch()
            new_match.id_gedetineerde_master = ged[0]
            new_match.id_gedetineerde_slave = ged[1]
            dbConnect.session.add(new_match)
            dbConnect.session.commit()
        return

    def merge(self):
        for g in dbConnect.session.query(Gedetineerde).filter(Gedetineerde.Id_gedetineerde >= 0).order_by(
                Gedetineerde.Id_gedetineerde).all():
            v = self.fetch_verblijf(g)  # 1 Gedetineerde = 1 Verblijf
            new_prisoner = PrisonersMerged()
            new_prisoner.Id_gedetineerde = g.Id_gedetineerde
            new_prisoner.Naam = g.Naam
            new_prisoner.Voornaam = g.Voornaam
            new_prisoner.Geslacht = g.Geslacht
            if v is not None:
                wp = self.fetch_item(v, 'woonplaats')  # 1 Gedetineerde = 1 Woonplaats
                gp = self.fetch_item(v, 'geboorteplaats')  # 1 Gedetineerde = 1 Geboorteplaats
                r = self.fetch_item(v, 'rechtbank')
                a = dbConnect.session.query(Archiefbestanden).filter(Archiefbestanden.Id_archief == v.Id_archief).one()
                new_prisoner.Leeftijd = v.Leeftijd
                new_prisoner.Lichaamslengte = v.Lichaamslengte_m
                new_prisoner.Inschrijvingsdatum = '%s-%s-%s' % (
                v.Inschrijvingsdatum_j, v.Inschrijvingsdatum_m, v.Inschrijvingsdatum_d)
                new_prisoner.Rolnummer = v.Rolnummer
                new_prisoner.Ontslagdatum = '%s-%s-%s' % (v.Ontslagdatum_j, v.Ontslagdatum_m, v.Ontslagdatum_d)
                new_prisoner.Burgerlijke_staat = v.Burgerlijke_staat
                new_prisoner.Geletterdheid = v.Geletterdheid
                new_prisoner.Pokkenletsel = v.Pokkenletsels
                new_prisoner.Verminkingen = v.Verminkingen
                new_prisoner.Beroep_letterlijk = self.merge_values(v, 'beroep', 'Beroep_letterlijk')
                new_prisoner.Beroep_vertaling = self.merge_values(v, 'beroep', 'Beroep_vertaling')
                new_prisoner.Beroep_cat = self.merge_values(v, 'beroep', 'Beroep_cat')
                new_prisoner.HISCO = self.merge_values(v, 'beroep', 'HISCO')
                new_prisoner.Misdrijf_letterlijk = self.merge_values(v, 'misdrijf', 'Misdrijf_letterlijk')
                new_prisoner.Misdrijf_vertaling = self.merge_values(v, 'misdrijf', 'Misdrijf_vertaling')
                new_prisoner.Misdrijf_cat = self.merge_values(v, 'misdrijf', 'Misdrijf_cat')
                if r is not None:
                    new_prisoner.Rechtbank_plaats = r.Plaats
                    new_prisoner.Rechtbank_soort = r.Soort
                if a is not None:
                    new_prisoner.Archief_bestand = a.Archiefbestand
                    new_prisoner.Archief_toegang = a.Toegang
                if wp is not None:
                    wp_extra = self.get_extra_woonplaats(wp.Plaatsnaam_vertaling)
                    new_prisoner.Woonplaats_vertaling = wp.Plaatsnaam_vertaling
                    new_prisoner.Woonplaats_NIS = wp_extra[3]
                    new_prisoner.Woonplaats_8 = wp_extra[0]
                    new_prisoner.Woonplaats_1846 = wp_extra[1]
                    new_prisoner.Woonplaats_1876 = wp_extra[2]
                if gp is not None:
                    new_prisoner.Geboorteplaats_vertaling = gp.Plaatsnaam_vertaling
                    new_prisoner.Geboorteplaats_NIS = gp.NIS_CODE
                    new_prisoner.Geboorteplaats_8 = gp.Jaar_VIII
                    new_prisoner.Geboorteplaats_1846 = gp.Jaar_1846
                    new_prisoner.Geboorteplaats_1876 = gp.Jaar_1876
            dbConnect.session.add(new_prisoner)
            dbConnect.session.commit()

    def match_check(self):
        for instance in dbConnect.session.query(PrisonersMerged).all():
            # Check whether Id_gedetineerde is a slave in big_match
            # If true; use fResolve to insert the information of the master
            # Else; insert information of this as master
            # In either case, insert the original als well
            check_prisoner = PrisonersCheck()
            check_prisoner.orig_id_gedetineerde = instance.Id_gedetineerde
            check_prisoner.orig_naam = instance.Naam
            check_prisoner.orig_voornaam = instance.Voornaam
            check_prisoner.orig_geboorteplaats = instance.Geboorteplaats_vertaling
            check_prisoner.orig_geboorteplaats_nis = instance.Geboorteplaats_NIS
            check_prisoner.orig_geboorteplaats_8 = instance.Geboorteplaats_8
            check_prisoner.orig_geboorteplaats_1846 = instance.Geboorteplaats_1846
            check_prisoner.orig_geboorteplaats_1876 = instance.Geboorteplaats_1876
            check_prisoner.orig_geslacht = instance.Geslacht
            check_prisoner.orig_misdrijf = instance.Misdrijf_vertaling
            check_prisoner.orig_woonplaats = instance.Woonplaats_vertaling
            check_prisoner.orig_woonplaats_nis = instance.Woonplaats_NIS
            check_prisoner.orig_woonplaats_8 = instance.Woonplaats_8
            check_prisoner.orig_woonplaats_1846 = instance.Woonplaats_1846
            check_prisoner.orig_woonplaats_1876 = instance.Woonplaats_1876
            check_prisoner.orig_beroep = instance.Beroep_vertaling
            check_prisoner.orig_HISCO = instance.HISCO
            if instance.Leeftijd is not None and instance.Inschrijvingsdatum is not None:
                geboortedatum = instance.Inschrijvingsdatum - datetime.timedelta(
                    days=int(instance.Leeftijd, base=10) * 365)
                check_prisoner.orig_geboortejaar = geboortedatum.year
            check_prisoner.orig_lichaamslengte = instance.Lichaamslengte
            master = dbConnect.session.query(PrisonersMatch).filter(
                PrisonersMatch.id_gedetineerde_slave == instance.Id_gedetineerde).first()
            is_master = dbConnect.session.query(PrisonersMatch).filter(
                PrisonersMatch.id_gedetineerde_master == instance.Id_gedetineerde).first()
            if is_master is not None or master is not None:
                all_prisoners = []
                if is_master is not None:
                    # This instance is in itself a master
                    # Master added
                    all_prisoners.append(dbConnect.session.query(PrisonersMerged).
                                         filter(and_(PrisonersMerged.Id_gedetineerde == is_master.id_gedetineerde_master, PrisonersMerged.Leeftijd > 21)).first())
                    # Add slaves
                    slaves = dbConnect.session.query(PrisonersMatch). \
                        filter(PrisonersMatch.id_gedetineerde_master == is_master.id_gedetineerde_master).all()
                    for slave in slaves:
                        all_prisoners.append(dbConnect.session.query(PrisonersMerged).
                                             filter(and_(PrisonersMerged.Id_gedetineerde == slave.id_gedetineerde_slave, PrisonersMerged.Leeftijd > 21)).first())
                    check_prisoner.merged_id = is_master.id_gedetineerde_master
                    check_prisoner.id_gedetineerde = is_master.id_gedetineerde_master
                elif master is not None:
                    # Get all slaves + the master as instances for fResolve
                    # Master added
                    all_prisoners.append(dbConnect.session.query(PrisonersMerged).
                                         filter(and_(PrisonersMerged.Id_gedetineerde == master.id_gedetineerde_master, PrisonersMerged.Leeftijd > 21)).first())
                    # Add primary slave
                    all_prisoners.append(dbConnect.session.query(PrisonersMerged).
                                         filter(and_(PrisonersMerged.Id_gedetineerde == master.id_gedetineerde_slave, PrisonersMerged.Leeftijd > 21)).first())
                    # Add slaves
                    slaves = dbConnect.session.query(PrisonersMatch). \
                        filter(and_(PrisonersMatch.id_gedetineerde_master == master.id_gedetineerde_master,
                                    PrisonersMatch.id_gedetineerde_slave != master.id_gedetineerde_slave)).all()
                    for slave in slaves:
                        all_prisoners.append(dbConnect.session.query(PrisonersMerged).
                                             filter(and_(PrisonersMerged.Id_gedetineerde == slave.id_gedetineerde_slave,
                                                         PrisonersMerged.Leeftijd > 21)).first())
                    check_prisoner.merged_id = master.id_gedetineerde_master
                    check_prisoner.id_gedetineerde = master.id_gedetineerde_master
                else:
                    raise Exception
                # New value
                resolve = fResolve()
                prisoner_list = []
                for p in all_prisoners:
                    if p is not None:
                        prisoner_list.append(p)
                if len(prisoner_list) != 0:
                    new_value = resolve.compare_instances(prisoner_list)
                    # Add to check_prisoner
                    check_prisoner.phase1_id = new_value['phase1_id']
                    check_prisoner.naam = new_value['naam']
                    check_prisoner.voornaam = new_value['voornaam']
                    check_prisoner.geboorteplaats = new_value['geboorteplaats']
                    check_prisoner.geboorteplaats_nis = new_value['geboorteplaats_nis']
                    check_prisoner.geboorteplaats_8 = new_value['geboorteplaats_8']
                    check_prisoner.geboorteplaats_1846 = new_value['geboorteplaats_1846']
                    check_prisoner.geboorteplaats_1876 = new_value['geboorteplaats_1876']
                    check_prisoner.geslacht = new_value['geslacht']
                    check_prisoner.misdrijf = new_value['misdrijf']
                    check_prisoner.woonplaats = new_value['woonplaats']
                    check_prisoner.woonplaats_nis = new_value['woonplaats_nis']
                    check_prisoner.woonplaats_8 = new_value['woonplaats_8']
                    check_prisoner.woonplaats_1846 = new_value['woonplaats_1846']
                    check_prisoner.woonplaats_1876 = new_value['woonplaats_1876']
                    check_prisoner.beroep = new_value['beroep']
                    check_prisoner.HISCO = new_value['HISCO']
                    check_prisoner.geboortejaar = new_value['geboortejaar']
                    check_prisoner.lichaamslengte = new_value['lichaamslengte']
                    check_prisoner.flag = new_value['flag']
                else:
                    check_prisoner.flag = 1
            else:
                check_prisoner.id_gedetineerde = instance.Id_gedetineerde
                check_prisoner.naam = instance.Naam
                check_prisoner.voornaam = instance.Voornaam
                check_prisoner.geboorteplaats = instance.Geboorteplaats_vertaling
                check_prisoner.geboorteplaats_nis = instance.Geboorteplaats_NIS
                check_prisoner.geboorteplaats_8 = instance.Geboorteplaats_8
                check_prisoner.geboorteplaats_1846 = instance.Geboorteplaats_1846
                check_prisoner.geboorteplaats_1876 = instance.Geboorteplaats_1876
                check_prisoner.geslacht = instance.Geslacht
                check_prisoner.misdrijf = instance.Misdrijf_vertaling
                check_prisoner.woonplaats = instance.Woonplaats_vertaling
                check_prisoner.woonplaats_nis = instance.Woonplaats_NIS
                check_prisoner.woonplaats_8 = instance.Woonplaats_8
                check_prisoner.woonplaats_1846 = instance.Woonplaats_1846
                check_prisoner.woonplaats_1876 = instance.Woonplaats_1876
                check_prisoner.beroep = instance.Beroep_vertaling
                check_prisoner.HISCO = instance.HISCO
                if instance.Leeftijd is not None and instance.Inschrijvingsdatum is not None:
                    geboortedatum = instance.Inschrijvingsdatum - datetime.timedelta(
                        days=int(instance.Leeftijd, base=10) * 365)
                    check_prisoner.geboortejaar = geboortedatum.year
                check_prisoner.lichaamslengte = instance.Lichaamslengte
            dbConnect.session.add(check_prisoner)
            dbConnect.session.commit()

    def fetch_verblijf(self, g):
        """
        Fetch the Verblijf corresponding to a Gedetineerde g
        :param g:
        :return:
        """
        return self.fetch_item(g, 'verblijf')

    def fetch_item(self, p, key):
        """
        Return a single item that has a one-to-many relationship defined, but is a one-to-one
        :param p:
        :param key:
        :return:
        """
        item_list = getattr(p, key)
        if len(item_list) > 1:
            for item in item_list:
                if item.Plaatsnaam_vertaling != 'Onbekend' and item.Plaatsnaam_vertaling is not None:
                    return item
        if len(item_list) < 1:
            return None
        return item_list[0]

    def get_extra_woonplaats(self, naam):
        if naam is None:
            return None, None, None, None
        gp = dbConnect.session.query(Geboorteplaats).filter(Geboorteplaats.Plaatsnaam_vertaling == naam).first()
        if gp is None:
            return None, None, None, None
        return gp.Jaar_VIII, gp.Jaar_1846, gp.Jaar_1876, gp.NIS_CODE

    def merge_values(self, parent, key, to_merge):
        l = getattr(parent, key)
        values = []
        for i in l:
            values.append(str(getattr(i, to_merge)))
        if len(values) == 0:
            return None
        return ';'.join(values)
