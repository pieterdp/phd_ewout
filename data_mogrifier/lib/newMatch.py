from lib.dbConnect import PrisonersMerged, dbConnect
from lib.dbPrisonersMatch import PrisonersCheck, PrisonersMatch, PrisonersNew
from sqlalchemy import and_, or_, distinct
import datetime


class MergeNew(dbConnect):
    def new_merge(self):
        ##
        # First do all the normal cases, that are neither master or slave
        # Second, go through all the masters, get all their slaves and chose the one closest to 35 to enter into the db
        for instance in dbConnect.session.query(PrisonersMerged).filter(and_(PrisonersMerged.Leeftijd >= 18,
                                                                             PrisonersMerged.Leeftijd <= 50)).all():
            master = dbConnect.session.query(PrisonersMatch).filter(
                PrisonersMatch.id_gedetineerde_slave == instance.Id_gedetineerde).first()
            is_master = dbConnect.session.query(PrisonersMatch).filter(
                PrisonersMatch.id_gedetineerde_master == instance.Id_gedetineerde).first()
            # Year of birth
            if instance.Leeftijd is not None and instance.Inschrijvingsdatum is not None:
                dofb = instance.Inschrijvingsdatum - datetime.timedelta(days=int(instance.Leeftijd, base=10) * 365)
                yofb = dofb.year
            else:
                yofb = None
            # Normal case: no master or slave
            if master is None and is_master is None:
                new_prisoner = PrisonersNew()
                new_prisoner.id_gedetineerde = instance.Id_gedetineerde
                new_prisoner.naam = instance.Naam
                new_prisoner.voornaam = instance.Voornaam
                new_prisoner.geboorteplaats = instance.Geboorteplaats_vertaling
                new_prisoner.geboorteplaats_nis = instance.Geboorteplaats_NIS
                new_prisoner.geslacht = instance.Geslacht
                new_prisoner.misdrijf = instance.Misdrijf_vertaling
                new_prisoner.woonplaats = instance.Woonplaats_vertaling
                new_prisoner.woonplaats_nis = instance.Woonplaats_NIS
                new_prisoner.beroep = instance.Beroep_vertaling
                new_prisoner.leeftijd = instance.Leeftijd
                new_prisoner.geboortejaar = yofb
                new_prisoner.lichaamslengte = instance.Lichaamslengte
                new_prisoner.flag = 0
                dbConnect.session.add(new_prisoner)
                dbConnect.session.commit()
        # Go through all the matches
        for master in dbConnect.session.query(PrisonersMatch.id_gedetineerde_master).distinct(PrisonersMatch.id_gedetineerde_master):
            to_compare = []
            # Add master
            to_compare.append(dbConnect.session.query(PrisonersMerged).
                              filter(PrisonersMerged.Id_gedetineerde == master).first())
            # Add slaves
            slaves = dbConnect.session.query(PrisonersMatch).\
                filter(PrisonersMatch.id_gedetineerde_master == master).all()
            for slave in slaves:
                to_compare.append(dbConnect.session.query(PrisonersMerged).
                                  filter(PrisonersMerged.Id_gedetineerde == slave.id_gedetineerde_slave).first())
            # Sort based on abs(item.Leeftijd - 35).
            ordered_by_dist = sorted(to_compare, key=lambda item: abs(int(item.Leeftijd, base=10) - 35))
            # Now insert the first item
            to_insert = ordered_by_dist[0]
            # Year of birth
            if to_insert.Leeftijd is not None and to_insert.Inschrijvingsdatum is not None:
                dofb = to_insert.Inschrijvingsdatum - datetime.timedelta(days=int(to_insert.Leeftijd, base=10) * 365)
                yofb = dofb.year
            else:
                yofb = None
            new_prisoner = PrisonersNew()
            new_prisoner.id_gedetineerde = to_insert.Id_gedetineerde
            new_prisoner.naam = to_insert.Naam
            new_prisoner.voornaam = to_insert.Voornaam
            new_prisoner.geboorteplaats = to_insert.Geboorteplaats_vertaling
            new_prisoner.geboorteplaats_nis = to_insert.Geboorteplaats_NIS
            new_prisoner.geslacht = to_insert.Geslacht
            new_prisoner.misdrijf = to_insert.Misdrijf_vertaling
            new_prisoner.woonplaats = to_insert.Woonplaats_vertaling
            new_prisoner.woonplaats_nis = to_insert.Woonplaats_NIS
            new_prisoner.beroep = to_insert.Beroep_vertaling
            new_prisoner.leeftijd = to_insert.Leeftijd
            new_prisoner.geboortejaar = yofb
            new_prisoner.lichaamslengte = to_insert.Lichaamslengte
            new_prisoner.flag = 0
            dbConnect.session.add(new_prisoner)
            dbConnect.session.commit()
