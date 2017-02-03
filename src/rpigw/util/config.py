# -*- coding: utf-8 -*-

"""
Config
===

An implementation of configuration.

:copyright: (c) 2017 Roman Ondráček.
:license: GNU GPLv3, see LICENSE for more details.
"""

import yaml


class Config(object):

    def __init__(self, config_file):
        self.config_file = config_file

    def read(self):
        """
        Read configuration from file
        """
        try:
            with open(self.config_file) as yaml_file:
                return yaml.load(yaml_file)
        except IOError:
            return False
