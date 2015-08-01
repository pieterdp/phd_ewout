__author__ = 'pieter'
from os.path import isfile
from .fMatch import FuzzMatch


class Map:
    """
    Get the input records from STDIN
    Every record is of the form:
    item.Geboorteplaats;item.Geboortedatum;item.Naam;item.Voornaam|item.src_table;item.src_id
    We will use Levenshtein later to compare
    The STDIN is a merger of the RAB & Prisoner tables
    """

    def __init__(self, infile):
        self.ordered = []
        self.min_rate = 0.5
        if not isfile(infile):
            raise Exception('Error: file %s does not exist!' % infile)
        f = open(infile, mode='r')
        for line in f:
            try:
                parts = self.component_parts(line)
            except KeyError:
                # This line is invalid, skip it
                continue
            # We ignore Voornaam, cause that will vary wildly
            self.layer_bucket(parts, 0, control_offset=3)

    def layer_bucket(self, bucket, offset, control_offset):
        """
        Walk through a bucket layer by layer; compare the elements at offset in layer
        If we get a new bucket of related items; perform this function again till layer[offset] = KeyError
        If so, add the bucket that is layer[offset - 1] to self.ordered and return True, ending this run
        :param bucket:
        :param offset:
        :return:
        """
        last = []
        part = []
        for layer in bucket:
            ##
            # If last is an empty array, then part should contain the layer and we continue with a new run
            try:
                s = last[offset]
            except KeyError:
                part = [layer]
                last = layer
                continue
            ##
            # If the distance between the compared items is higher than min_rate; add them to the part-list
            # If not, check whether in the layer we can compare items beyond our current offset (recursion)
            # If not, add the part we were working on to self.ordered, as this is the rightmost element we can compare
            # and continue with a new run
            # If it is, recurse using this function with an offset + 1
            # If nothing more to try, return True
            if self.match_two(layer[offset], last[offset]):
                part = self.stash(layer, part)
            else:
                if (offset + 1) >= control_offset:
                    # The items after control_offset must not be checked, so this run exits as well
                    self.ordered.append(part)
                else:
                    try:
                        s = layer[offset + 1]
                        self.layer_bucket(part, offset + 1, control_offset=control_offset)
                    except KeyError:
                        # No more items to try, finished
                        self.ordered.append(part)
                part = [layer]
            last = layer
        return True

    def component_parts(self, line):
        """
        Split a line in its component parts: split on |, then on ;
        :param line:
        :return list:
        """
        parts = line.split('|')
        if len(parts) < 2:
            raise KeyError('Error: not enough parts!')
        output = []
        for part in parts:
            a = part.split(';')
            output = output + a
        return output

    def stash(self, item, bucket):
        """
        Stash (add) an item to a bucket
        :param item:
        :param bucket:
        :return:
        """
        bucket.append(item)
        return bucket

    def match_two(self, first, second, min_rate=None):
        """
        Match two strings (first, second).
        If L-score is above min_rate (self.min_rate as default), return True; else False
        :param first:
        :param second:
        :param min_rate:
        :return:
        """
        if min_rate is None:
            min_rate = self.min_rate
        first = str(first)
        second = str(second)
        f = FuzzMatch(first, second)
        if f >= min_rate:
            return True
        else:
            return False
