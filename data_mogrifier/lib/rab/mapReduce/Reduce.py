__author__ = 'pieter'
import sys
from Levenshtein import *
from re import sub


class Reduce:
    """
    Get all names from STDIN
    For every line; compare with previous line
    If L > 0.5 add to an array
    If L < 0.5, perform matching on array; create new array
    """

    def __init__(self):
        previous = ''
        self.list = []
        for line in sys.stdin:
            if self.s_ratio(line, previous) > 0.5:
                self.list.append(line)
            else:
                # Do stuff
                self.list = [line]
            previous = line

    def s_prepare(self, string):
        """
        Make lowercase and remove all non-alphanumeric characters
        """
        string.lower()
        return sub('[^a-z0-9]', '', string)

    def s_ratio(self, line, previous):
        a_line = line.split(';')
        a_prev = previous.split(';')
        s_line = '%s;%s;%s;%s' % a_line
        s_prev = '%s;%s;%s;%s' % a_prev
