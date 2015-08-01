__author__ = 'pieter'

from .rabTables import *
from ..dbPrisonersMatch import PrisonersCheck
from ..dbConnect import dbConnect


class RABMerge(dbConnect):

    def add_check(self):
        for item in dbConnect.session.query(PrisonersCheck).all():
            if item.naam is not None:
                merged = RABMerged()
                merged.src_table = 'PrisonersCheck.id'
                merged.src_id = item.id
                merged.Geboorteplaats = item.geboorteplaats
                merged.Geboortedatum = item.geboortejaar
                merged.Naam = item.naam
                merged.Voornaam = item.voornaam
                dbConnect.session.add(merged)
                dbConnect.session.commit()

    def add_rab(self):
        i = 0
        for item in dbConnect.session.query(RABTable).filter(RABTable.id > 188).all():
            i += 1
            print("Item #%d" % i)
            merged = RABMerged()
            merged.src_table = 'RABTable.id'
            merged.src_id = item.id
            merged.Geboorteplaats = item.Geboorteplaats
            gb = item.Geboortedatum
            if gb is not None and gb != '':
                # 	25/8/1851 0:00:00
                gb_a = gb.split(' ')
                datum_a = gb_a[0].split('/')
                jaar = datum_a[2]
            else:
                jaar = None
            merged.Geboortedatum = jaar
            merged.Naam = item.Naam
            merged.Voornaam = item.Voornaam
            dbConnect.session.add(merged)
            dbConnect.session.commit()
