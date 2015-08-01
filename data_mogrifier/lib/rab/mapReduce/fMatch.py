from Levenshtein import ratio
import re


class FuzzMatch:
    """
    """

    def __init__(self, string_a, string_b, algorithm='Levenshtein'):
        """
        """
        self.strcmp = [string_a, string_b]
        self.a = algorithm

    def prepare(self, string):
        """
        """
        string.lower()
        return re.sub('[^a-z]', '', string)

    def f_match(self):
        """
        Match two string using Levenshtein
        """
        self.strcmp = [self.prepare(elem) for elem in self.strcmp]
        m_func = getattr('FuzzMatch', "match_%s" % self.a, self.match_Levenshtein)
        return m_func()

    def match_Levenshtein(self):
        """
        """
        return ratio(self.strcmp[0], self.strcmp[1])
