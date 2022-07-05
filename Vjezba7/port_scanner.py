import socket
import multiprocessing
from datetime import datetime
from multiprocessing import Pool


def f(port):
    s = socket.socket()
    #socket.setdefaulttimeout(1)
      
    try:
        con = s.connect((remoteServer,port))
        print("Success:" + str(port))
        s.close()
    except:
        print("Didn't work:" + str(port))
        s.close()
        pass

def port_list():
        port_range = input("Enter the port range you want to scan").split('-')
        for i in range(int(port_range[0]), int(port_range[1]) + 1):
             list1.append(int(i))

        print(list1)

if __name__ == '__main__':
    
    remoteServer = input("Enter the adress you wish to scan: ")
    
    remoteServerIP = socket.gethostbyname(remoteServer)

    socket.setdefaulttimeout(1)

    print("-" * 60)
    print("Scanning host: ", remoteServerIP)
    print("-" * 60)

    #port1 = int(input("Unesite prvi port: "))
    #port2 = int(input("Unesite drugi port: "))

    t1 = datetime.now()

    list1 = []
    
    port_list()
    broj_cpu = 2
    #pool = multiprocessing.Pool(processes=broj_cpu*2)
    with Pool(8) as p:
        print(p.map(f,list1))
        print("Done")

    t2 = datetime.now()

    total = t2 - t1

    print("Complete in : ", total)