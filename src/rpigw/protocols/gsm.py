# -*- coding: utf-8 -*-

"""
GSM
===

An implementation of GSM communication.

:copyright: (c) 2017 Roman Ondráček.
:license: GNU GPLv3, see LICENSE for more details.
"""

from ..util.config import Config
import gammu

class Gsm(object):

    def __init__(self, config):
        self.enabled = config['gsm']['enabled']
        if self.enabled:
            self.state_machine = gammu.StateMachine()
            self.state_machine.ReadConfig()
            self.state_machine.Init()
            self.state_machine.SetIncomingCallback(smsCallback)
            try:
                self.state_machine.SetIncomingSMS()
            except gammu.ERR_NOTSUPPORTED:
                print('Your phone does not support incoming SMS notifications!')

    def smsCallback(self, state_machine, callback_type, data):
        print('Received incoming event type: ' + callback_type)
        if ('Number' not in data):
            data = state_machine.GetSMS(data['Folder'], data['Location'])[0]
        print(data)
