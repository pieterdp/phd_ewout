import class_dbConnect

class dbMatch (dbConnect):

	def __init__ (self, table_name, config_file = 'etc/settings.conf'):
		dbConnect.__init__ (config_file)
		self.tableName = table_name
		self.filterViews = {} # key = filter_value; value = view_name

	def __createView (self, columns):
		query = ("CREATE VIEW AS",
				 "SELECT %s FROM %s a, %s b")
		#columns = []

	
	def __filter (self, filter_column):
		cursor = self.cnx.cursor ()
		query = "SELECT DISTINCT %s as mFilter FROM %s"
		mFilters = []
		
		try:
			cursor.execute (query, (filter_column, self.tableName))
		except mysql.connector.Error as err:
			raise Exception (err)
			return False
		
		for (mFilter) in cursor:
			mFilters.append (mFilter)
		cursor.close ()
		self.mFilters = mFilters
		
		return self.mFilters
	
	def matchPepare (self, filter_column):
		
