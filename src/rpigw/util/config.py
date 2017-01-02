# -*- coding: utf-8 -*-

"""
Config
===

An implementation of configuration.

:copyright: (c) 2017 Roman Ondráček.
:license: GNU GPLv3, see LICENSE for more details.
"""


import json

class Config(object):

    def __init__(self, config_file):
        self.config_file = config_file

    def read(self):
        """
        Read configuration from file
        """
        try:
            with open(self.config_file) as json_data:
                return json.load(json_data)
        except IOError:
            return False
