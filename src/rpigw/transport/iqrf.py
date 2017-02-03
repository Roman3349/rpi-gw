# -*- coding: utf-8 -*-

"""
IQRF
===

An implementation of a IQRF networking.

:copyright: (c) 2017 Roman Ondráček.
:license: GNU GPLv3, see LICENSE for more details.
"""

from iqrf.transport import cdc
from iqrf.transport import spi


class Iqrf(object):

    def __init__(self, config):
        self.enabled = config['iqrf']['enabled']
        self.interface = config['iqrf']['interface']
        self.port = config['iqrf']['interfaces'][self.interface]['port']
        self.device = None

        try:
            if self.interface == 'cdc':
                self.device = cdc.open(self.port)
            elif self.interface == 'spi':
                self.device = spi.open(self.port)
            else:
                raise Exception()
        except Exception as error:
            print("An error occured:", type(error), error)

    def send_request(self, packet):
        if self.interface == 'cdc':
            self.device.send(cdc.DataSendRequest(packet))
        elif self.interface == 'spi':
            self.device.send(spi.DataSendRequest(packet), timeout=5)
        confirmation = self.device.receive(timeout=5).data
        response = self.device.receive(timeout=5).data
        return {"confirmation": confirmation, "response": response}
