import sys
import threading
import argparse
import logging

from rpigw.util.config import Config
from rpigw.transport.gsm import Gsm
from rpigw.transport.iqrf import Iqrf
from rpigw.device.iqrf_tr import IqrfTr, IqrfTrPnum
from rpigw.device.smart_socket import SmartSocket
from systemd.journal import JournalHandler


def main():
    parser = argparse.ArgumentParser(usage='usage: %(prog)s [options]')
    parser.add_argument('-c', '--config', action='store', type=str,
                        dest='config', default='/etc/rpigw/config.yml',
                        help='Config file path')
    args = parser.parse_args()
    log = logging.getLogger('rpigw')
    log.addHandler(JournalHandler())
    log.setLevel(logging.DEBUG)
    log.info('Starting rpigw...')
    config = Config(args.config).read()
    gsm = Gsm(config)
    iqrf = Iqrf(config)
    sms = gsm.read_sms('ALL')
    log.info('Deleting an old text messages...')
    if config['app']['enable-sms-feedback']:
        log.info('A text message feedback is enabled.')
    else:
        log.info('A text message feedback is disabled.')
    for i in sms:
        if i:
            gsm.delete_sms(i['id'])
    try:
        read_sms(gsm, iqrf, config, log)
    except Exception as error:
        log.error('An error occured:', type(error), error)
    return 0


def read_sms(gsm, iqrf, config, log):
    iqrf_tr = IqrfTr(iqrf)
    smart_socket = SmartSocket(iqrf)
    sms = gsm.read_sms('REC UNREAD')
    for i in sms:
        content = i['content']
        array = content.split()
        if len(array) is 2:
            device = array[0].lower()
            address = int(array[1])
            if device == 'thermometer' or device == 'teplomer':
                response = iqrf_tr.thermometer_read(address)
                temperature = iqrf_tr.thermometer_decode(response)
                log.debug('[THERMOMETER]: ')
                log.debug(response)
                if sms_feedback:
                    content = 'Teplota: ' + str(temperature['float']) + '*C'
                    gsm.send_sms(i['number'], content)
        elif len(array) is 3:
            device = array[0].lower()
            address = int(array[1])
            command = array[2].lower()
            if device == 'ledg':
                if command == 'on' or command == 'zapnout':
                    response = iqrf_tr.led_on(address, IqrfTrPnum.LEDG)
                    log.debug('[LEDG](ON): ')
                    log.debug(response)
                elif command == 'off' or command == 'vypnout':
                    response = iqrf_tr.led_off(address, IqrfTrPnum.LEDG)
                    log.debug('[LEDG](OFF): ')
                    log.debug(response)
                elif command == 'blink' or command == 'bliknuti':
                    response = iqrf_tr.led_pulse(address, IqrfTrPnum.LEDG)
                    log.debug('[LEDG](BLINK): ')
                    log.debug(response)
                elif command == 'status' or command == 'stav':
                    response = iqrf_tr.led_status(address, IqrfTrPnum.LEDG)
                    log.debug('[LEDG](STATUS): ')
                    log.debug(response)
                else:
                    log.debug('Unknown command')
                    content = 'Neznamy prikaz!'
                    gsm.send_sms(i['number'], content)
            elif device == 'ledr':
                if command == 'on' or command == 'zapnout':
                    response = iqrf_tr.led_on(address, IqrfTrPnum.LEDR)
                    log.debug('[LEDG](ON): ')
                    log.debug(response)
                elif command == 'off' or command == 'vypnout':
                    response = iqrf_tr.led_off(address, IqrfTrPnum.LEDR)
                    log.debug('[LEDG](OFF): ')
                    log.debug(response)
                elif command == 'blink' or command == 'bliknuti':
                    response = iqrf_tr.led_pulse(address, IqrfTrPnum.LEDR)
                    log.debug('[LEDG](BLINK): ')
                    log.debug(response)
                elif command == 'status' or command == 'stav':
                    response = iqrf_tr.led_status(address, IqrfTrPnum.LEDR)
                    log.debug('[LEDG](STATUS): ')
                    log.debug(response)
                else:
                    log.debug('Unknown command')
                    content = 'Neznamy prikaz!'
                    gsm.send_sms(i['number'], content)
            elif device == 'socket' or device == 'zasuvka':
                if command == 'on' or command == 'zapnout':
                    response = smart_socket.set(address, 1)
                    log.debug('[Smart socket](ON): ')
                    log.debug(response)
                    if sms_feedback and response['response'][6] == 0x00:
                        content = 'Zasuvka byla zapnuta.'
                        gsm.send_sms(i['number'], content)
                elif command == 'off' or command == 'vypnout':
                    response = smart_socket.set(address, 0)
                    log.debug('[Smart socket](OFF): ')
                    log.debug(response)
                    if sms_feedback and response['response'][6] == 0x00:
                        content = 'Zasuvka byla vypnuta.'
                        gsm.send_sms(i['number'], content)
                elif command == 'status' or command == 'stav':
                    response = smart_socket.get(address)
                    log.debug('[Smart socket](STATUS): ')
                    log.debug(response)
                else:
                    log.debug('Unknown command')
                    content = 'Neznamy prikaz!'
                    gsm.send_sms(i['number'], content)
            else:
                log.debug('Uknown device')
                content = 'Nezname zarizeni!'
                gsm.send_sms(i['number'], content)
        gsm.delete_sms(i['id'])
    threading.Timer(1, read_sms, [gsm, iqrf, config, log]).start()


if __name__ == '__main__':
    sys.exit(main())
