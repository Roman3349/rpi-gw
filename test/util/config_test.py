# -*- coding: utf-8 -*-

"""
Config Test
===

A test of an implementation of configuration.

:copyright: (c) 2017 Roman Ondráček.
:license: GNU GPLv3, see LICENSE for more details.
"""

import unittest

from rpigw.util import config
from collections import OrderedDict

READ_CONFIG = {
  "gsm": {
    "enabled": True,
    "port": "/dev/ttyUSB0",
    "baudRate": 9600,
    "pin": None
  },
  "iqrf": {
    "enabled": True,
    "interface": "spi",
    "interfaces": {
      "spi": {
        "port": "/dev/spidev0.0"
      },
      "uart": {
        "port": "/dev/ttyACM0",
        "baudRate": 9600
      }
    }
  }
}

class ConfigTests(unittest.TestCase):
    """
        Test configuration
    """

    def test_read_success(self):
        """
        [util] Test reading configuration from file
        """
        self.assertEqual(config.Config("./test/config.yml").read(), READ_CONFIG)

    def test_read_fail(self):
        """
        [util] Test reading configuration from non-existing file
        """
        self.assertEqual(config.Config("./test/config0.yml").read(), False)
