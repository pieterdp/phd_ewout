from statistics import mean, median, mode, StatisticsError
from math import floor

class fResolve:

    def __init__(self):
        self.instances = []

    def compare_instances(self, instances):
        if type(instances) is not list:
            raise Exception('Error: input is not a list!')
        self.instances = instances
        l = self.coalesce_lichaamslengte()
        j = self.coalesce_geboortejaar()
        b = self.coalesce_beroep()
        m = self.coalesce_misdrijf()
        g = self.coalesce_place('Geboorteplaats')
        w = self.coalesce_place('Woonplaats')
        return {
            'phase1_id': getattr(instances[0], 'p_ID'),
            'naam': getattr(instances[0], 'Naam'),
            'voornaam': getattr(instances[0], 'Voornaam'),
            'geboorteplaats': g['place'],
            'geboorteplaats_nis': g['nis'],
            'geboorteplaats_8': g['8'],
            'geboorteplaats_1846': g['1846'],
            'geboorteplaats_1876': g['1876'],
            'geslacht': getattr(instances[0], 'Geslacht'),
            'misdrijf': m,
            'woonplaats': w['place'],
            'woonplaats_nis': w['nis'],
            'woonplaats_8': w['8'],
            'woonplaats_1846': w['1846'],
            'woonplaats_1876': w['1876'],
            'beroep': b['beroep'],
            'HISCO': b['HISCO'],
            'geboortejaar': j,
            'lichaamslengte': l['lichaamslengte'],
            'flag': l['flag']
        }

    def coalesce_lichaamslengte (self):
        """
        sort: if diff (0, max) > 5; flag
        :param instances:
        :return:
        """
        lichaamslengte = []
        for instance in self.instances:
            if getattr(instance, 'Lichaamslengte') is not None:
                lichaamslengte.append(float(getattr(instance, 'Lichaamslengte')))
        lichaamslengte = sorted(lichaamslengte)
        flag = 0
        try:
            m = mode(lichaamslengte)
        except StatisticsError:
            try:
                m = mean(lichaamslengte)
            except StatisticsError:
                m = 0
                flag = 1
        if flag != 1:
            if (lichaamslengte[len(lichaamslengte) - 1] - lichaamslengte[0]) > 5:
                flag = 1
        return {
            'lichaamslengte': m,
            'flag': flag
        }

    def coalesce_geboortejaar (self):
        """

        :param instances:
        :return:
        """
        geboortejaar = []
        for instance in self.instances:
            age = 0
            yofi = 0
            if getattr(instance, 'Leeftijd') is not None:
                age = int(getattr(instance, 'Leeftijd'))
            if getattr(instance, 'Inschrijvingsdatum') is not None:
                yofi = getattr(instance, 'Inschrijvingsdatum')
                yofi = int(yofi[0:4])
            geboortejaar.append(yofi - age)
        """
        Get the mode; if there isn't one, use mean (round down)
        """
        try:
            m = mode(geboortejaar)
        except StatisticsError:
            m = floor(mean(geboortejaar))
        return m

    def coalesce_beroep (self):
        """
        :param instances:
        :return:
        """
        beroepen = {}  # key = hisco; value = beroep
        for instance in self.instances:
            if getattr(instance, 'HISCO') is not None:
                beroepen[getattr(instance, 'HISCO')] = getattr(instance, 'Beroep_vertaling')
        # Sort keys
        k = sorted(beroepen.keys())
        if len(k) == 0:
            return {
                'HISCO': -1,
                'beroep': ''
            }
        return {
            'HISCO': k[0],
            'beroep': beroepen[k[0]]
        }

    def coalesce_misdrijf (self):
        """
        :param instances:
        :return:
        """
        misdrijf=[]
        for instance in self.instances:
            if getattr(instance, 'Misdrijf_vertaling') is not None:
                misdrijf.append(getattr(instance, 'Misdrijf_vertaling'))
        return ';'.join(misdrijf)

    def coalesce_place(self, type):
        """
        :param instances:
        :param type: geboorteplaats or woonplaats
        :return dict:
        """
        places = {}
        group = []
        for instance in self.instances:
            if getattr(instance, '%s_vertaling' % type) is not None:
                place = getattr(instance, '%s_vertaling' % type)
                places[place] = 0
                group.append({
                    'place': getattr(instance, '%s_vertaling' % type),
                    'nis': getattr(instance, '%s_NIS' % type),
                    '8': getattr(instance, '%s_8' % type),
                    '1846': getattr(instance, '%s_1846' % type),
                    '1876': getattr(instance, '%s_1876' % type)
                })
        if len(group) == 0:
            group = [
                {
                    'place': '',
                    'nis': '',
                    '8': 0,
                    '1846': 0,
                    '1876': 0
                }
            ]
        if len(list(places.keys())) != 0:
            coalesced = {
                'place': [],
                'nis': [],
                '8': [],
                '1846': [],
                '1876': []
            }
            for g in group:
                coalesced['place'].append(g['place'])
                coalesced['nis'].append(g['nis'])
                coalesced['8'].append(str(g['8']))
                coalesced['1846'].append(str(g['1846']))
                coalesced['1876'].append(str(g['1876']))
            return {
                'place': ';'.join(coalesced['place']),
                'nis': ';'.join(coalesced['nis']),
                '8': ';'.join(coalesced['8']),
                '1846': ';'.join(coalesced['1846']),
                '1876': ';'.join(coalesced['1876'])
            }
        else:
            return {
                'place': group[0]['place'],
                'nis': group[0]['nis'],
                '8': group[0]['8'],
                '1846': group[0]['1846'],
                '1876': group[0]['1876']
            }
