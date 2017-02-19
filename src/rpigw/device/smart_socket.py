# -*- coding: utf-8 -*-

"""
Smart socket
===

An implementation of a my smart socket DPA commands.

:copyright: (c) 2017 Roman Ondráček.
:license: GNU GPLv3, see LICENSE for more details.
"""

from rpigw.device.iqrf_tr import IqrfTrPnum


# class SmartSocketPnum(IqrfTrPnum):
#     SMART_SOCKET = 0x20


class SmartSocket(object):

    def __init__(self, iqrf):
        self.iqrf = iqrf

    def output(self, nadr, hwpid=0xFFFF):
        hwpid1, hwpid2 = divmod(hwpid, 1 << 8)
        # pnum = SmartSocketPnum.SMART_SOCKET
        # packet = bytes([nadr, 0x00, pnum, 0x02, hwpid1, hwpid2])
        pnum = IqrfTrPnum.IO
        packet = bytes([nadr, 0x00, pnum, 0x00, hwpid1, hwpid2, 0x02, 0x04, 0x00, 0x02, 0x0A, 0x00])
        return self.iqrf.send_request(packet)

    def get(self, nadr, hwpid=0xFFFF):
        """
        Get status of smart socket
        @parma nadr Network address
        @param hwpid HW profile ID
        """
        hwpid1, hwpid2 = divmod(hwpid, 1 << 8)
        # pnum = SmartSocketPnum.SMART_SOCKET
        # packet = bytes([nadr, 0x00, pnum, 0x02, hwpid1, hwpid2])
        pnum = IqrfTrPnum.IO
        packet = bytes([nadr, 0x00, pnum, 0x02, hwpid1, hwpid2])
        return self.iqrf.send_request(packet)

    def set(self, nadr, status, hwpid=0xFFFF):
        """
        Set status of smart socket
        @parma nadr Network address
        @param hwpid HW profile ID
        """
        self.output(nadr, hwpid)
        hwpid1, hwpid2 = divmod(hwpid, 1 << 8)
        if status == 0:
            # pnum = SmartSocketPnum.SMART_SOCKET
            # packet = bytes([nadr, 0x00, pnum, status, hwpid1, hwpid2])
            pnum = IqrfTrPnum.IO
            packet = bytes([nadr, 0x00, pnum, 0x01, hwpid1, hwpid2, 0x02, 0x04, 0x00, 0x02, 0x0A, 0x00])
            return self.iqrf.send_request(packet)
        elif status == 1:
            # pnum = SmartSocketPnum.SMART_SOCKET
            # packet = bytes([nadr, 0x00, pnum, status, hwpid1, hwpid2])
            pnum = IqrfTrPnum.IO
            packet = bytes([nadr, 0x00, pnum, 0x01, hwpid1, hwpid2, 0x02, 0x04, 0x04, 0x02, 0x0A, 0x0A])
            return self.iqrf.send_request(packet)
