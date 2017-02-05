# -*- coding: utf-8 -*-

"""
IQRF TR
===

An implementation of a IQRF TR DPA commans.

:copyright: (c) 2017 Roman Ondráček.
:license: GNU GPLv3, see LICENSE for more details.
"""

from enum import IntEnum


class IqrfTrPnum(IntEnum):
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

    def led_on(self, nadr, pnum, hwpid=0xFFFF):
        """
        Turn on a LED on TR module
        @parma nadr Network address
        @param pnum Peripherhal number
        @param hwpid HW profile ID
        """
        hwpid1, hwpid2 = divmod(hwpid, 1 << 8)
        if pnum == IqrfTrPnum.LEDG or pnum == IqrfTrPnum.LEDR:
            packet = bytes([nadr, 0x00, pnum, 0x01, hwpid1, hwpid2])
            return self.iqrf.send_request(packet)

    def led_off(self, nadr, pnum, hwpid=0xFFFF):
        """
        Turn on a LED on TR module
        @parma nadr Network address
        @param pnum Peripherhal number
        @param hwpid HW profile ID
        """
        hwpid1, hwpid2 = divmod(hwpid, 1 << 8)
        if pnum == IqrfTrPnum.LEDG or pnum == IqrfTrPnum.LEDR:
            packet = bytes([nadr, 0x00, pnum, 0x00, hwpid1, hwpid2])
            return self.iqrf.send_request(packet)

    def led_pulse(self, nadr, pnum, hwpid=0xFFFF):
        """
        Pulse a LED on TR module
        @parma nadr Network address
        @param pnum Peripherhal number
        @param hwpid HW profile ID
        """
        hwpid1, hwpid2 = divmod(hwpid, 1 << 8)
        if pnum == IqrfTrPnum.LEDG or pnum == IqrfTrPnum.LEDR:
            packet = bytes([nadr, 0x00, pnum, 0x03, hwpid1, hwpid2])
            return self.iqrf.send_request(packet)
