from dbConnect import dbConnect
from fMatch import fuzzMatch
import sqlalchemy as mysql
from sqlalchemy.sql import select, column
import time


class dbMatch (dbConnect):

    def __init__ (self, table_name):
        self.tableName = table_name
        self.filterViews = {} # key = filter_value; value = view_name
        self.table = mysql.Table (self.tableName, mysql.MetaData ())
        self.matches = {} # key = view_name; value = matches (see self.match ())

    def __createView (self, columns, filter_column):
        """
        Create a view for a certain filter with a given list of columns
        :param columns: list of columns to select
        :param filter: string
        :return:
        """
        view_name = "%s_%s" % (filter_column, time.time ())
        self.filterViews[filter_column] = view_name
        columns = columns.split (',')
        query = "CREATE VIEW `%s` AS SELECT %s, %s FROM `%s` a, `%s` b" % (view_name, ", ".join (["a.%s as %s_a" % (item, item) for item in columns]), ", ".join (["b.%s as %s_b" % (item, item) for item in columns]), self.tableName, self.tableName)
        self.cnx.execute (query)
        return True

    def __filter (self, filter_column):
        """
        Get a list of values for the key 'filter_column'
        This list will be used to create the views
        :param filter_column key to filter on
        :return mFilters list of filters (also sets self.mFilters)
        """
        m_filters = []
        result = self.cnx.execute (select ([filter_column], distinct=True, from_obj=self.table))
        rows = result.fetchall ()
        for row in rows:
            m_filters.append (row[filter_column])
        self.mFilters = m_filters
        return self.mFilters

    def matchPepare (self, filter_column, columns):
        """"
        Prepare for matching
        :param filter_column column to filter on (selects these from the DB and creates views based on this
        column with a cart.prod of the original table filtered on filter_column)
        :param columns list of columns to include in the cart prod
        """
        self.__filter (filter_column)
        for mFilter in self.mFilters:
            self.__createView (columns, mFilter)
        return True

    def suggest_single (self, view_name, filter_columns, id_column, id_matcher):
        """
        Suggest a match between two items in the view based on their Levenshtein distance using fMatch Works on items identified by one unique identifier
        :param view_name name of the view to work on
        :param filter_columns list of tuples containing columns to be matched: filter_columns[i] = (c_a, c_b)
        :param id_column tuple of the column_name and its value of the identifier
        :param id_matcher column name of the unique identifier of the item matched against in the cart prod
        :return list of possible matches, ordered by score: matches[id] = [{c_x:[(c_z, 2%)}]
        """
        # View
        view = mysql.Table (view_name, mysql.MetaData ())
        s = select (['*'], from_obj=view).where (column (id_column[0]) == id_column[1])
        result = self.cnx.execute (s)
        rows = result.fetchall ()
        # We now have a list of all items in the cart prod against one item (identified by one id)
        # Now, iterate through them, adding their ID to an array
        sugg = {}
        for row in rows:
            # Every match is in its own dict with the column name as key, with as value a tuple with the column against it matched, with its score
            sugg[row[id_matcher]] = {}
            for (field_a, field_b) in filter_columns:
                # Now match them using fmatch
                m = fuzzMatch (row[field_a], row[field_b])
                sugg[row[id_matcher]][field_a] = (field_b, m.fMatch ())
        return sugg







