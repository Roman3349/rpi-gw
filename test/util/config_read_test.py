import unittest
import math

from rpigw.util import config

READ_CONFIG = {"gsm":{"enabled":True,"interface":"usb-acm","interfaces":{"usb-acm":{"port":"/dev/ttyACM0","baud_rate":"9600"}}},"iqrf":{"enabled":True,"interface":"spi","interfaces":{"spi":{"port":"/dev/spidev0.0"},"usb-acm":{"port":"/dev/ttyACM1","baud_rate":"9600"}}}}

class ConfigTests(unittest.TestCase):

    def test_read(self):
        self.assertEqual(config.Config("./test/config.json").read(), READ_CONFIG)
        self.assertEqual(config.Config("./test/config0.json").read(), False)
