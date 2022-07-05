from queue import Queue
import socket
import threading
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

target = input("Enter the adress you wish to scan: ")
remoteServerIP = socket.gethostbyname(target)

print("-" * 60)
print("Scanning: ", remoteServerIP)
print("-" * 60)

t1 = datetime.now()

queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        socket.setdefaulttimeout(5)
        return True
    except:
        return False

def get_ports():
     port1 = int(input("First port: "))
     port2 = int(input("Second port: "))
     print("-" * 60)
     for ports in range(port1,port2):
        #ports = ports.split()
        ports = (int, ports) #list(map(int, ports))
        for port in ports:
            queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)


def run_scanner(threads):

    get_ports()

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("Open ports are:", open_ports)


run_scanner(200)

t2 = datetime.now()

total = t2 - t1

print("Scan complete in : ", total)