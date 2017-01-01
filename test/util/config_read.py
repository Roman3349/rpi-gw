import unittest
from rpigw.util import config

READ_CONFIG = {"gsm": {"port": "/dev/ttyACM0","baud_rate": "9600"}}

class ConfigTests(unittest.TestCase):

	def test_read(self):
		conf = config.Config("./test/util/config_read.json")
		self.assertEqual(conf.read(), READ_CONFIG)

