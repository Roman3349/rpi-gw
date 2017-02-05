# -*- coding: utf-8 -*-

"""
IQRF TR
===

An implementation of a IQRF TR DPA commans.

:copyright: (c) 2017 Roman Ondráček.
:license: GNU GPLv3, see LICENSE for more details.
"""

from enum import Enum


class IqrfTrPnum(Enum):
    COORDINATOR = 0x00
    NODE = 0x01
    OS = 0x02
    EEPROM = 0x03
    EEEPROM = 0x04
    RAM = 0x05
    LEDR = 0x06
    LEDG = 0x07
    SPI = 0x08
    IO = 0x09
    Thermometer = 0x0A
    PWM = 0x0B
    UART = 0x0C
    FRC = 0x0D


class IqrfTr(object):

    def __init__(self, iqrf):
        self.iqrf = iqrf

    def pulse_led(self, nadr, pnum, hwpid):
        """
        Pulse a LED on TR module
        @parma nadr Network address
        @param pnum Peripherhal number
        @param hwpid HW profile ID
        """
        hwpid1, hwpid2 = divmod(hwpid, 1 << 8)
        if pnum == IqrfTrPnum.LEDG or pnum == IqrfTrPnum.LEDR:
            packet = bytes(nadr, pnum, 0x03, hwpid1, hwpid2)
            return self.iqrf.send_request(packet)
