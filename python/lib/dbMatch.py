import dbConnect
import time


class dbMatch (dbConnect):

    def __init__ (self, table_name, config_file = 'etc/settings.conf'):
        dbConnect.__init__ (config_file)
        self.tableName = table_name
        self.filterViews = {} # key = filter_value; value = view_name

    def __createView (self, columns, filter):
        query = ("CREATE VIEW %s AS",
                 "SELECT %s FROM %s a, %s b")
        columns = {"a":", ".join (["a.%s as %s_a" % (item, item) for item in columns]),
                   "b":", ".join (["b.%s as %s_a" % (item, item) for item in columns])}
        cursor = self.cnx.cursor ()
        view_name = "%s_%s" % (filter, time.time ())
        self.filterViews[filter] = view_name
        cursor.execute (query, (view_name, columns['a'], columns['b'], self.tableName, self.tableName))


    def __filter (self, filter_column):
        cursor = self.cnx.cursor ()
        query = "SELECT DISTINCT %s as mFilter FROM %s"
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

    def matchPepare (self, filter_column):
        pass
