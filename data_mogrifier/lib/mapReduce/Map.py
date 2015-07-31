__author__ = 'pieter'


class Map:
    """
    Get the input records from STDIN
    For every record, output as semicolon-delimited:
    Geboortejaar;Geboorteplaats;Naam;Voornaam;Source;ID
    We will use Levenshtein later to compare
    The STDIN is a merger of the RAB & Prisoner tables
    """

    def __init__(self, s_input):
        a_input = s_input.split(';')
        s_output = '%s;%s;%s;%s;%s;%s' % (a_input[0], a_input[1], a_input[2], a_input[3], a_input[4], a_input[5])
        self.output = s_output

