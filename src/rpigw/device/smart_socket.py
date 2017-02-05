# -*- coding: utf-8 -*-

"""
Smart socket
===

An implementation of a my smart socket DPA commands.

:copyright: (c) 2017 Roman Ondráček.
:license: GNU GPLv3, see LICENSE for more details.
"""

from rpigw.device.iqrf_tr import IqrfTrPnum


class SmartSocketPnum(IqrfTrPnum):
    SMART_SOCKET = 0x20


class SmartSocket(object):

    def __init__(self, iqrf):
        self.iqrf = iqrf

    def get(self, nadr, hwpid=0xCDEF):
        """
        Get status of smart socket
        @parma nadr Network address
        @param hwpid HW profile ID
        """
        hwpid1, hwpid2 = divmod(hwpid, 1 << 8)
        pnum = SmartSocketPnum.SMART_SOCKET
        packet = bytes(nadr, pnum, 0x02, hwpid1, hwpid2)
        return self.iqrf.send_request(packet)

    def set(self, nadr, status, hwpid=0xCDEF):
        """
        Set status of smart socket
        @parma nadr Network address
        @param hwpid HW profile ID
        """
        hwpid1, hwpid2 = divmod(hwpid, 1 << 8)
        if status == 0 or status == 1:
            pnum = SmartSocketPnum.SMART_SOCKET
            packet = bytes(nadr, pnum, status, hwpid1, hwpid2)
            return self.iqrf.send_request(packet)
