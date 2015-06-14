from .dbConnect import dbConnect, Prisoners, OldPrisoners
from .fResolve import fResolve
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

class dbFetch:

    def __init__(self):
        """
        :return:
        """
        self.dbi = dbConnect()
        self.dbi.connect()
        session = sessionmaker(bind=self.dbi.engine)
        self.session = session()
        self.oldList = {}
        self.newList = {}
        self.f_resolve = fResolve ()

    def mergePrisoners(self):
        """
        :return:
        """
        for instance in self.session.query(OldPrisoners).filter(and_(OldPrisoners.Leeftijd > 22, OldPrisoners.Leeftijd < 51, OldPrisoners.Lichaamslengte > 140, OldPrisoners.Lichaamslengte < 190)):
            if instance.p_ID not in self.oldList:
                self.oldList[instance.p_ID] = [instance]
            else:
                self.oldList[instance.p_ID].append(instance)

    def comparePrisoners(self):
        for p_ID, instances in self.oldList.items():
            self.newList[p_ID] = self.f_resolve.compare_instances(instances)

    def storePrisoners(self):
        for p_ID, item in self.newList.items():
            self.session.add(Prisoners(
                phase1_id=item['phase1_id'],
                naam=item['naam'],
                voornaam=item['voornaam'],
                geboorteplaats=item['geboorteplaats'],
                geboorteplaats_nis=item['geboorteplaats_nis'],
                geboorteplaats_8=item['geboorteplaats_8'],
                geboorteplaats_1846=item['geboorteplaats_1846'],
                geboorteplaats_1876=item['geboorteplaats_1876'],
                geslacht=item['geslacht'],
                misdrijf=item['misdrijf'],
                woonplaats=item['woonplaats'],
                woonplaats_nis=item['woonplaats_nis'],
                woonplaats_8=item['woonplaats_8'],
                woonplaats_1846=item['woonplaats_1846'],
                woonplaats_1876=item['woonplaats_1876'],
                beroep=item['beroep'],
                HISCO=item['HISCO'],
                geboortejaar=item['geboortejaar'],
                lichaamslengte=item['lichaamslengte'],
                flag=item['flag']
            ))
        self.session.commit()
