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
    "gsm":{
        "enabled":True,
        "interface":"usb-acm",
        "interfaces":{
            "usb-acm":{
                "port":"/dev/ttyACM0",
                "baud_rate":"9600"
            }
        }
    },
    "iqrf":{
        "enabled":True,
        "interface":"spi",
        "interfaces":{
            "spi":{
                "port":"/dev/spidev0.0"
            },
            "usb-acm":{
                "port":"/dev/ttyACM1",
                "baud_rate":"9600"
            }
        }
    }
}

class ConfigTests(unittest.TestCase):
    """

    """

    def test_read(self):
        """
        Test reading configuration from file
        """
        self.assertEqual(config.Config("./test/config.json").read(), READ_CONFIG)
        self.assertEqual(config.Config("./test/config0.json").read(), False)
