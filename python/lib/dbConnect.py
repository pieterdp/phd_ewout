import sqlalchemy as mysql
import configparser
import cFile


class dbConnect:
    """
    Functions to connect to the DB
    """
    def __init__ (self, config_file = 'etc/settings.conf'):
        self.config_start (config_file)

    def config_start (self, config_file = 'etc/settings.conf'):
        """
        Function to load the configuration file
        """
        self.config = configparser.ConfigParser ()
        try:
            self.config.read (config_file)
        except FileNotFoundError:
            print ("Warning. Configuration file does not exist.")
            cFile.cFile (config_file)
            self.config.read (config_file)

    def connect (self):
        """
        Function to connect to a DB
        Uses self.config for its config values (host, db, user, pass)
        :return true/false
        """
        self.cnx = mysql.create_engine ('mysql://%s:%s@%s/%s' % (self.config['DB']['user'], self.config['DB']['password'], self.config['DB']['host'], self.config['DB']['database']), echo=True)
        return True


