import npyscreen
from lib.dbMatch import dbMatch
from lib.aMatch import aMatch
from lib.cFile import cFile
from lib.dbConnect import dbConnect
import sys

dbi = dbConnect ()
dbi.connect ()

"""
Select form
"""


def select_table (*args):
    """
    Select the table
    :param args:
    :return: table_name
    """
    F = npyscreen.Form (name='Select table')
    table = F.add (npyscreen.TitleText, name='Table:')
    F.edit ()
    return table.value


def select_columns (*args):
    """
    Select the columns
    :param args:
    :return: (id_column, selected_columns)
    """
    F = npyscreen.Form (name='Select columns')
    id_column = F.add (npyscreen.TitleSelectOne, name='ID column:', values=columns, max_height=8)
    selected_columns = F.add (npyscreen.TitleMultiSelect, name='Selected columns in view:', values=columns, max_height=8)
    filter_column = F.add (npyscreen.TitleSelectOne, name='Filter column:', values=columns, max_height=8)
    inscr_column = F.add (npyscreen.TitleSelectOne, name='Inscription date column:', values=columns, max_height=8)
    age_column = F.add (npyscreen.TitleSelectOne, name='Age column:', values=columns, max_height=8)
    F.edit ()
    return (id_column.value, selected_columns.value, filter_column.value, inscr_column.value, age_column.value)


def select_compare_columns (*args):
    """
    Select columns to compare
    :param args:
    :return:
    """
    F = npyscreen.Form (name='Select columns to compare for view ' + v)
    # Columns in the view are named include_columns _a or _b, so we use this knowledge here
    columns_compared_against = {}
    mod_inc_columns = [i + "_b" for i in include_columns]
    mod_inc_columns.append ('NONE')
    for c in include_columns:
        columns_compared_against[c + "_a"] = F.add (npyscreen.TitleSelectOne, name='Match ' + c + '_a against:', values=mod_inc_columns, max_height=3)
    F.edit ()
    columns_compared_against = {item[0]:mod_inc_columns[item[1].value[0]] for item in columns_compared_against.items ()}
    return columns_compared_against


def select_match (*args):
    """
    Select a match
    Like this:
    item_matched_against = all columns in view separated by ' '
    possible_matches ordered by score displayed as all columns in view separated by ' ' preceded by score
    :param args:
    :return: matches ID's of the matches
    """
    F = npyscreen.Form (name='Select a match')
    title_text = [str (s) for s in dbi.get_single_item_by_id (r_id, table, columns=include_columns)]
    title_text = " ".join (title_text)
    #[(id, sc), ...]
    options = []
    r_sorted = t_sorted[0:20] # Limit to first 20 items (TODO: config)
    for (f_id, sc, avg) in r_sorted:
        items = [str (s) for s in dbi.get_single_item_by_id (f_id, table, columns=include_columns)]
        options.append (" ".join (items) + "(" + str (round (avg, 2)) + ")")
    options.append ('NONE')
    _matches = F.add (npyscreen.TitleMultiSelect, name='Select a match for ' + title_text + " (ordered by score):", values=options, max_height=8)
    F.edit ()
    results = []
    for r in _matches.value:
        if r >= len (r_sorted):
            # User selected NONE
            return ['NONE']
        else:
            results.append (r_sorted[r][0])
    return results



table = npyscreen.wrapper_basic (select_table)
columns = dbi.selectColumns (table)
s_columns = npyscreen.wrapper_basic (select_columns)
print ("Creating view ... ")
##
# Get the columns we want to include in the view
filter_column = columns[s_columns[2][0]]
include_columns = []
for c in s_columns[1]:
    include_columns.append (columns[c])
id_column = columns[s_columns[0][0]]
# inscr_column.value, age_column.value
inscr_column = columns[s_columns[3][0]]
age_column = columns[s_columns[4][0]]
dbm = dbMatch (table, table + '_match')
dbm.config_start ()
dbm.connect ()
# Prepare matching
# include_columns should always contain id_column (or stuff won't work)
if id_column not in include_columns:
    include_columns.append (id_column)
dbm.matchPepare (filter_column, include_columns, id_column, inscr_column, age_column)
print ("[OK]")
# Execute matching per view
for v in dbm.filterViews.values ():
    print ("Matching view " + v)
    # Ask which columns to compare to each other
    column_tuples = npyscreen.wrapper_basic (select_compare_columns)
    column_tuples = [(item[0], item[1]) for item in column_tuples.items () if item[1] != 'NONE']
    # Get list of IDS
    ids = dbm.suggest_all (v, id_column)
    for id in ids:
        records = dbm.suggest_single (v, column_tuples, (id_column + "_a", id), id_column + "_b", id_column)
        print ("Matching record #" + str (id))
        r_id = id
        sugg = records
        am = aMatch ()
        fields = [f for (f, d) in column_tuples]
        # Check whether it already matched, if so, skip
        if dbm.is_matched (r_id, table):
            continue
        compared = am.matchCompare (sugg, fields)
        t_sorted = dbm.match_single (compared)
        selected_matches = npyscreen.wrapper_basic (select_match)
        # sorted[selected_matches]
        print ("Storing matches ...")
        for s_m in selected_matches:
            print ("#" + str (s_m))
            if s_m == 'NONE':
                dbm.store_match (r_id, s_m, id_column, 'NOT_FOUND')
            else:
                dbm.store_match (r_id, s_m, id_column)
        print ("[OK]")
    #dbm.clean (v)

print ("Finished")