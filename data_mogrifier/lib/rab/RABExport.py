__author__ = 'pieter'

from ..dbConnect import dbConnect
from .rabTables import RABMerged
import re


class RABExport(dbConnect):

    def export_as_file(self, filename):
        f = open(filename, 'w')
        i = 0
        for item in dbConnect.session.query(RABMerged).order_by(RABMerged.Geboorteplaats, RABMerged.Geboortedatum,
                                                                RABMerged.Naam, RABMerged.Voornaam).all():
            i += 1
            print('Item #%d' % i)
            semicolon = re.compile(';')
            to_out = [item.Geboorteplaats, item.Geboortedatum, item.Naam, item.Voornaam, item.src_table, item.src_id]
            if semicolon.search(item.Geboorteplaats) is not None:
                to_out[0] = item.Geboorteplaats.split(';')
                to_out[0] = to_out[0][0]
            if semicolon.search(item.Geboortedatum) is not None:
                to_out[1] = item.Geboortedatum.split(';')
                to_out[1] = to_out[1][0]
            f.write('%s\n' % self.as_string(to_out))
        f.close()

    def as_string(self, item_array):
        output_string = '{0};{1};{2};{3}|{4};{5}'
        items = tuple(item_array)
        return output_string.format(*items)
