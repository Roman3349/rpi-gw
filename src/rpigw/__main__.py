import sys

from rpigw.util.config import Config
from rpigw.transport.gsm import Gsm


def main():
    config_file = "./../../test/config.yml"
    config = Config(config_file).read()
    gsm = Gsm(config)
    gsm.write('AT')
    print(gsm.read())
    print(gsm.read_sms('ALL'))
    #gsm.send_sms('+420702888729', 'Test')
    #print(gsm.read())
    #gsm.delete_sms(1)
    #print(gsm.read())
    return 0

if __name__ == "__main__":
    sys.exit(main())
