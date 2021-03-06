import sqlalchemy as mysql
from sqlalchemy.sql import select, column, literal_column
import configparser
import cFile
import sys


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
        self.cnx = mysql.create_engine ('mysql://%s:%s@%s/%s' % (self.config['DB']['user'], self.config['DB']['password'], self.config['DB']['host'], self.config['DB']['database']))
        return True

    def get_single_item_by_id (self, id, table, columns=["*"]):
        """
        Get a single item by its ID
        :param id: id
        :param table: name of the table
        :return: dict item
        """
        table = mysql.Table (table, mysql.MetaData ())
        s = select (columns, from_obj=table).where (literal_column ('ID') == id)
        result = self.cnx.execute (s)
        return result.fetchone ()

    def selectColumns (self, table_name):
        """
        Function to select all columns in a given table
        :param table_name: name of the table
        :return: list columns
        """
        columns = []
        result = self.cnx.execute ("SHOW COLUMNS FROM %s" % table_name)
        for row in result:
            columns.append (row[0])
        return columns



