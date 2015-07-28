__author__ = 'pieter'
from lib import gbTables
from lib import matchTables
import npyscreen
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

engine = create_engine(
    'mysql://%s:%s@%s/%s' % ('', '', '', ''), encoding='utf8',
    echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def select(*args):
    F = npyscreen.Form(name='ID or P_ID')
    title_text = '%s <> %s (P_ID) | %s <> %s (ID)' %\
                 ('%s %s' % (p_id[0].Naam, p_id[0].Voornaam),
                  '%s %s' % (p_id[1].Naam, p_id[1].Voornaam),
                  '%s %s' % (g_id[0].Naam, g_id[0].Voornaam),
                  '%s %s' % (g_id[1].Naam, g_id[1].Voornaam))
    values = ('P_ID', 'ID')
    id_or_pid = F.add(npyscreen.TitleSelectOne, name=title_text, values=values)
    F.edit()
    return id_or_pid.value


gm = ['Aarsele', 'Aartrijke', 'Ardooie', 'Beernem', 'Bekegem', 'Blankenberge', 'Bredene', 'Brugge', 'Dadizele', 'Damme',
      'Dentergem', 'Eernegem', 'Egem', 'Emelgem', 'Ettelgem', 'Gistel', 'Gits', 'Heist', 'Hooglede', 'Houtave',
      'Ichtegem', 'Ingelmunster', 'Izegem', 'Jabbeke', 'Kanegem', 'Klemskerke', 'Knokke', 'Koolskamp', 'Lapscheure',
      'Leffinge', 'Lichtervelde', 'Loppem', 'Markegem', 'Meulebeke', 'Middelkerke', 'Moere', 'Moerkerke', 'Moorslede',
      'Oedelem', 'Oostende', 'Oostkamp', 'Oostkerke', 'Oostrozebeke', 'Oudenburg', 'Pittem', 'Ramskapelle', 'Roeselare',
      'Roksem', 'Ruddervoorde', 'Ruiselede', 'Rumbeke', 'Schuiferskapelle', 'Sijsele', 'SintJoris', 'Slijpe',
      'Snaaskerke', 'Snellegem', 'Stalhille', 'Stene', 'Tielt', 'Torhout', 'Uitkerke', 'Varsenare', 'Vlissegem',
      'Waardamme', 'Wakken', 'Westende', 'Westkapelle', 'Westkerke', 'Wilskerke', 'Wingene', 'Zandvoorde',
      'Zedelgem', 'Zerkegem', 'Zevekote', 'Zuienkerke', 'Zwevezele']
f = open('match_list', 'w')
for g in gm:
    choices = ('P_ID', 'ID')
    g_c = getattr(gbTables, g)  # Gemeente
    m_c = getattr(matchTables, '%sMatch' % g)  # Match
    # Get the first match from m_c
    first = session.query(m_c).first()
    if first is None:
        # No matches, so nothing to do here
        continue
    # Use try & one()
    try:
        p_id = (
            session.query(g_c).filter(getattr(g_c, 'p_ID') == first.id_matched).one(),
            session.query(g_c).filter(getattr(g_c, 'p_ID') == first.id_match).one()
        )  # If they were matched using Id_gedetineerde ("P_ID"), these two should be similar
    except NoResultFound:
        f.write('%s:ID\n' % g)
        continue
    try:
        g_id = (
            session.query(g_c).filter(getattr(g_c, 'ID') == first.id_matched).one(),
            session.query(g_c).filter(getattr(g_c, 'ID') == first.id_match).one()
        )  # If they were matched using ID ("ID"), these two should be similar
    except NoResultFound:
        f.write('%s:P_ID\n' % g)
        continue
    choice = npyscreen.wrapper_basic(select)
    f.write('%s:%s\n' % (g, choices[choice[0]]))
f.close()
