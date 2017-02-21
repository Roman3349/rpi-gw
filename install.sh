#!/bin/bash

# Instalation script for Raspberry Pi IQRF and GSM gateway

# Install application
sudo python3 setup.py install

# Copy SystemD manifest to SystemD directory
sudo cp rpigw.service /lib/systemd/system/rpigw.service
sudo chmod 644 /lib/systemd/system/rpigw.service

# Make directory in /etc/ for a configuration file and copy it here
sudo mkdir /etc/rpigw/
sudo cp test/config.yml /etc/rpigw/config.yml
sudo chmod 644 /etc/rpigw/config.yml

# Enable and start SystemD service
sudo systemctl enable rpigw.service
sudo systemctl start rpigw.service
