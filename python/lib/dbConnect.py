import mysql.connector
import configparser
import cFile


class dbConnect:
    """
    Functions to connect to the DB
    """
    def __init__ (self, config_file = 'etc/settings.conf'):
        """
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
        @return true/false
        """
        try:
            self.cnx = mysql.connector.connect (user=self.config['DB']['user'],
                                                password=self.config['DB']['password'],
                                                host=self.config['DB']['host'],
                                                database=self.config['DB']['database'])
        except mysql.connector.Error as err:
            raise Exception (err)
        return True

    def disconnect (self):
        """
        Function to disconnect from the DB
        @return true/false
        """
        try:
            self.cnx.close ()
        except mysql.connector.Error as err:
            raise Exception (err)
        return True


