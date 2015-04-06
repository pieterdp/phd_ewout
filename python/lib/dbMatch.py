from dbConnect import dbConnect
from fMatch import fuzzMatch
import sqlalchemy as mysql
from sqlalchemy.sql import select, column, update, literal_column
import time
import sys


class dbMatch (dbConnect):

    def __init__ (self, table_name, match_name):
        self.tableName = table_name
        self.filterViews = {} # key = filter_value; value = view_name
        self.table = mysql.Table (self.tableName, mysql.MetaData ())
        self.matches = {} # key = view_name; value = matches (see self.match ())
        self.matchName = match_name
        self.match = mysql.Table (self.matchName, mysql.MetaData ()) # Create

    def __createView (self, columns, filter_column, where_column, id_column):
        """
        Create a view for a certain filter with a given list of columns
        :param columns: list of columns to select
        :param filter: string
        :return:
        """
        view_name = "%s_%s" % (filter_column, int(time.time ()))
        self.filterViews[filter_column] = view_name
        #columns = columns.split (',')
        query = "CREATE VIEW `%s` AS SELECT a.%s as ID, %s, %s FROM `%s` a, `%s` b WHERE a.%s = '%s' AND b.%s = '%s' AND a.%s <> b.%s AND a.matched = 'NO'" %\
                                                                                            (view_name, id_column, ", ".join (["a.%s as %s_a" % (item, item) for item in columns]),
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

    def suggest_single (self, view_name, filter_columns, id_column, id_matcher, id_original):
        """
        Suggest a match between two items in the view based on their Levenshtein distance using fMatch Works on items identified by one unique identifier
        :param view_name name of the view to work on
        :param filter_columns list of tuples containing columns to be matched: filter_columns[i] = (c_a, c_b)
        :param id_column tuple of the column_name and its value of the identifier
        :param id_matcher column name of the unique identifier of the item matched against in the cart prod
        :param id_original column name of the unique identifier in the original table
        :return list of possible matches: matches[id] = {c_x:[(c_z, 2%)}
        """
        # View
        """
        s = select([table1.c.a]).\
    select_from(
        table1.join(table2, table1.c.a==table2.c.b)
    )"""
        view = mysql.Table (view_name, mysql.MetaData ())
        ## WHERE view.id = foo AND view.id = or.id AND or.match = NO
        j = view.join (self.table, literal_column (self.tableName + "." + id_original) == literal_column (view_name + "." + id_column[0]))
        s = select (['*'], from_obj=[view, self.table]).where (literal_column (view_name + "." + id_column[0]) == id_column[1]).where (literal_column (self.tableName + "." + 'matched') == 'NO').select_from (j)
        #s = select (['*'], from_obj=[view, or_table]).where (view.c[id_column[0]] == id_column[1]).where (view.c[id_column[0]] == or_table.c[id_matcher]).where (or_table.c['matched'] == 'NO')  # Where clause must be added for matched=NO
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
        sugg_00 = [] # Highest match with s < 0.5 (only filled if above are empty)
        sugg = []
        for match in matches['agg']:
            if match[2] >= 0.5:
                sugg_05.append (match)
        if not sugg_05:
            max_sc = 0 # Maximum score found
            max_item = [] # Item with the highest score
            for match in matches['agg']:
                if match[2] > max_sc or max_sc == 0:
                    max_item = [match]
                elif match[2] == max_sc and max_sc != 0:
                    max_item.append (match)
            sugg_00 = max_item
            sugg = sugg_00
        elif sugg_05:
            scores = []
            items = []
            for match in sugg_05:
                scores.append (match[2])
            scores.sort (reverse=True)
            for score in scores:
                for match in sugg_05:
                    if match[2] == score:
                        items.append (match)
            sugg = items
        # Remove duplicate ID's
        ids = []
        result = []
        for item in sugg:
            if item[0] in ids:
                continue
            else:
                ids.append (item[0])
                result.append (item)
        return result

    def store_match (self, id_matched, id_match, id_original, status='YES'):
        """
        Store a match between two items in the match table
        :param id_matched: id of the item matched against
        :param id_match: id of the match
        :param id_original: name of the unique identifier in the original table
        :return:
        """
        # Update self.tableName
        for id in [id_matched, id_match]:
            u = "UPDATE %s t SET t.matched = '%s' WHERE t.%s = '%s'" % (self.tableName, status, id_original, id)
                #update (self.table).where (literal_column (self.tableName + "." + "ID") == id).values ({literal_column (self.tableName + "." + "matched"):'YES'})
            self.cnx.execute (u)
        # Insert into self.match (id_matched, id_match)
        if status == 'YES':
            i = "INSERT INTO %s (id_matched, id_match) VALUES ('%s', '%s')" % (self.matchName, id_matched, id_match)
            self.cnx.execute (i)
        return True

    def clean (self, view_name):
        view = mysql.Table (view_name, mysql.MetaData ())
        view.drop ()
        return True

    def suggest_all (self, view_name, id_column):
        """
        Return a list of IDS in a view
        """
        #('ID_a', 2049)
        view = mysql.Table (view_name, mysql.MetaData ())
        # Select all id's to work on
        s = select ([id_column], distinct=True, from_obj=view)
        ids = self.cnx.execute (s)
        ids = ids.fetchall ()
        return [id[0] for id in ids]

    def is_matched (self, id, table):
        """
        Item is matched?
        :param id:
        :param table:
        :return:
        """
        table = mysql.Table (table, mysql.MetaData ())
        s = select (['matched'], from_obj=table).where (literal_column ('ID') == id)
        result = self.cnx.execute (s)
        r = result.fetchone ()
        if r[0] == 'NO':
            return False
        else:
            return True



