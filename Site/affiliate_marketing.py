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
    afl_default = {
        'concerning': '/conversion/afl_default',
        'psychological_types': '/conversion/afl_default',
        'point_and_line': '/conversion/afl_default',
        'gifts_differing': '/conversion/afl_default',
        'understand_1': '/conversion/afl_default',
        'new_art_life': '/conversion/afl_default',
        'understand_spanish': '/conversion/afl_default',
        'understand_2': '/conversion/afl_default',
        'presidents': '/conversion/afl_default',
    }

    afl_none = {
        'concerning': '',
        'psychological_types': '',
        'point_and_line': '',
        'gifts_differing': '',
        'understand_1': '',
        'new_art_life': '',
        'understand_spanish': '',
        'understand_2': '',
        'presidents': '',
    }

    #
    # Active Link Dictionaries:
    #
    afl_button = {}

    def __init__(self):

        """
        Assign source links to active links
        """

        self.afl_button['concerning'] = self.afl_default['concerning']
        self.afl_button['psychological_types'] = self.afl_default['psychological_types']
        self.afl_button['point_and_line'] = self.afl_default['point_and_line']
        self.afl_button['gifts_differing'] = self.afl_default['gifts_differing']
        self.afl_button['understand_1'] = self.afl_default['understand_1']
        self.afl_button['new_art_life'] = self.afl_default['new_art_life']
        self.afl_button['understand_spanish'] = self.afl_default['understand_spanish']
        self.afl_button['understand_2'] = self.afl_default['understand_2']
        self.afl_button['presidents'] = self.afl_default['presidents']
