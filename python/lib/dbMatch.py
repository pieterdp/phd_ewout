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

    def __createView (self, columns, filter_column, where_column, id_column):
        """
        Create a view for a certain filter with a given list of columns
        :param columns: list of columns to select
        :param filter: string
        :return:
        """
        view_name = "%s_%s" % (filter_column, time.time ())
        self.filterViews[filter_column] = view_name
        columns = columns.split (',')
        query = "CREATE VIEW `%s` AS SELECT %s, %s FROM `%s` a, `%s` b WHERE a.%s = '%s' AND b.%s = '%s' AND a.%s <> b.%s" % (view_name, ", ".join (["a.%s as %s_a" % (item, item) for item in columns]),
                                                                                             ", ".join (["b.%s as %s_b" % (item, item) for item in columns]),
                                                                                             self.tableName, self.tableName, where_column, filter_column, where_column, filter_column,
                                                                                             id_column, id_column)
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

    def matchPepare (self, filter_column, columns, id_column):
        """"
        Prepare for matching
        :param filter_column column to filter on (selects these from the DB and creates views based on this
        column with a cart.prod of the original table filtered on filter_column)
        :param columns list of columns to include in the cart prod
        """
        self.__filter (filter_column)
        for mFilter in self.mFilters:
            self.__createView (columns, mFilter, filter_column, id_column)
        return True

    def suggest_single (self, view_name, filter_columns, id_column, id_matcher):
        """
        Suggest a match between two items in the view based on their Levenshtein distance using fMatch Works on items identified by one unique identifier
        :param view_name name of the view to work on
        :param filter_columns list of tuples containing columns to be matched: filter_columns[i] = (c_a, c_b)
        :param id_column tuple of the column_name and its value of the identifier
        :param id_matcher column name of the unique identifier of the item matched against in the cart prod
        :return list of possible matches: matches[id] = {c_x:[(c_z, 2%)}
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

    def match_single (self, matches):
        """
        Does one of the following:
            if it finds >=1 match with a score of 1, it only suggests those (1 = equal)
            if it finds a match with a score of >=0.5, it suggests those
            if it only finds matches <=0.5, it suggests the one with the highest score
        :param matches: (return of aMatch)
        :return: matches = [(id, sc), ...]
        """
        sugg_05 = [] # Matches with s >= 0.5
        sugg_1 = [] # Matches with s = 1
        sugg_00 = [] # Highest match with s < 0.5 (only filled if above are empty)
        for match in matches['agg']:
            if match[1] == 1:
                sugg_1.append (match)
            elif match[1] >= 0.5:
                sugg_05.append (match)
        if not sugg_1 and not sugg_05:
            max_sc = 0 # Maximum score found
            max_item = [] # Item with the highest score
            for match in matches['agg']:
                if match[1] > max_sc or max_sc == 0:
                    max_item = [match]
                elif match[1] == max_sc and max_sc != 0:
                    max_item.append (match)
            sugg_00 = max_item
            return sugg_00
        elif sugg_1:
            return sugg_1
        elif sugg_05 and not sugg_1:
            scores = []
            items = []
            for match in sugg_05:
                scores.append (match[1])
            scores.sort (reverse=True)
            for score in scores:
                for match in sugg_05:
                    if match[1] == score:
                        items.append (match)
            return items

    def store_match (self, id_matched, id_match):
        pass

    def clean (self):
        pass









