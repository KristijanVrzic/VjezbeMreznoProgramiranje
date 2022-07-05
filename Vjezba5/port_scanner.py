import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

remoteServer = input("Please enter the adress you wish to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)
print("-" * 60)
print("Scanning: ", remoteServerIP)
print("-" * 60)


port1 = int(input("Enter port num1: "))
port2 = int(input("Enter port num2: "))
t1 = datetime.now()

for port in range(port1, port2):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServerIP, port))
    if result == 0:
            print("Port {}:           Open".format(port))
            sock.close()

t2 = datetime.now()
total = t2 - t1
print("Scanning complete in: ", total)