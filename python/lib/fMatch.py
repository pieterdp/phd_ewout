from Levenshtein import *
import re

class fuzzMatch:
    """
    """

    def __init__ (self, string_a, string_b, ALGORITHM = 'Levenshtein'):
        """
        """
        self.strcmp = [string_a, string_b]
        self.a = ALGORITHM

    def fPrepare (self, fString):
        """
        """
        fString.lower ()
        fString = re.sub ('[^a-z]', '', fString)
        return fString

    def fMatch (self):
        """
        Match two string using Levenshtein
        """
        self.strcmp = [self.fPrepare (elem) for elem in self.strcmp]
        self.mFunc = getattr ('fuzzMatch', "match%s" % self.a, self.matchLevenshtein)
        self.simRate = self.mFunc ()
        return self.simRate

    def matchLevenshtein (self):
        """
        """
        mRate = ratio (self.strcmp[0], self.strcmp[1])
        return mRate
