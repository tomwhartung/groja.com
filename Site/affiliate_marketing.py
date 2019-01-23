""" Module to manage affiliate marketing links

Purpose: allow managing affiliate marketing links in one place
Author: Tom W. Hartung
Date: Winter, 2019
Copyright: (c) 2019 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:

"""


class AffiliateLinks:

    """
    Use python dictionaries to make it easier to update affiliate links
    """

    #
    # Source Link Dictionaries:
    #
    afl_none = {
        'concerning': '',
        'psychological_types': '',
        'point_and_line': '',
        'gifts_differing': '',
    }

    #
    # Active Link Dictionaries:
    #
    afl_button = {}

    def __init__(self):

        """
        Assign source links to active links
        """

        self.afl_button['concerning'] = afl_none['concerning']
        self.afl_button['psychological_types'] = afl_none['psychological_types']
        self.afl_button['point_and_line'] = afl_none['point_and_line']
        self.afl_button['gifts_differing'] = afl_none['gifts_differing']


