import sys
import threading

from rpigw.util.config import Config
from rpigw.transport.gsm import Gsm
from rpigw.transport.iqrf import Iqrf
from rpigw.device.iqrf_tr import IqrfTr, IqrfTrPnum
from rpigw.device.smart_socket import SmartSocket


def main():
    config_file = "./../../test/config.yml"
    config = Config(config_file).read()
    gsm = Gsm(config)
    iqrf = Iqrf(config)
    gsm.write('AT')
    print(gsm.read())
    read_sms(gsm, iqrf)
    return 0


def read_sms(gsm, iqrf):
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
                print('[THERMOMETER]: ')
                print(response)
                content = 'Teplota: ' + str(temperature['float'])
                gsm.send_sms(i['number'], content)
        elif len(array) is 3:
            device = array[0].lower()
            address = int(array[1])
            command = array[2].lower()
            if device == 'ledg':
                if command == 'on' or command == 'zapnout':
                    response = iqrf_tr.led_on(address, IqrfTrPnum.LEDG)
                    print('[LEDG](ON): ')
                    print(response)
                elif command == 'off' or command == 'vypnout':
                    response = iqrf_tr.led_off(address, IqrfTrPnum.LEDG)
                    print('[LEDG](OFF): ')
                    print(response)
                elif command == 'blink' or command == 'bliknuti':
                    response = iqrf_tr.led_pulse(address, IqrfTrPnum.LEDG)
                    print('[LEDG](BLINK): ')
                    print(response)
                elif command == 'status' or command == 'stav':
                    response = iqrf_tr.led_status(address, IqrfTrPnum.LEDG)
                    print('[LEDG](STATUS): ')
                    print(response)
                else:
                    print('Unknown command')
                    content = 'Neznamy prikaz!'
                    gsm.send_sms(i['number'], content)
            elif device == 'ledr':
                if command == 'on' or command == 'zapnout':
                    response = iqrf_tr.led_on(address, IqrfTrPnum.LEDR)
                    print('[LEDG](ON): ')
                    print(response)
                elif command == 'off' or command == 'vypnout':
                    response = iqrf_tr.led_off(address, IqrfTrPnum.LEDR)
                    print('[LEDG](OFF): ')
                    print(response)
                elif command == 'blink' or command == 'bliknuti':
                    response = iqrf_tr.led_pulse(address, IqrfTrPnum.LEDR)
                    print('[LEDG](BLINK): ')
                    print(response)
                elif command == 'status' or command == 'stav':
                    response = iqrf_tr.led_status(address, IqrfTrPnum.LEDR)
                    print('[LEDG](STATUS): ')
                    print(response)
                else:
                    print('Unknown command')
                    content = 'Neznamy prikaz!'
                    gsm.send_sms(i['number'], content)
            elif device == 'socket' or device == 'zasuvka':
                if command == 'on' or command == 'zapnout':
                    response = smart_socket.set(address, 1)
                    print('[Smart socket](ON): ')
                    print(response)
                elif command == 'off' or command == 'vypnout':
                    response = smart_socket.set(address, 0)
                    print('[Smart socket](OFF): ')
                    print(response)
                elif command == 'status' or command == 'stav':
                    response = smart_socket.get(address)
                    print('[Smart socket](STATUS): ')
                    print(response)
                else:
                    print('Unknown command')
                    content = 'Neznamy prikaz!'
                    gsm.send_sms(i['number'], content)
            else:
                print('Uknown device')
                content = 'Nezname zarizeni!'
                gsm.send_sms(i['number'], content)
        gsm.delete_sms(i['id'])
    threading.Timer(1, read_sms, [gsm, iqrf]).start()


if __name__ == "__main__":
    sys.exit(main())
