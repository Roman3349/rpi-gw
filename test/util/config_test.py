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

READ_CONFIG = {
  "app": {
    "enable-sms-feedback": True
  },
  "gsm": {
    "enabled": True,
    "interface": "uart",
    "interfaces": {
      "uart": {
        "port": "/dev/ttyUSB0",
        "baudRate": 9600
      }
    },
    "pin": False
  },
  "iqrf": {
    "enabled": True,
    "interface": "spi",
    "interfaces": {
      "spi": {
        "port": "/dev/spidev0.0"
      },
      "cdc": {
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
        cfg_file = './test/config.yml'
        self.assertEqual(config.Config(cfg_file).read(), READ_CONFIG)

    def test_read_fail(self):
        """
        [util] Test reading configuration from non-existing file
        """
        cfg_file = './test/config0.yml'
        self.assertEqual(config.Config(cfg_file).read(), False)
