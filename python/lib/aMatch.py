
class aMatch:
    """
    Class for the matching algorithm
    """

    def __init__ (self):
        pass

    def matchCompare (self, matches, fields):
        """
        Function to compare two matches based on their score
        :param matches[id] = {c_x:[(c_z, 2%)} (id is the id of the item matched against)
        :param fields: the list of column names "c_x"
        :return matched_compared = {agg:[(id, score, avg), ...], field_x:[(pos, id, score), ...], ...}
        """
        result_set = {}
        result = {'agg': []}
        for field in fields:
            scores = []
            for (i, c) in matches.items ():
                # List of scores per field
                scores.append (c[field][1])
            # Sort
            scores.sort (reverse=True)
            # Add to result_set
            result_set[field] = scores
        # Now we have a dict with as keys the field_names and as value a sorted list of scores
        # now get the ID's which correspond to those scores (TODO improve)
        for field in result_set.keys ():
            result[field] = []
            for s in result_set[field]:
                for (i, c) in matches.items ():
                    if c[field][1] == s:
                        result[field].append ((i, s))
        # Get the aggregated values
        t_agg = []
        t_score = []
        for i in matches.keys ():
            sc = 0
            am = 0 # To compute the average: total
            for field in result_set.keys ():
                for (n, s) in result[field]:
                    if n == i:
                        sc = sc + s
                        am = am + 1
            t_agg.append ((i, sc, sc/am))
            t_score.append (sc)
        # Order the aggregated values
        t_score.sort (reverse=True)
        ids = []
        for s in t_score:
            for (i, sc, av) in t_agg:
                if s == sc:
                    if i in ids:
                        continue
                    else:
                        result['agg'].append ((i, sc, av))
                        ids.append (i)
        return result



    def __sort (self, _dict):
        """
        return the following:
        result = {agg:[(pos, id, score), ...], field_x:[(pos, id, score), ...], ...}
        :param _dict:
        :return:
        """
        pass