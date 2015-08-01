__author__ = 'pieter'

from .rabTables import *
from ..dbPrisonersMatch import PrisonersCheck
from ..dbConnect import dbConnect
import re


class RABMerge(dbConnect):

    def add_check(self):
        i = 0
        f = open('RABMerged_pc.sql', 'w')
        for item in dbConnect.session.query(PrisonersCheck).all():
            i += 1
            print("Item #%d" % i)
            sql = "INSERT INTO RABMerged (src_table, src_id, Geboorteplaats, Geboortedatum, Naam, Voornaam) VALUES ('%s','%s','%s', '%s', '%s', '%s');\n"
            if item.naam is not None:
                semi = re.compile(';')
                if semi.match(str(item.geboorteplaats)):
                    g = item.geboorteplaats.split(';')
                    geboorteplaats = g[0]
                else:
                    geboorteplaats = item.geboorteplaats
                if semi.match(str(item.geboortejaar)):
                    g = item.geboortejaar.split(';')
                    geboortejaar = g[0]
                else:
                    geboortejaar = item.geboortejaar
                f.write(sql % ('PrisonersCheck.id', item.id, self.only_alpha(geboorteplaats), geboortejaar,
                               self.only_alpha(item.naam), self.only_alpha(item.voornaam)))
        f.close()

    def add_rab(self):
        i = 0
        f = open('RABMerged.sql', 'w')
        for item in dbConnect.session.query(RABTable).all():
            i += 1
            print("Item #%d" % i)  # 1 = 234
            sql = "INSERT INTO RABMerged (src_table, src_id, Geboorteplaats, Geboortedatum, Naam, Voornaam) VALUES ('%s','%s','%s', '%s', '%s', '%s');\n"
            gb = item.Geboortedatum
            if gb is not None and gb != '':
                # 	25/8/1851 0:00:00
                gb_a = gb.split(' ')
                datum_a = gb_a[0].split('/')
                jaar = datum_a[2]
            else:
                jaar = 'NULL'
            f.write(sql % ('RABTable.id', item.id, self.only_alpha(item.Geboorteplaats), jaar,
                           self.only_alpha(item.Naam), self.only_alpha(item.Voornaam)))
        f.close()

    def only_alpha(self, string):
        if string is not None:
            output = re.sub('[^a-z0-9A-Z -]', '', string)
        else:
            output = 'NULL'
        return output

