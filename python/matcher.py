from lib.dbMatch import dbMatch
from lib.fMatch import fuzzMatch
from lib.cFile import cFile
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


def update_progress(progress):
    print ('\r[{0}] {1}%'.format('#'*(progress/10), progress))

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
db_match = dbMatch (cli[2])
db_match.config_start ()
db_match.connect ()
#try:
db_match.matchPepare (cli[0], cli[1])
#except Exception:
#    e = sys.exc_info()[0]
#    print ("Error: %s" % e)
#    sys.exit (3)
print ('Merging tables')
update_progress (250)