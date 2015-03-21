import configparser
import os


class cFile:
    """
    """

    def __init__(self, config_file):
        self.configFile = config_file
        self.config = configparser.ConfigParser()
        try:
            self.fsock = open(self.configFile, "r")
            self.fsock.close()
        except FileNotFoundError:
            self.create()

    def create(self):
        """
        """
        conf = configparser.ConfigParser()  # Don't want the default interfering
        conf['DEFAULT'] = {
        }
        conf['DB'] = {'host': 'localhost',
                      'user': 'db_user',
                      'password': 'db_pass',
                      'database': 'db'
                      }
        try:
            with open(self.configFile, 'w') as configfile:
                conf.write(configfile)
        except IOError:
            raise Exception('Error: could not create file %s' % self.configFile)
        return True
