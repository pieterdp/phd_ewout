from lib.dbMatch import dbMatch
from lib.aMatch import aMatch
from lib.cFile import cFile
from lib.dbConnect import dbConnect
from progressbar import ProgressBar, Percentage, Bar
import sys
import getopt


"""
Command-line options
"""


def parse_cli (argv):
    try:
        opts, args = getopt.getopt (argv, "f:c:t:", ["filter=", "columns=", "table="])
    except getopt.GetoptError:
        usage ()
        sys.exit (2)
    for opt, arg in opts:
        if opt in ('-f', '--filter'):
            filter_column = arg
        elif opt in ('-c', '--columns'):
            columns = arg
            columns.split (',')
        elif opt in ('-t', '--table'):
            table = arg
        else:
            usage ()
            sys.exit (2)
    source = "".join (args)
    return (filter_column, columns, table, source)


def usage ():
    pass


"""
Configuration options
"""
cf = cFile ('etc/settings.conf')

"""
Application
"""
if __name__ == "__main__":
    cli = parse_cli (sys.argv[1:])
else:
    sys.exit (-1)


print ('Preparing matching:')
db_match = dbMatch (cli[2], cli[2] + "_match")
db_match.config_start ()
db_match.connect ()
db_match.matchPepare (cli[0], cli[1].split (','), 'ID')
print ('Merging tables')

print ('Comparing')
single = db_match.suggest_single (db_match.filterViews['Wakkerdam'], [('Naam_a', 'Naam_b'), ('Voornaam_a', 'Voornaam_b')], ('ID_a', 2049), 'ID_b', 'ID')
amatch = aMatch ()
r = amatch.matchCompare (single, ['Naam_a', 'Voornaam_a'])
print (r)
sys.exit ()
m = db_match.match_single(r)
print (m)
for (id, sc, av) in m:
    print (id)
    sf = db_match.get_single_item_by_id (id, 'app_test')
    sf = [str (s) for s in sf]
    print (" ".join (sf))