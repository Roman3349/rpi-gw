import os, sys, logging

from rpigw.util.config import Config
from rpigw.protocols.gsm import Gsm

def main():
    config_file = "./../../test/config.yml"
    config = Config(config_file).read()
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    gsm = Gsm(config)
    return 0

if __name__ == "__main__":
    sys.exit(main())
