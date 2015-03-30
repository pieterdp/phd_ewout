from lib.dbMatch import dbMatch
from lib.fMatch import fuzzMatch
from lib.cFile import cFile
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

pbar = ProgressBar (widgets=[Percentage (), Bar ()], maxval=100).start ()

print ('Preparing matching:')
db_match = dbMatch (cli[2])
db_match.config_start ()
db_match.connect ()
db_match.matchPepare (cli[0], cli[1])
print ('Merging tables')
pbar.update (25)

print ('Comparing')
print (db_match.suggest_single (db_match.filterViews['Oostende'], [('Naam_a', 'Naam_b'), ('Voornaam_a', 'Voornaam_b')], ('ID_a', 1), 'ID_b'))
pbar.finish ()