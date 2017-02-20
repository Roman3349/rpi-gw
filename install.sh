#!/bin/bash

# Instalation script for Raspberry Pi IQRF and GSM gateway

sudo python3 setup.py install

sudo cp rpigw.service /lib/systemd/system/
sudo mkdir /root/rpigw/
sudo cp test/config.yml /root/rpigw/config.yml

sudo systemctl enable rpigw.service
sudo systemctl start rpigw.service
