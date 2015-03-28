from dbConnect import dbConnect
import mysql.connector
import time
import sys


class dbMatch (dbConnect):

    def __init__ (self, table_name):
        self.tableName = table_name
        self.filterViews = {} # key = filter_value; value = view_name

    def __createView (self, columns, filter_column):
        """
        Create a view for a certain filter with a given list of columns
        :param columns: list of columns to select
        :param filter: string
        :return:
        """
        query = ("CREATE VIEW %s AS",
                 "SELECT %s FROM %s a, %s b")
        columns = {"a":", ".join (["a.%s as %s_a" % (item, item) for item in columns]),
                   "b":", ".join (["b.%s as %s_a" % (item, item) for item in columns])}
        cursor = self.cnx.cursor ()
        view_name = "%s_%s" % (filter_column, time.time ())
        self.filterViews[filter_column] = view_name
        try:
            cursor.execute (query, (view_name, columns['a'], columns['b'], self.tableName, self.tableName))
        except mysql.connector.Error as err:
            raise Exception (err)
        return True

    def __filter (self, filter_column):
        """
        Get a list of values for the key 'filter_column'
        This list will be used to create the views
        :param filter_column key to filter on
        :return mFilters list of filters (also sets self.mFilters)
        """
        cursor = self.cnx.cursor ()
        query = "SELECT DISTINCT %s as filter FROM %s"
        m_filters = []

        try:
            cursor.execute (query, (filter_column, self.tableName))
        except mysql.connector.Error as err:
            raise Exception (err)

        for (m_filter) in cursor:
            m_filters.append (m_filter)
        cursor.close ()
        self.mFilters = m_filters
        return self.mFilters

    def matchPepare (self, filter_column, columns):
        """"
        Prepare for matching
        :param filter_column column to filter on (selects these from the DB and creates views based on this
        column with a cart.prod of the original table filtered on filter_column)
        :param columns list of columns to include in the cart prod
        """
        #try:
        self.__filter (filter_column)
        #except:
        #    e = sys.exc_info()[0]
        #    print ("Error: %s" % e)
        #    return False
        for mFilter in self.mFilters:
            self.__createView (columns, mFilter)
        #    try:
        #    except:
        #        e = sys.exc_info()[0]
        #        print ("Error: %s" % e)
        #        return False
        return True



