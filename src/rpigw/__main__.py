import sys
import threading

from rpigw.util.config import Config
from rpigw.transport.gsm import Gsm
from rpigw.transport.iqrf import Iqrf
from rpigw.device.iqrf_tr import IqrfTr, IqrfTrPnum


def main():
    config_file = "./../../test/config.yml"
    config = Config(config_file).read()
    gsm = Gsm(config)
    iqrf = Iqrf(config)
    gsm.write('AT')
    print(gsm.read())
    read_sms(gsm, iqrf)
    # print(gsm.read_sms('ALL'))
    # gsm.send_sms('+420702888729', 'Test')
    # print(gsm.read())
    # gsm.delete_sms(1)
    # print(gsm.read())
    return 0


def read_sms(gsm, iqrf):
    iqrf_tr = IqrfTr(iqrf)
    sms = gsm.read_sms('REC UNREAD')
    for i in sms:
        content = i['content']
        array = content.split()
        if len(array) is 3:
            device = array[0].lower()
            address = array[1]
            command = array[2].lower()
            if device == 'ledg':
                if command == 'on' or command == 'zapnout':
                    # TODO: send request to module
                    print('On')
                elif command == 'off' or command == 'vypnout':
                    # TODO: send request to module
                    print('Off')
                elif command == 'blink' or command == 'bliknuti':
                    response = iqrf_tr.pulse_led(address, IqrfTrPnum.LEDG)
                elif command == 'status' or command == 'stav':
                    # TODO: send request to module
                    print('Status')
                else:
                    print('Unknown')
                    content = 'Unknown command!\r\nNeznamy prikaz!'
                    # gsm.send_sms(i['number'], content)
            elif device == 'ledr':
                if command == 'on' or command == 'zapnout':
                    # TODO: send request to module
                    print('On')
                elif command == 'off' or command == 'vypnout':
                    # TODO: send request to module
                    print('Off')
                elif command == 'blink' or command == 'bliknuti':
                    response = iqrf_tr.pulse_led(address, IqrfTrPnum.LEDR)
                    print(response)
                elif command == 'status' or command == 'stav':
                    # TODO: send request to module
                    print('Status')
                else:
                    print('Unknown')
                    content = 'Unknown command!\r\nNeznamy prikaz!'
                    # gsm.send_sms(i['number'], content)
            elif device == 'socket' or device == 'zasuvka':
                if command == 'on' or command == 'zapnout':
                    # TODO: send request to smart socket
                    iqrf_tr = IqrfTr(iqrf)
                    iqrf_tr.pulse_led(IqrfTrPnum.LEDG)
                    print('On')
                elif command == 'off' or command == 'vypnout':
                    # TODO: send request to smart socket
                    print('Off')
                elif command == 'status' or command == 'stav':
                    # TODO: send request to smart socket
                    print('Status')
                else:
                    print('Unknown')
                    content = 'Unknown command!\r\nNeznamy prikaz!'
                    # gsm.send_sms(i['number'], content)
            else:
                print('Uknown device')
    threading.Timer(1, read_sms, [gsm, iqrf]).start()

if __name__ == "__main__":
    sys.exit(main())
