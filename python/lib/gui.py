from lib.dbMatch import dbMatch
from lib.aMatch import aMatch
from lib.cFile import cFile
from lib.dbConnect import dbConnect
import npyscreen


class guiPre (npyscreen.ActionForm):
    def create (self):
        self.parentApp.tablename = self.add (npyscreen.TitleText, name='Tabel:')
        pass

    def beforeEditing (self):
        pass

    def on_ok (self):
        pass

    def on_cancel (self):
        pass

    def afterEditing (self):
        self.parentApp.setNextForm ('SELECT_TABLE')

class guiSelect (npyscreen.ActionForm):
    def create (self):
        pass

    def beforeEditing (self):

        self.columns = self.parentApp.dbi.selectColumns (self.parentApp.tablename)

    def afterEditing (self):
        self.parentApp.setNextForm ('MAIN')


class gui (npyscreen.NSAppManaged):
    def onStart (self):
        self.tablename = ''
        self.dbi = dbConnect ()
        self.addForm ("PRE", guiPre)
        self.addForm ("SELECT_TABLE", guiSelect)
        self.addForm ("MAIN")